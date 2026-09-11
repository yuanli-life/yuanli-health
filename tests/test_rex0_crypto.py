import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from runtime.rex0.crypto import generate_keypair_b64, sign_json_b64, verify_json_b64


class Rex0CryptoTests(unittest.TestCase):
    def test_valid_signature_verifies_and_tamper_fails(self):
        private_b64, public_b64 = generate_keypair_b64()
        body = {
            'issuer_id': 'issuer-synthetic-001',
            'nonce': 'nonce-001',
            'contract': {
                'contract_id': 'ACT-YH-REX0-R2-001',
                'principal_ref': 'synthetic-principal-A',
                'action_class': 'READ',
            },
        }
        signature = sign_json_b64(private_b64, body)
        self.assertTrue(verify_json_b64(public_b64, body, signature))

        tampered = copy.deepcopy(body)
        tampered['contract']['principal_ref'] = 'synthetic-principal-B'
        self.assertFalse(verify_json_b64(public_b64, tampered, signature))

    def test_key_order_does_not_change_signature_bytes(self):
        private_b64, public_b64 = generate_keypair_b64()
        a = {'b': 2, 'a': {'y': 2, 'x': 1}}
        b = {'a': {'x': 1, 'y': 2}, 'b': 2}
        signature = sign_json_b64(private_b64, a)
        self.assertTrue(verify_json_b64(public_b64, b, signature))


if __name__ == '__main__':
    unittest.main()
