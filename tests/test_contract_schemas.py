import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from runtime.contracts.validator import validate_action_contract, validate_action_receipt

class ContractValidationTests(unittest.TestCase):
    def load(self, path):
        return json.loads((ROOT / path).read_text())

    def test_valid_contract_and_receipt(self):
        contract = self.load('fixtures/yh-rex0/synthetic-action-contract.valid.json')
        receipt = self.load('fixtures/yh-rex0/real-ego-smoke-receipt.valid.json')
        self.assertEqual(validate_action_contract(contract), [])
        self.assertEqual(validate_action_receipt(receipt), [])

    def test_revoked_contract_rejected(self):
        contract = self.load('fixtures/yh-rex0/synthetic-action-contract.valid.json')
        contract['revoked'] = True
        self.assertIn('contract is revoked', validate_action_contract(contract))

    def test_commit_requires_principal_approval_receipt(self):
        contract = self.load('fixtures/yh-rex0/synthetic-action-contract.valid.json')
        contract['action_class'] = 'COMMIT'
        contract['requires_approval']['principal'] = True
        self.assertIn('missing principal approval receipt', validate_action_contract(contract))

if __name__ == '__main__':
    unittest.main()
