import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from runtime.rex0.worker_policy import PolicyViolation, assert_dispatch_allowed, assert_receipt_matches_dispatch


class Rex0WorkerPolicyTests(unittest.TestCase):
    def setUp(self):
        self.worker = {
            'worker_id': 'worker-A',
            'principal_refs': ['synthetic-principal-A'],
            'max_action_class': 'READ',
            'status': 'active',
        }
        self.dispatch = {
            'contract_id': 'ACT-YH-REX0-R2-001',
            'principal_ref': 'synthetic-principal-A',
            'action_class': 'READ',
            'lease_owner': 'worker-A',
            'lease_token': 'lease-001',
        }

    def test_worker_a_can_execute_principal_a_read(self):
        assert_dispatch_allowed(self.worker, self.dispatch)

    def test_worker_b_scope_cannot_claim_principal_a(self):
        worker_b = dict(self.worker, worker_id='worker-B', principal_refs=['synthetic-principal-B'])
        with self.assertRaisesRegex(PolicyViolation, 'principal_scope_denied'):
            assert_dispatch_allowed(worker_b, self.dispatch)

    def test_revoked_worker_rejected(self):
        revoked = dict(self.worker, status='revoked')
        with self.assertRaisesRegex(PolicyViolation, 'worker_not_active'):
            assert_dispatch_allowed(revoked, self.dispatch)

    def test_wrong_lease_owner_rejected(self):
        wrong = dict(self.dispatch, lease_owner='worker-B')
        with self.assertRaisesRegex(PolicyViolation, 'wrong_lease_owner'):
            assert_dispatch_allowed(self.worker, wrong)

    def test_receipt_must_match_contract_principal_and_lease(self):
        receipt = {
            'contract_id': self.dispatch['contract_id'],
            'principal_ref': self.dispatch['principal_ref'],
            'lease_token': self.dispatch['lease_token'],
        }
        assert_receipt_matches_dispatch(receipt, self.dispatch)
        with self.assertRaisesRegex(PolicyViolation, 'receipt_principal_mismatch'):
            assert_receipt_matches_dispatch(dict(receipt, principal_ref='synthetic-principal-B'), self.dispatch)
        with self.assertRaisesRegex(PolicyViolation, 'receipt_lease_mismatch'):
            assert_receipt_matches_dispatch(dict(receipt, lease_token='lease-002'), self.dispatch)


if __name__ == '__main__':
    unittest.main()
