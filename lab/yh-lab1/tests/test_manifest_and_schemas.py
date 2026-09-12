from pathlib import Path
import json
import yaml

ROOT = Path('lab/yh-lab1')


def test_manifest_freezes_exact_v01_contract():
    manifest = yaml.safe_load((ROOT / 'manifest.yaml').read_text())
    assert manifest['space_id'] == 'Hay2045/yh-lab1-intelligence-lab'
    assert manifest['dataset_id'] == 'Hay2045/yh-lab1-evals'
    assert manifest['visibility'] == 'private'
    assert manifest['fixture_counts'] == {'golden': 20, 'hard_negative': 20, 'synthetic_principal': 10}
    assert manifest['p0_failures'] == [
        'cross_principal_leakage',
        'fabricated_clinical_fact',
        'unauthorized_clinical_action',
        'secret_leakage',
    ]


def test_route_registry_has_exactly_three_declared_routes():
    routes = yaml.safe_load((ROOT / 'routes/routes.yaml').read_text())['routes']
    assert [r['route_id'] for r in routes] == ['route_qwen3', 'route_phi4mini', 'route_mistral7b']
    assert len(routes) == 3


def test_all_lab_schemas_are_valid_json_schema_documents():
    names = ['eval_case', 'synthetic_principal', 'adjudication', 'admission_receipt']
    for name in names:
        payload = json.loads((ROOT / f'schemas/{name}.schema.json').read_text())
        assert payload['$schema'] == 'https://json-schema.org/draft/2020-12/schema'
        assert payload['type'] == 'object'
