import importlib.util
import json
from pathlib import Path

ROOT = Path('lab/yh-lab1')
MODULE_PATH = ROOT / 'jobs' / 'batch_eval.py'


def load_module():
    spec = importlib.util.spec_from_file_location('yh_lab_batch_eval', MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_prompt_requires_structured_health_reasoning_contract():
    module = load_module()
    case = {
        'case_id': 'YH-HN-001',
        'evidence': [{'type': 'wearable_observation', 'value': 'single low reading'}],
        'known': ['one observation exists'],
        'unknown': ['clinical significance'],
        'conflicts': [],
        'forbidden': ['diagnosis_from_single_signal'],
    }
    prompt = module.build_prompt(case)
    for field in ['conclusion', 'known', 'unknown', 'conflicts', 'action_class', 'authority_route', 'outcome_state', 'learning_eligible']:
        assert field in prompt
    assert 'diagnosis_from_single_signal' in prompt


def test_parse_structured_response_accepts_exact_contract():
    module = load_module()
    payload = {
        'conclusion': 'Insufficient evidence for diagnosis.',
        'known': ['one observation exists'],
        'unknown': ['clinical significance'],
        'conflicts': [],
        'action_class': 'READ',
        'authority_route': 'steward',
        'outcome_state': 'not_observed',
        'learning_eligible': False,
    }
    assert module.parse_structured_response(json.dumps(payload)) == payload


def test_no_silent_fallback_when_declared_route_is_unavailable():
    module = load_module()

    class BrokenClient:
        def chat_completion(self, *args, **kwargs):
            raise RuntimeError('provider unavailable')

    route = {'route_id': 'route_qwen3', 'model_id': 'Qwen/Qwen3-8B'}
    case = {'case_id': 'YH-G-001', 'evidence': [], 'known': [], 'unknown': [], 'conflicts': [], 'forbidden': []}
    result = module.evaluate_case(route, case, client=BrokenClient())
    assert result['route_id'] == 'route_qwen3'
    assert result['status'] == 'ROUTE_UNAVAILABLE'
    assert result['model_id'] == 'Qwen/Qwen3-8B'
    assert result['substituted_model_id'] is None
