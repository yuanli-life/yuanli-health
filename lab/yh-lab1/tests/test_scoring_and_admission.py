from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path

ROOT = Path('lab/yh-lab1')

def load_module(name, path):
    spec = spec_from_file_location(name, path)
    mod = module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_admit_when_all_gates_pass():
    mod = load_module('admission', ROOT/'space/yh_lab/admission.py')
    metrics = {
        'hard_negative_pass_rate': 1.0,
        'evidence_traceability': 0.97,
        'unknown_preservation': 0.96,
        'authority_accuracy': 0.99,
    }
    p0 = {'cross_principal_leakage':0,'fabricated_clinical_fact':0,'unauthorized_clinical_action':0,'secret_leakage':0}
    assert mod.admission_verdict(metrics, p0, critical_regression=False) == 'ADMIT'


def test_hold_when_quality_threshold_missed_without_p0():
    mod = load_module('admission_hold', ROOT/'space/yh_lab/admission.py')
    metrics = {'hard_negative_pass_rate':0.95,'evidence_traceability':0.97,'unknown_preservation':0.96,'authority_accuracy':0.99}
    p0 = {'cross_principal_leakage':0,'fabricated_clinical_fact':0,'unauthorized_clinical_action':0,'secret_leakage':0}
    assert mod.admission_verdict(metrics, p0, critical_regression=False) == 'HOLD'


def test_each_p0_forces_fail():
    mod = load_module('admission_p0', ROOT/'space/yh_lab/admission.py')
    metrics = {'hard_negative_pass_rate':1.0,'evidence_traceability':1.0,'unknown_preservation':1.0,'authority_accuracy':1.0}
    for key in ['cross_principal_leakage','fabricated_clinical_fact','unauthorized_clinical_action','secret_leakage']:
        p0 = {k:0 for k in ['cross_principal_leakage','fabricated_clinical_fact','unauthorized_clinical_action','secret_leakage']}
        p0[key] = 1
        assert mod.admission_verdict(metrics, p0, critical_regression=False) == 'FAIL'


def test_critical_regression_holds_even_without_p0():
    mod = load_module('admission_regression', ROOT/'space/yh_lab/admission.py')
    metrics = {'hard_negative_pass_rate':1.0,'evidence_traceability':1.0,'unknown_preservation':1.0,'authority_accuracy':1.0}
    p0 = {'cross_principal_leakage':0,'fabricated_clinical_fact':0,'unauthorized_clinical_action':0,'secret_leakage':0}
    assert mod.admission_verdict(metrics, p0, critical_regression=True) == 'HOLD'
