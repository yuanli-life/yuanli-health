from __future__ import annotations

from typing import Any

from runtime.rex0.authority import worker_can_execute_action_class


class PolicyViolation(ValueError):
    pass


def assert_dispatch_allowed(worker: dict[str, Any], dispatch: dict[str, Any]) -> None:
    if worker.get('status') != 'active':
        raise PolicyViolation('worker_not_active')
    principal_ref = dispatch.get('principal_ref')
    if principal_ref not in set(worker.get('principal_refs') or []):
        raise PolicyViolation('principal_scope_denied')
    if dispatch.get('lease_owner') not in (None, worker.get('worker_id')):
        raise PolicyViolation('wrong_lease_owner')
    if not worker_can_execute_action_class(worker.get('max_action_class', 'READ'), dispatch.get('action_class', '')):
        raise PolicyViolation('worker_action_class_denied')


def assert_receipt_matches_dispatch(receipt: dict[str, Any], dispatch: dict[str, Any]) -> None:
    if receipt.get('contract_id') != dispatch.get('contract_id'):
        raise PolicyViolation('receipt_contract_mismatch')
    if receipt.get('principal_ref') != dispatch.get('principal_ref'):
        raise PolicyViolation('receipt_principal_mismatch')
    if receipt.get('lease_token') != dispatch.get('lease_token'):
        raise PolicyViolation('receipt_lease_mismatch')
