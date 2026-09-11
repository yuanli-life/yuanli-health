from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import jsonschema

from runtime.rex0.authority import authority_errors

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / 'contracts'


def _load_schema(name: str) -> dict[str, Any]:
    return json.loads((SCHEMA_DIR / name).read_text())


def _parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace('Z', '+00:00')).astimezone(timezone.utc)


def _schema_errors(instance: dict[str, Any], schema_name: str) -> list[str]:
    schema = _load_schema(schema_name)
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    return [f"schema: {e.message}" for e in sorted(validator.iter_errors(instance), key=lambda e: list(e.path))]


def validate_action_contract(contract: dict[str, Any], now: datetime | None = None) -> list[str]:
    errors = _schema_errors(contract, 'action-contract-v1.schema.json')
    if errors:
        return errors
    now = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    if contract.get('revoked'):
        errors.append('contract is revoked')
    if _parse_time(contract['expires_at']) <= now:
        errors.append('contract is expired')
    for error in authority_errors(contract):
        if error.startswith('missing_') and error.endswith('_approval'):
            role = error[len('missing_'):-len('_approval')]
            errors.append(f'missing {role} approval receipt')
        else:
            errors.append(error)
    if set(contract.get('allowed_actions', [])) & set(contract.get('forbidden_actions', [])):
        errors.append('allowed_actions overlaps forbidden_actions')
    return errors


def validate_action_receipt(receipt: dict[str, Any]) -> list[str]:
    return _schema_errors(receipt, 'action-receipt-v1.schema.json')
