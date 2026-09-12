from __future__ import annotations

import json
from pathlib import Path

SPACE_ROOT = Path(__file__).resolve().parent.parent
CANDIDATE_DATA_ROOTS = (SPACE_ROOT / 'fixtures', SPACE_ROOT.parent / 'fixtures')


def _data_root() -> Path:
    for root in CANDIDATE_DATA_ROOTS:
        if (root / 'golden.jsonl').exists():
            return root
    raise FileNotFoundError('YH-LAB1 fixture root not found')


def load_jsonl(name: str) -> list[dict]:
    path = _data_root() / name
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def load_cases() -> list[dict]:
    return load_jsonl('golden.jsonl') + load_jsonl('hard_negative.jsonl')


def load_principals() -> list[dict]:
    return load_jsonl('synthetic_principals.jsonl')


def find_case(case_id: str) -> dict:
    for case in load_cases():
        if case['case_id'] == case_id:
            return case
    raise KeyError(f'Unknown case_id: {case_id}')
