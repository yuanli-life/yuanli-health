import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from runtime.ego_runner.runner import PolicyError, validate_runner_policy

class EgoRunnerPolicyTests(unittest.TestCase):
    def setUp(self):
        self.contract = json.loads((ROOT / 'fixtures/yh-rex0/synthetic-action-contract.valid.json').read_text())

    def test_valid_read_contract(self):
        validate_runner_policy(self.contract)

    def test_rejects_disallowed_domain(self):
        c = copy.deepcopy(self.contract)
        c['payload']['url'] = 'https://openai.com/'
        with self.assertRaisesRegex(PolicyError, 'domain not allowlisted'):
            validate_runner_policy(c)

    def test_rejects_secret_shaped_payload(self):
        c = copy.deepcopy(self.contract)
        c['payload']['api_token'] = 'secret-value'
        with self.assertRaisesRegex(PolicyError, 'secret-shaped key'):
            validate_runner_policy(c)

    def test_rejects_unsupported_action(self):
        c = copy.deepcopy(self.contract)
        c['allowed_actions'] = ['open_page', 'click_submit']
        with self.assertRaisesRegex(PolicyError, 'unsupported action'):
            validate_runner_policy(c)

if __name__ == '__main__':
    unittest.main()
