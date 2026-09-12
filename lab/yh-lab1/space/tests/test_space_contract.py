import importlib.util
from pathlib import Path

SPACE = Path('lab/yh-lab1/space')


def test_space_source_declares_required_tabs_and_mcp_read_tools():
    source = (SPACE / 'app.py').read_text()
    for tab in ['Overview','Eval Scoreboard','Synthetic Principals','Golden Cases','Hard Negatives','Blind Review','Error Taxonomy','Admission Gate']:
        assert tab in source
    for fn in ['get_eval_summary','get_case','compare_routes','get_admission_status']:
        assert f'def {fn}' in source
    assert 'mcp_server=True' in source


def test_space_read_tools_are_callable_without_network():
    spec = importlib.util.spec_from_file_location('yh_lab_space_app', SPACE / 'app.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    summary = module.get_eval_summary()
    assert summary['lab_id'] == 'YH-LAB1'
    assert summary['fixture_counts'] == {'golden':20,'hard_negative':20,'synthetic_principal':10}
    case = module.get_case('YH-HN-001')
    assert case['case_id'] == 'YH-HN-001'
    assert module.get_admission_status()['verdict'] in {'ADMIT','HOLD','FAIL'}
