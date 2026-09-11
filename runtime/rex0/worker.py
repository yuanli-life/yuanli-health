from __future__ import annotations

import argparse
import json
import os
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.contracts.validator import validate_action_contract, validate_action_receipt
from runtime.ego_runner.runner import execute_contract
from runtime.rex0.crypto import sign_json_b64, verify_json_b64
from runtime.rex0.worker_policy import assert_dispatch_allowed, assert_receipt_matches_dispatch


def _iso_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')


def _fresh_nonce(prefix: str) -> str:
    return f'{prefix}-{uuid.uuid4().hex}'


def load_secret_b64(path: str | None, env_name: str) -> str:
    if path:
        value = Path(path).read_text().strip()
    else:
        value = os.environ.get(env_name, '').strip()
    if not value:
        raise RuntimeError(f'missing private key: {env_name}')
    return value


def post_json(url: str, body: dict[str, Any], timeout: int = 30) -> dict[str, Any]:
    request = Request(
        url,
        data=json.dumps(body, separators=(',', ':'), ensure_ascii=False).encode('utf-8'),
        headers={'content-type': 'application/json', 'user-agent': 'yuanli-health-rex0-worker/0.1'},
        method='POST',
    )
    with urlopen(request, timeout=timeout) as response:
        payload = response.read().decode('utf-8')
        return json.loads(payload) if payload else {}


def signed_worker_envelope(
    *,
    worker_id: str,
    private_key_b64: str,
    op: str,
    principal_ref: str | None,
    body: dict[str, Any] | None = None,
    nonce: str | None = None,
    timestamp: str | None = None,
) -> dict[str, Any]:
    envelope = {
        'worker_id': worker_id,
        'nonce': nonce or _fresh_nonce(op),
        'timestamp': timestamp or _iso_now(),
        'op': op,
        'principal_ref': principal_ref,
        'body': body,
    }
    signature = sign_json_b64(private_key_b64, envelope)
    return {**envelope, 'signature_b64': signature}


def verify_dispatch_signature(dispatch: dict[str, Any], issuer_public_keys: dict[str, str]) -> None:
    issuer_id = dispatch.get('issuer_id')
    public_key = issuer_public_keys.get(issuer_id)
    if not public_key:
        raise RuntimeError(f'unknown issuer: {issuer_id}')
    signed_body = {
        'issuer_id': issuer_id,
        'nonce': dispatch.get('contract_nonce'),
        'contract': dispatch.get('contract'),
    }
    if not verify_json_b64(public_key, signed_body, dispatch.get('issuer_signature_b64', '')):
        raise RuntimeError('issuer signature verification failed')


def execute_dispatch(
    *,
    worker: dict[str, Any],
    dispatch: dict[str, Any],
    issuer_public_keys: dict[str, str],
) -> dict[str, Any]:
    verify_dispatch_signature(dispatch, issuer_public_keys)
    contract = dispatch.get('contract') or {}
    contract_errors = validate_action_contract(contract)
    if contract_errors:
        raise RuntimeError('invalid dispatched contract: ' + '; '.join(contract_errors))

    policy_view = {
        'contract_id': dispatch.get('contract_id'),
        'principal_ref': dispatch.get('principal_ref'),
        'action_class': dispatch.get('action_class') or contract.get('action_class'),
        'lease_owner': dispatch.get('lease_owner'),
        'lease_token': dispatch.get('lease_token'),
    }
    assert_dispatch_allowed(worker, policy_view)

    receipt = execute_contract(contract)
    receipt['lease_token'] = str(dispatch['lease_token'])
    receipt_errors = validate_action_receipt(receipt)
    if receipt_errors:
        raise RuntimeError('invalid R2 receipt: ' + '; '.join(receipt_errors))
    assert_receipt_matches_dispatch(receipt, policy_view)
    return receipt


def run_once(
    *,
    pull_url: str,
    receipt_url: str,
    fail_url: str,
    worker: dict[str, Any],
    private_key_b64: str,
    issuer_public_keys: dict[str, str],
) -> dict[str, Any]:
    principal_ref = worker['principal_refs'][0]
    pull_envelope = signed_worker_envelope(
        worker_id=worker['worker_id'],
        private_key_b64=private_key_b64,
        op='pull',
        principal_ref=principal_ref,
    )
    dispatch = post_json(pull_url, pull_envelope)
    if dispatch.get('status') == 'NO_WORK':
        return dispatch
    if dispatch.get('status') != 'DISPATCH':
        raise RuntimeError(f'pull rejected: {dispatch}')

    try:
        receipt = execute_dispatch(worker=worker, dispatch=dispatch, issuer_public_keys=issuer_public_keys)
    except Exception as exc:
        fail_body = {
            'contract_id': dispatch.get('contract_id'),
            'lease_token': dispatch.get('lease_token'),
            'error_class': 'WORKER_EXECUTION_ERROR',
            'error_detail': str(exc)[:500],
        }
        fail_envelope = signed_worker_envelope(
            worker_id=worker['worker_id'],
            private_key_b64=private_key_b64,
            op='fail',
            principal_ref=principal_ref,
            body=fail_body,
        )
        failure_result = post_json(fail_url, fail_envelope)
        raise RuntimeError(f'worker execution failed; failure receipt={failure_result}') from exc

    receipt_body = {'receipt': receipt, 'lease_token': dispatch['lease_token']}
    receipt_envelope = signed_worker_envelope(
        worker_id=worker['worker_id'],
        private_key_b64=private_key_b64,
        op='receipt',
        principal_ref=principal_ref,
        body=receipt_body,
    )
    return post_json(receipt_url, receipt_envelope)


def main() -> None:
    parser = argparse.ArgumentParser(description='YH-REX0 R2 authenticated one-shot worker')
    parser.add_argument('--pull-url', required=True)
    parser.add_argument('--receipt-url', required=True)
    parser.add_argument('--fail-url', required=True)
    parser.add_argument('--worker-config', required=True, help='JSON file with worker_id/principal_refs/max_action_class/status')
    parser.add_argument('--issuer-public-keys', required=True, help='JSON map issuer_id -> Ed25519 public key b64')
    parser.add_argument('--private-key-file')
    args = parser.parse_args()

    worker = json.loads(Path(args.worker_config).read_text())
    issuer_public_keys = json.loads(Path(args.issuer_public_keys).read_text())
    private_key_b64 = load_secret_b64(args.private_key_file, 'YH_REX0_WORKER_PRIVATE_KEY_B64')
    result = run_once(
        pull_url=args.pull_url,
        receipt_url=args.receipt_url,
        fail_url=args.fail_url,
        worker=worker,
        private_key_b64=private_key_b64,
        issuer_public_keys=issuer_public_keys,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
