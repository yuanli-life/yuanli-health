from pathlib import Path
import importlib.util
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load_script(name: str):
    path = ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RepositoryContractTests(unittest.TestCase):
    def test_required_f01_assets_exist(self):
        required = [
            "constitution/YHOS-F0.1.md",
            "constitution/upstream-authority.yaml",
            "systems/dual-system-registry.yaml",
            "ontology/registry.yaml",
            "intents/registry.yaml",
            "routing/dual-system-router.yaml",
            "AGENTS.md",
            "evaluations/golden-journeys.yaml",
        ]
        missing = [p for p in required if not (ROOT / p).is_file()]
        self.assertEqual(missing, [])

    def test_structural_validator_passes_candidate(self):
        validator = load_script("validate_repository")
        errors = validator.validate_repository(ROOT)
        self.assertEqual(errors, [])

    def test_public_privacy_scanner_passes_candidate(self):
        scanner = load_script("scan_public_content")
        findings = scanner.scan_repository(ROOT)
        self.assertEqual(findings, [])


if __name__ == "__main__":
    unittest.main()
