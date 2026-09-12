from pathlib import Path
import json
import re
import jsonschema

ROOT = Path('lab/yh-lab1')
FORBIDDEN_KEYS = {'name','phone','email','id_number','cookie','password','token','authorization','apple_health_raw','clinical_document_raw'}


def load_jsonl(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def nested_keys(value):
    if isinstance(value, dict):
        for k, v in value.items():
            yield k.lower()
            yield from nested_keys(v)
    elif isinstance(value, list):
        for item in value:
            yield from nested_keys(item)


def test_fixture_counts_and_unique_ids():
    golden = load_jsonl(ROOT / 'fixtures/golden.jsonl')
    hard = load_jsonl(ROOT / 'fixtures/hard_negative.jsonl')
    principals = load_jsonl(ROOT / 'fixtures/synthetic_principals.jsonl')
    assert (len(golden), len(hard), len(principals)) == (20, 20, 10)
    case_ids = [x['case_id'] for x in golden + hard]
    assert len(case_ids) == len(set(case_ids))
    principal_ids = [x['principal_variant'] for x in principals]
    assert len(principal_ids) == len(set(principal_ids))


def test_fixtures_validate_against_schemas():
    case_schema = json.loads((ROOT / 'schemas/eval_case.schema.json').read_text())
    principal_schema = json.loads((ROOT / 'schemas/synthetic_principal.schema.json').read_text())
    for row in load_jsonl(ROOT / 'fixtures/golden.jsonl') + load_jsonl(ROOT / 'fixtures/hard_negative.jsonl'):
        jsonschema.validate(row, case_schema)
    for row in load_jsonl(ROOT / 'fixtures/synthetic_principals.jsonl'):
        jsonschema.validate(row, principal_schema)


def test_no_phi_or_secret_shaped_keys_in_fixtures():
    for path in [ROOT/'fixtures/golden.jsonl', ROOT/'fixtures/hard_negative.jsonl', ROOT/'fixtures/synthetic_principals.jsonl']:
        for row in load_jsonl(path):
            assert FORBIDDEN_KEYS.isdisjoint(set(nested_keys(row)))
