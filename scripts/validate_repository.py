#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

REQUIRED_FILES = [
    "constitution/YHOS-F0.1.md",
    "constitution/upstream-authority.yaml",
    "systems/dual-system-registry.yaml",
    "ontology/registry.yaml",
    "intents/registry.yaml",
    "routing/dual-system-router.yaml",
    "AGENTS.md",
    "evaluations/golden-journeys.yaml",
]

CAPABILITIES = ["recover", "adapt", "energize", "move", "think", "connect"]
INTENTS = ["today_capacity", "key_moment", "body_signal", "life_disruption", "long_game"]
MODES = ["performance_first", "healthspan_first", "coupled"]
GOLDEN_JOURNEYS = [f"GJ0{i}_" for i in range(1, 9)]


def read(root: Path, rel: str) -> str:
    return (root / rel).read_text(encoding="utf-8")


def require(text: str, token: str, where: str, errors: list[str]) -> None:
    if token not in text:
        errors.append(f"{where}: missing required token {token!r}")


def validate_repository(root: Path) -> list[str]:
    root = Path(root)
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            errors.append(f"missing required file: {rel}")
    if errors:
        return errors

    constitution = read(root, "constitution/YHOS-F0.1.md")
    systems = read(root, "systems/dual-system-registry.yaml")
    ontology = read(root, "ontology/registry.yaml")
    intents = read(root, "intents/registry.yaml")
    router = read(root, "routing/dual-system-router.yaml")
    agents = read(root, "AGENTS.md")
    journeys = read(root, "evaluations/golden-journeys.yaml")

    for token in [
        "status: proposed",
        "One Kernel × Two Engines × One Learning System",
        "Performance cannot override Healthspan safety",
        "Public Law × Private Reality",
        "FIRST_CROSS_SYSTEM_HEALTH_REUSE",
    ]:
        require(constitution, token, "constitution/YHOS-F0.1.md", errors)

    require(systems, "architecture: one_kernel_two_engines_one_learning_system", "systems/dual-system-registry.yaml", errors)
    require(systems, "id: performance", "systems/dual-system-registry.yaml", errors)
    require(systems, "id: healthspan", "systems/dual-system-registry.yaml", errors)
    require(systems, "id: one_reality_learning_system", "systems/dual-system-registry.yaml", errors)

    for capability in CAPABILITIES:
        require(ontology, f"id: {capability}", "ontology/registry.yaml", errors)
    require(ontology, "expected_count: 12", "ontology/registry.yaml", errors)
    require(ontology, "expected_count: 4", "ontology/registry.yaml", errors)
    require(ontology, "expected_count: 5", "ontology/registry.yaml", errors)
    require(ontology, "upstream_exact_id_import_pending", "ontology/registry.yaml", errors)

    for intent in INTENTS:
        require(intents, f"id: {intent}", "intents/registry.yaml", errors)
    for mode in MODES:
        require(router, f"{mode}:", "routing/dual-system-router.yaml", errors)

    for token in [
        "performance_cannot_override_healthspan_safety: true",
        "ai_cannot_override_clinical_authority: true",
        "short_clock_cannot_overwrite_long_clock: true",
        "allow_no_action: true",
    ]:
        require(router, token, "routing/dual-system-router.yaml", errors)

    require(agents, "Founder Intents are invocation vocabulary, not ontology.", "AGENTS.md", errors)
    require(agents, "Fail closed", "AGENTS.md", errors)

    for prefix in GOLDEN_JOURNEYS:
        if prefix not in journeys:
            errors.append(f"evaluations/golden-journeys.yaml: missing preregistered journey prefix {prefix}")
    require(journeys, "GJ09_first_cross_system_reuse", "evaluations/golden-journeys.yaml", errors)
    require(journeys, "future_reality_gate_not_synthetic_claim", "evaluations/golden-journeys.yaml", errors)

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_repository(root)
    if errors:
        print("F0.1 STRUCTURAL VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("F0.1 STRUCTURAL VALIDATION: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
