from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.contracts.validator import validate_action_contract, validate_action_receipt

SUPPORTED_ACTIONS = {'open_page', 'read_title'}
SECRET_KEY = re.compile(r'(token|secret|password|passwd|cookie|authorization|api[_-]?key)', re.I)

class PolicyError(ValueError):
    pass


def _find_secret_key(value, path='payload'):
    if isinstance(value, dict):
        for key, child in value.items():
            if SECRET_KEY.search(str(key)):
                return f'{path}.{key}'
            found = _find_secret_key(child, f'{path}.{key}')
            if found:
                return found
    elif isinstance(value, list):
        for i, child in enumerate(value):
            found = _find_secret_key(child, f'{path}[{i}]')
            if found:
                return found
    return None


def validate_runner_policy(contract: dict) -> None:
    errors = validate_action_contract(contract)
    if errors:
        raise PolicyError('; '.join(errors))
    if contract['action_class'] != 'READ':
        raise PolicyError('v0.1 ego runner supports READ only')
    unsupported = set(contract['allowed_actions']) - SUPPORTED_ACTIONS
    if unsupported:
        raise PolicyError(f'unsupported action: {sorted(unsupported)}')
    secret_path = _find_secret_key(contract.get('payload', {}))
    if secret_path:
        raise PolicyError(f'secret-shaped key rejected: {secret_path}')
    url = contract.get('payload', {}).get('url')
    if not isinstance(url, str):
        raise PolicyError('payload.url is required')
    parsed = urlparse(url)
    if parsed.scheme != 'https' or not parsed.hostname:
        raise PolicyError('only https URLs are allowed')
    if parsed.hostname not in set(contract['allowed_domains']):
        raise PolicyError(f'domain not allowlisted: {parsed.hostname}')


def _iso_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')


def execute_contract(contract: dict) -> dict:
    validate_runner_policy(contract)
    started = _iso_now()
    url = contract['payload']['url']
    task_name = f"YH-REX0 {contract['contract_id']}"
    script = f"""
const task = await useOrCreateTaskSpace({json.dumps(task_name)});
await openOrReuseTab({json.dumps(url)}, {{ wait: true, timeout: 20 }});
const title = await js('document.title');
const currentUrl = await js('location.href');
cliLog(JSON.stringify({{taskSpaceId: task.id, title, url: currentUrl, status: 'COMPLETED'}}));
"""
    proc = subprocess.run(
        ['ego-browser', 'nodejs'],
        input=script,
        text=True,
        capture_output=True,
        timeout=30,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f'ego-browser failed rc={proc.returncode}: {proc.stderr[-500:]}')
    combined = proc.stdout + '\n' + proc.stderr
    lines = [line.strip() for line in combined.splitlines() if line.strip().startswith('{')]
    if not lines:
        raise RuntimeError('ego-browser produced no structured result')
    result = json.loads(lines[-1])
    receipt = {
        'receipt_id': f"RCP-{contract['contract_id'][4:]}",
        'contract_id': contract['contract_id'],
        'execution_id': f"ego-task-{result['taskSpaceId']}",
        'principal_ref': contract['principal_ref'],
        'executor': {
            'plane': 'ego-browser',
            'runtime': 'ego-lite',
            'task_space_ref': result['taskSpaceId'],
        },
        'authority': {
            'principal_approved': False,
            'clinician_approved': False,
            'steward_approved': False,
        },
        'started_at': started,
        'finished_at': _iso_now(),
        'status': 'COMPLETED',
        'attempted_actions': [
            {'action': 'open_page', 'status': 'SUCCESS', 'target_ref': result['url']},
            {'action': 'read_title', 'status': 'SUCCESS', 'detail': result['title']},
        ],
        'external_reference': result['url'],
        'evidence_refs': [],
        'artifact_hashes': [],
        'error_class': 'NONE',
        'next_required_gate': None,
        'no_secret_attestation': True,
        'schema_version': 'action-receipt-v1',
    }
    receipt_errors = validate_action_receipt(receipt)
    if receipt_errors:
        raise RuntimeError('generated invalid receipt: ' + '; '.join(receipt_errors))
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--contract', required=True)
    parser.add_argument('--execute', action='store_true')
    args = parser.parse_args()
    contract = json.loads(Path(args.contract).read_text())
    validate_runner_policy(contract)
    if args.execute:
        print(json.dumps(execute_contract(contract), ensure_ascii=False, indent=2))
    else:
        print(json.dumps({'status': 'VALIDATED', 'contract_id': contract['contract_id']}))

if __name__ == '__main__':
    main()
