from __future__ import annotations

import base64
import hashlib
from typing import Any

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey

from runtime.rex0.canonical import canonical_bytes


def _b64e(raw: bytes) -> str:
    return base64.b64encode(raw).decode('ascii')


def _b64d(value: str) -> bytes:
    return base64.b64decode(value.encode('ascii'), validate=True)


def generate_keypair_b64() -> tuple[str, str]:
    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    private_raw = private_key.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption(),
    )
    public_raw = public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw,
    )
    return _b64e(private_raw), _b64e(public_raw)


def sign_json_b64(private_key_b64: str, body: Any) -> str:
    private_key = Ed25519PrivateKey.from_private_bytes(_b64d(private_key_b64))
    return _b64e(private_key.sign(canonical_bytes(body)))


def verify_json_b64(public_key_b64: str, body: Any, signature_b64: str) -> bool:
    try:
        public_key = Ed25519PublicKey.from_public_bytes(_b64d(public_key_b64))
        public_key.verify(_b64d(signature_b64), canonical_bytes(body))
        return True
    except Exception:
        return False


def public_key_fingerprint(public_key_b64: str) -> str:
    return hashlib.sha256(_b64d(public_key_b64)).hexdigest()
