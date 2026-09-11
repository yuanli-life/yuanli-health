from __future__ import annotations

import json
from typing import Any


def canonical_json(value: Any) -> str:
    """Return deterministic UTF-8 JSON used by the R2 signing boundary.

    R2 contracts intentionally avoid floats and non-JSON values. This helper mirrors
    the Edge Runtime's recursive key-sorted compact representation.
    """
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False)


def canonical_bytes(value: Any) -> bytes:
    return canonical_json(value).encode('utf-8')
