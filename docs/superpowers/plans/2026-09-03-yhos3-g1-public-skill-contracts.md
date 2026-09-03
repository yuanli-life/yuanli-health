# YHOS3 G1 Public + Skill Contracts Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the public invocation/journey contracts and synthetic-qualified Skill projection required for the YHOS3 G1 Managed Gold Loop, without private runtime writes, source-ID migration, or real health data.

**Architecture:** `yuanli-life/yuanli-health` publishes the machine-readable Founder invocation and Managed Health Journey contract. `moonstachain/yuanli-health-skills` keeps the existing 16 source capability IDs and adds a YHOS3 product projection plus deterministic aliases/tests so the existing Experience capabilities can be invoked under the Health Office semantics. Real orchestration/ACT/OUT is explicitly deferred to the separately governed private-runtime child plan.

**Tech Stack:** JSON contracts, Python 3 standard library validation in public repo; Python 3 existing `router.py`, `suite_runner.py`, `full_suite.py`, unittest/pytest-compatible tests in Skill Core.

**Spec:** `docs/specs/2026-09-03-yhos3-sovereign-principal-health-office-design.md`

## Global Constraints

- Do not change the 16 `source_capability_id` values.
- Do not copy Skill implementation into `yuanli-life/yuanli-health`.
- Do not store real/re-identifiable health values in either repository fixture set.
- Public contracts may express route candidates, never clinical decisions or final health priority.
- `first-health-session`, `ninety-day-health-experiment`, `weekly-health-checkpoint`, `doctor-visit-prep`, `outcome-review`, `learning-reuse` remain the six Experience source capabilities.
- `outcome-review` and `learning-reuse` may share one product Journey label, but OUT and REUSE evidence gates remain independent.
- Every new fixture must be synthetic-only.
- This plan must not deploy private runtime or claim ACT/OUT/reuse in Reality.

---

### Task 1: Publish the YHOS3 Founder Invocation Contract

**Files:**
- Create: `yuanli-life/yuanli-health/invocation/yhos3-founder-invocation-v1.json`
- Create: `yuanli-life/yuanli-health/scripts/validate_yhos3_public_contracts.py`
- Create: `yuanli-life/yuanli-health/tests/test_yhos3_public_contracts.py`

**Interfaces:**
- Consumes: five Founder Intents from the accepted YHOS3 spec.
- Produces: JSON schema `yhos3-founder-invocation-v1` with stable machine intent IDs and source-experience route candidates.

- [ ] **Step 1: Write the failing public-contract test**

Create `tests/test_yhos3_public_contracts.py`:

```python
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class YHOS3PublicContractsTest(unittest.TestCase):
    def test_invocation_contract_has_exact_five_intents_and_no_health_priority(self):
        data = json.loads(
            (ROOT / "invocation" / "yhos3-founder-invocation-v1.json").read_text(encoding="utf-8")
        )
        self.assertEqual(data["schema"], "yhos3-founder-invocation-v1")
        self.assertEqual(
            set(data["intents"]),
            {"today_capacity", "key_moment", "body_signal", "life_disruption", "long_game"},
        )
        self.assertFalse(data["router_authority"]["may_decide_health_priority"])
        self.assertFalse(data["router_authority"]["may_create_clinical_authority"])
        self.assertEqual(data["privacy"]["repository_phi"], "forbidden")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the test and verify RED**

Run from `yuanli-life/yuanli-health`:

```bash
python3 -m unittest tests/test_yhos3_public_contracts.py -v
```

Expected: FAIL because `invocation/yhos3-founder-invocation-v1.json` does not exist.

- [ ] **Step 3: Create the minimal invocation contract**

Create `invocation/yhos3-founder-invocation-v1.json` with this exact shape:

```json
{
  "schema": "yhos3-founder-invocation-v1",
  "version": "1.0",
  "north_star": "health_optionality",
  "intents": {
    "today_capacity": {"mode": "performance_first", "route_candidate": "yuanli.health.experience.weekly-health-checkpoint"},
    "key_moment": {"mode": "performance_first", "route_candidate": "yuanli.health.experience.first-health-session"},
    "body_signal": {"mode": "healthspan_first", "route_candidate": "yuanli.health.experience.first-health-session"},
    "life_disruption": {"mode": "coupled", "route_candidate": "yuanli.health.experience.first-health-session"},
    "long_game": {"mode": "healthspan_first", "route_candidate": "yuanli.health.experience.first-health-session"}
  },
  "router_authority": {
    "may_select_route_candidate": true,
    "may_decide_health_priority": false,
    "may_create_clinical_authority": false,
    "may_activate_plan": false
  },
  "privacy": {"repository_phi": "forbidden"}
}
```

- [ ] **Step 4: Add a standard-library validator**

Create `scripts/validate_yhos3_public_contracts.py`:

```python
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "invocation" / "yhos3-founder-invocation-v1.json"
EXPECTED = {"today_capacity", "key_moment", "body_signal", "life_disruption", "long_game"}


