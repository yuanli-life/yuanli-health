import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from runtime.rex0.authority import authority_errors, worker_can_execute_action_class


def contract(action_class, roles=(), destructive_confirmed=False):
    return {
        'action_class': action_class,
        'approval_receipts': [
            {'actor_role': role, 'approved_at': '2026-09-11T11:00:00Z', 'receipt_ref': f'APR-{role}'}
            for role in roles
        ],
        'payload': {'destructive_confirmed': destructive_confirmed},
        # Caller-declared flags intentionally cannot weaken the runtime matrix.
        'requires_approval': {'principal': False, 'clinician': False, 'steward': False},
    }


class Rex0AuthorityTests(unittest.TestCase):
    def test_read_requires_no_human_approval(self):
        self.assertEqual(authority_errors(contract('READ')), [])

    def test_prepare_requires_steward(self):
        self.assertIn('missing_steward_approval', authority_errors(contract('PREPARE')))
        self.assertEqual(authority_errors(contract('PREPARE', ['steward'])), [])

    def test_commit_requires_steward_and_principal(self):
        self.assertIn('missing_principal_approval', authority_errors(contract('COMMIT', ['steward'])))
        self.assertEqual(authority_errors(contract('COMMIT', ['steward', 'principal'])), [])

    def test_clinical_requires_all_three_roles(self):
        errors = authority_errors(contract('CLINICAL', ['steward', 'principal']))
        self.assertIn('missing_clinician_approval', errors)
        self.assertEqual(authority_errors(contract('CLINICAL', ['steward', 'principal', 'clinician'])), [])

    def test_destructive_requires_all_roles_and_explicit_confirmation(self):
        roles = ['steward', 'principal', 'clinician']
        self.assertIn('missing_destructive_confirmation', authority_errors(contract('DESTRUCTIVE', roles)))
        self.assertEqual(authority_errors(contract('DESTRUCTIVE', roles, True)), [])

    def test_read_only_worker_cannot_execute_higher_class(self):
        self.assertTrue(worker_can_execute_action_class('READ', 'READ'))
        self.assertFalse(worker_can_execute_action_class('READ', 'PREPARE'))
        self.assertFalse(worker_can_execute_action_class('READ', 'CLINICAL'))


if __name__ == '__main__':
    unittest.main()
