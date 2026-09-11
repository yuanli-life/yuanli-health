from __future__ import annotations

from typing import Any

ACTION_RANK = {
    'READ': 0,
    'PREPARE': 1,
    'COMMIT': 2,
    'CLINICAL': 3,
    'DESTRUCTIVE': 4,
}

REQUIRED_ROLES = {
    'READ': (),
    'PREPARE': ('steward',),
    'COMMIT': ('steward', 'principal'),
    'CLINICAL': ('steward', 'principal', 'clinician'),
    'DESTRUCTIVE': ('steward', 'principal', 'clinician'),
}


def approval_roles(contract: dict[str, Any]) -> set[str]:
    return {
        item.get('actor_role')
        for item in contract.get('approval_receipts', [])
        if isinstance(item, dict) and isinstance(item.get('actor_role'), str)
    }


def authority_errors(contract: dict[str, Any]) -> list[str]:
    action_class = contract.get('action_class')
    if action_class not in ACTION_RANK:
        return ['invalid_action_class']
    roles = approval_roles(contract)
    errors = [f'missing_{role}_approval' for role in REQUIRED_ROLES[action_class] if role not in roles]
    if action_class == 'DESTRUCTIVE' and contract.get('payload', {}).get('destructive_confirmed') is not True:
        errors.append('missing_destructive_confirmation')
    return errors


def worker_can_execute_action_class(max_action_class: str, action_class: str) -> bool:
    if max_action_class not in ACTION_RANK or action_class not in ACTION_RANK:
        return False
    return ACTION_RANK[action_class] <= ACTION_RANK[max_action_class]