def main() -> int:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    if data.get("schema") != "yhos3-founder-invocation-v1":
        raise SystemExit("invalid invocation schema")
    if set(data.get("intents", {})) != EXPECTED:
        raise SystemExit("invalid founder intent set")
    authority = data.get("router_authority", {})
    if authority.get("may_decide_health_priority") is not False:
        raise SystemExit("router may not decide health priority")
    if authority.get("may_create_clinical_authority") is not False:
        raise SystemExit("router may not create clinical authority")
    if data.get("privacy", {}).get("repository_phi") != "forbidden":
        raise SystemExit("public PHI must be forbidden")
    print("YHOS3 public invocation contract: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 5: Run validator and unit test**

```bash
python3 scripts/validate_yhos3_public_contracts.py
python3 -m unittest tests/test_yhos3_public_contracts.py -v
```

Expected: validator prints `PASS`; unittest reports `OK`.

- [ ] **Step 6: Commit**

```bash
git add invocation/yhos3-founder-invocation-v1.json scripts/validate_yhos3_public_contracts.py tests/test_yhos3_public_contracts.py
git commit -m "feat: add YHOS3 founder invocation contract"
```

---

### Task 2: Publish the Managed Health Journey Contract and Burden Ledger

**Files:**
- Create: `yuanli-life/yuanli-health/journeys/yhos3-managed-health-cycle-v1.json`
- Modify: `yuanli-life/yuanli-health/scripts/validate_yhos3_public_contracts.py`
- Modify: `yuanli-life/yuanli-health/tests/test_yhos3_public_contracts.py`

**Interfaces:**
- Consumes: route candidate from Task 1.
- Produces: a public state-machine contract for the G1 Journey plus explicit `management_burden` fields.

- [ ] **Step 1: Add a failing state-machine test**

Append:

```python
    def test_managed_cycle_preserves_reality_boundaries_and_burden_fields(self):
        data = json.loads(
            (ROOT / "journeys" / "yhos3-managed-health-cycle-v1.json").read_text(encoding="utf-8")
        )
        self.assertEqual(data["schema"], "yhos3-managed-health-cycle-v1")
        self.assertEqual(
            data["reality_spine"],
            ["CTX", "EVD", "DEC", "WPK", "ACT", "OUT", "LRN", "REUSE"],
        )
        self.assertEqual(set(data["terminal_states"]), {"WAIT", "ESCALATE", "BLOCKED", "SETTLED"})
        self.assertEqual(
            set(data["management_burden_fields"]),
            {
                "principal_manual_action_count",
                "principal_decision_count",
                "principal_time_minutes",
                "attention_interruptions",
                "office_handled_steps"
            },
        )
        self.assertFalse(data["claims"]["plan_is_act"])
        self.assertFalse(data["claims"]["act_is_outcome"])
        self.assertFalse(data["claims"]["outcome_is_attribution"])
```

- [ ] **Step 2: Verify RED**

```bash
python3 -m unittest tests/test_yhos3_public_contracts.py -v
```

Expected: FAIL because Journey contract does not exist.

- [ ] **Step 3: Create the Journey contract**

Create `journeys/yhos3-managed-health-cycle-v1.json`:

```json
{
  "schema": "yhos3-managed-health-cycle-v1",
  "version": "1.0",
  "reality_spine": ["CTX", "EVD", "DEC", "WPK", "ACT", "OUT", "LRN", "REUSE"],
  "g1_required_through": "OUT",
  "terminal_states": ["WAIT", "ESCALATE", "BLOCKED", "SETTLED"],
  "experience_sources": [
    "yuanli.health.experience.first-health-session",
    "yuanli.health.experience.ninety-day-health-experiment",
    "yuanli.health.experience.weekly-health-checkpoint",
    "yuanli.health.experience.doctor-visit-prep",
    "yuanli.health.experience.outcome-review",
    "yuanli.health.experience.learning-reuse"
  ],
  "management_burden_fields": [
    "principal_manual_action_count",
    "principal_decision_count",
    "principal_time_minutes",
    "attention_interruptions",
    "office_handled_steps"
  ],
  "claims": {
    "plan_is_act": false,
    "act_is_outcome": false,
    "outcome_is_attribution": false,
    "learning_is_reuse": false,
    "g1_requires_compounding": false
  },
  "privacy": {"repository_phi": "forbidden"}
}
```

- [ ] **Step 4: Extend validator for the Journey contract**

Add a `validate_journey()` function that checks the exact reality spine, terminal states, burden-field set, false claim booleans, and PHI prohibition; call it from `main()` after invocation validation.

- [ ] **Step 5: Run tests**

```bash
python3 scripts/validate_yhos3_public_contracts.py
python3 -m unittest tests/test_yhos3_public_contracts.py -v
```

Expected: PASS / OK.

- [ ] **Step 6: Commit**

```bash
git add journeys/yhos3-managed-health-cycle-v1.json scripts/validate_yhos3_public_contracts.py tests/test_yhos3_public_contracts.py
git commit -m "feat: define YHOS3 managed health journey"
```

---

### Task 3: Add the YHOS3 Product Projection in Skill Core Without Source-ID Migration

**Files:**
- Create: `moonstachain/yuanli-health-skills/registry/yhos3-product-projection.json`
- Modify: `moonstachain/yuanli-health-skills/src/yuanli_health_skills/router.py`
- Modify: `moonstachain/yuanli-health-skills/tests/test_full_router.py`

**Interfaces:**
- Consumes: stable route tokens from the public contract/Journey semantics.
- Produces: deterministic product aliases mapping to existing source capability IDs; no health-priority decision.

- [ ] **Step 1: Add failing router tests**

Add tests equivalent to:

```python
def test_yhos3_product_aliases_route_to_existing_source_ids():
    available = list(CAPABILITIES)
    expected = {
        "health_office_intake": "yuanli.health.experience.first-health-session",
        "managed_health_cycle": "yuanli.health.experience.ninety-day-health-experiment",
        "low_burden_checkpoint": "yuanli.health.experience.weekly-health-checkpoint",
        "clinical_collaboration": "yuanli.health.experience.doctor-visit-prep",
        "settlement": "yuanli.health.experience.outcome-review",
        "reuse": "yuanli.health.experience.learning-reuse",
    }
    for jtbd, source_id in expected.items():
        route = route_jtbd(jtbd, available, decision_candidate_id="SYN-DEC" if jtbd == "managed_health_cycle" else None)
        assert route["source_capability_id"] == source_id
        assert route["health_priority_decided"] is False
```

Also add a test proving unsupported prose does not silently route:

```python
def test_router_does_not_guess_unregistered_natural_language():
    route = route_jtbd("我最近状态不太好你替我决定吃什么药", list(CAPABILITIES))
    assert route["route_state"] == "no_route"
    assert route["health_priority_decided"] is False
```

- [ ] **Step 2: Run router tests and verify RED**

```bash
pytest tests/test_full_router.py -q
```

Expected: new alias test fails with `UNSUPPORTED_JTBD`.

- [ ] **Step 3: Add explicit YHOS3 aliases to `router.py`**

Extend `_EXPERIENCE_ROUTES` only with:

```python
    "health_office_intake": "yuanli.health.experience.first-health-session",
    "managed_health_cycle": "yuanli.health.experience.ninety-day-health-experiment",
    "low_burden_checkpoint": "yuanli.health.experience.weekly-health-checkpoint",
    "clinical_collaboration": "yuanli.health.experience.doctor-visit-prep",
    "settlement": "yuanli.health.experience.outcome-review",
    "reuse": "yuanli.health.experience.learning-reuse",
```

Do not add fuzzy NLP classification inside Skill Core.

For `managed_health_cycle`, reuse the existing rule that a supplied `decision_candidate_id` is required before routing to the experiment source; otherwise route to `first-health-session` rather than fabricating DEC.

- [ ] **Step 4: Create product projection registry**

Create `registry/yhos3-product-projection.json`:

```json
{
  "schema": "yhos3-product-projection-v1",
  "source_suite_id": "YL-SUITE-HEALTH-20260823-0001",
  "source_id_migration": false,
  "gold_experience_projection": {
    "health_office_intake": "yuanli.health.experience.first-health-session",
    "managed_health_cycle": "yuanli.health.experience.ninety-day-health-experiment",
    "low_burden_checkpoint": "yuanli.health.experience.weekly-health-checkpoint",
    "clinical_collaboration": "yuanli.health.experience.doctor-visit-prep",
    "settlement": "yuanli.health.experience.outcome-review",
    "reuse": "yuanli.health.experience.learning-reuse"
  },
  "meta_front_door": false,
  "claims": {"released": false, "clinically_validated": false, "runtime_observed": false}
}
```

- [ ] **Step 5: Run focused and full tests**

```bash
pytest tests/test_full_router.py -q
pytest tests/test_full_suite.py tests/test_full_suite_cases.py tests/test_abi.py -q
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_capabilities.py
```

Expected: zero failures and validator exit 0.

- [ ] **Step 6: Commit**

```bash
git add registry/yhos3-product-projection.json src/yuanli_health_skills/router.py tests/test_full_router.py
git commit -m "feat: project YHOS3 health office routes"
```

---

### Task 4: Preregister Synthetic G1 Managed-Loop Shadow Cases

**Files:**
- Create: `moonstachain/yuanli-health-skills/fixtures/yhos3-g1/managed-gold-loop-cases.json`
- Create: `moonstachain/yuanli-health-skills/tests/test_yhos3_g1_shadow.py`

**Interfaces:**
- Consumes: existing `run_full_suite()` and YHOS3 route aliases.
- Produces: synthetic evidence that the public/product semantics preserve authority and reality boundaries before any private Runtime work.

- [ ] **Step 1: Write failing Shadow tests**

Create tests covering at minimum these synthetic cases:

```text
G1-S01 intake with incomplete evidence -> decision candidate only; no WPK/ACT
G1-S02 managed cycle with valid DEC -> WPK/ACT candidates, runtime_observed=false
G1-S03 clinical request through non-clinical route -> RED / CLINICAL_ESCALATION_REQUIRED
G1-S04 doctor-visit prep clinical handoff -> allowed candidate with clinician guardrail
G1-S05 outcome review without ACT -> fail prerequisite
G1-S06 outcome review with ACT + observation -> OUT candidate, no attribution claim
G1-S07 reuse with identical preload/use receipt -> INDEPENDENT_RECEIPTS_REQUIRED
G1-S08 repository PHI / non-synthetic fixture -> rejected by existing suite rules
```

Implement fixtures with only `SYN-*` opaque values. Do not include realistic names, labs, dates of birth, addresses, medical record numbers, or actual health values.

- [ ] **Step 2: Run test and verify RED**

```bash
pytest tests/test_yhos3_g1_shadow.py -q
```

Expected: FAIL because fixture file/test support is not present.

- [ ] **Step 3: Add the synthetic fixture bank**

Use existing `full-suite-synthetic-case-v1` shape and valid `SYN-FS-###` case IDs where routed through `run_full_suite()`. Keep new YHOS3 case labels in `coverage_tags`, not by changing existing case schema.

- [ ] **Step 4: Implement tests by calling existing runners, not a new framework**

Use:

```python
from yuanli_health_skills.full_suite import process_full_suite_case
from yuanli_health_skills.suite_runner import run_full_suite
```

Assert exact authority/reality properties, including:

```python
assert result["canonical_write"] is False
assert result["persistence"] == "none"
assert result["runtime_observed"] is False
assert result["health_outcome_claimed"] is False
assert result["clinical_effectiveness_claimed"] is False
```

- [ ] **Step 5: Run focused and repository tests**

```bash
pytest tests/test_yhos3_g1_shadow.py -q
pytest tests -q
PYTHONDONTWRITEBYTECODE=1 python3 scripts/generate_codex_adapter.py --check
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_codex_adapter.py --check-repository
PYTHONDONTWRITEBYTECODE=1 python3 scripts/scan_public_content.py --check-current --check-history
```

Expected: zero failures; generated adapter byte-exact; public content/history scan clean.

- [ ] **Step 6: Commit**

```bash
git add fixtures/yhos3-g1/managed-gold-loop-cases.json tests/test_yhos3_g1_shadow.py
git commit -m "test: preregister YHOS3 G1 synthetic shadow"
```

---

### Task 5: Freeze the G1 Evaluation Contract in the Public Front Door

**Files:**
- Create: `yuanli-life/yuanli-health/evaluation/YHOS3-G1-MANAGED-GOLD-LOOP-v0.1.md`
- Modify: `yuanli-life/yuanli-health/tests/test_yhos3_public_contracts.py`

**Interfaces:**
- Consumes: Tasks 1-4 public and synthetic contracts.
- Produces: non-compensatory PASS/FAIL criteria for later G1C private Reality work.

- [ ] **Step 1: Add a failing presence/required-terms test**

```python
    def test_g1_evaluation_contract_is_preregistered(self):
        text = (ROOT / "evaluation" / "YHOS3-G1-MANAGED-GOLD-LOOP-v0.1.md").read_text(encoding="utf-8")
        for token in (
            "verified ACT",
            "observed OUT",
            "Principal management burden",
            "WAIT",
            "ESCALATE",
            "ACT ≠ OUT",
            "no compounding claim"
        ):
            self.assertIn(token, text)
```

- [ ] **Step 2: Verify RED**

```bash
python3 -m unittest tests/test_yhos3_public_contracts.py -v
```

Expected: FAIL because evaluation contract is absent.

- [ ] **Step 3: Write evaluation contract**

The document must freeze:

- mother claim from the Program plan;
- exact G1 required fields;
- hard authority/privacy gates;
- `PASS / FAIL / INCONCLUSIVE / BLOCKED / NOT_OBSERVED` terminal vocabulary;
- management burden dimensions;
- no outcome or compounding claim from synthetic qualification;
- real G1C run must be private and Human-authorized.

- [ ] **Step 4: Run public tests and validator**

```bash
python3 scripts/validate_yhos3_public_contracts.py
python3 -m unittest tests/test_yhos3_public_contracts.py -v
```

Expected: PASS / OK.

- [ ] **Step 5: Commit**

```bash
git add evaluation/YHOS3-G1-MANAGED-GOLD-LOOP-v0.1.md tests/test_yhos3_public_contracts.py
git commit -m "docs: preregister YHOS3 G1 managed gold loop"
```

---

### Task 6: Independent Verification and G1C Handoff

**Files:**
- No production file changes.
- Produce PR/CI evidence only.

**Interfaces:**
- Consumes: all prior tasks.
- Produces: a verified public+Skill contract package ready for a separately authorized private-runtime child plan.

- [ ] **Step 1: Run full public verification**

From `yuanli-life/yuanli-health`:

```bash
python3 scripts/validate_yhos3_public_contracts.py
python3 -m unittest discover -s tests -v
```

Expected: zero failures.

- [ ] **Step 2: Run full Skill Core verification**

From `moonstachain/yuanli-health-skills`:

```bash
pytest tests -q
PYTHONDONTWRITEBYTECODE=1 python3 scripts/generate_codex_adapter.py --check
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_codex_adapter.py --check-repository
PYTHONDONTWRITEBYTECODE=1 python3 scripts/scan_public_content.py --check-current --check-history
```

Expected: zero failures and all check commands exit 0.

- [ ] **Step 3: Verify no source capability identity drift**

```bash
git diff main -- registry/source-capabilities.json capabilities/
```

Expected: no source-ID migration and no accidental contract mutation outside explicitly planned files.

- [ ] **Step 4: Verify synthetic-only scope**

Search newly changed files for prohibited realistic/private data patterns according to the existing public content scanner; any hit is a hard FAIL until adjudicated.

- [ ] **Step 5: Create separate Draft PRs**

Create one governed PR per repository. Do not combine repositories into one evidence claim.

Public PR title:

`YHOS3-G1A｜Founder Invocation + Managed Journey Contract`

Skill PR title:

`YHOS3-G1B｜Gold Skill Projection + Synthetic Shadow`

Both PR bodies must state:

`SYNTHETIC / CONTRACT QUALIFICATION ONLY — NO PRIVATE RUNTIME, ACT, OUTCOME, CLINICAL EFFECTIVENESS, OR COMPOUNDING CLAIM.`

- [ ] **Step 6: Stop before G1C runtime work**

Do not implement or deploy `yuanli-health-apple` runtime yet. First perform a fresh private-runtime source audit and obtain a new exact-path authority, because the prior FHP2 M0 forward authorization expired on 2026-09-02 and the previously named Concierge source file is not currently present on `main`.

- [ ] **Step 7: Commit any final plan-only metadata if needed**

If no file changed in this verification task, do not create an empty commit.

---

## Self-Review Checklist

- Spec coverage: this child plan covers Public Invocation, Managed Journey, existing 16-Skill projection, Gold Experience priority, synthetic Shadow, and G1 evaluation preregistration.
- Deliberate gap: private Runtime implementation is not guessed; it is a separate G1C plan after fresh source/authority re-anchor.
- No placeholders: all Task 1-4 code/contract shapes and commands are explicit.
- Type/name consistency: stable source IDs match the current `registry/source-capabilities.json`; route alias names match across public and Skill plan sections.
- Scope discipline: no new top-level ontology, database, fuzzy NLP router, runtime persistence, or clinical authority is introduced.
