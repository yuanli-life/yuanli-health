# YH-STRAT2-G0 Repeatable Principal Health Office Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the minimum repeatable `YH-MANAGED-0.1.0` Product Kernel that can run one Sleep Recovery Health Case for Principal #000 and later admit Principal #001/#002 without customer-specific code, tables, workflows, prompts, or agents.

**Architecture:** GitHub remains Product/Law Canon; Supabase/PostgreSQL stores multi-Principal operational state; a small Python Product Kernel implements the Health Case state machine and Blueprint contract; a replaceable intelligence interface returns structured candidate reasoning; a simple worker advances due Cases; Principal/Steward web surfaces are projections from the same Product Kernel. Existing Local Health Kernel remains raw health Reality Canon and is referenced through minimized `EvidenceRef` records rather than copied into the new product state by default.

**Tech Stack:** Python 3.11+, Pydantic v2, pytest, Supabase/PostgreSQL + RLS, Next.js/TypeScript for MVP surfaces, OpenAI behind a typed adapter, GitHub for release/Blueprint/schema Canon.

**Spec:** `docs/superpowers/specs/2026-09-11-yh-strat2-g0-repeatable-principal-health-office-design.md`

## Global Constraints

- Product release is exactly `YH-MANAGED-0.1.0`.
- Initial Blueprint is exactly `BP-SLEEP-001` version `1.0.0`.
- Product proof is `One Product × Three Principals × Zero Fork`.
- Product Kernel must contain no Principal-specific branching such as `if principal == "Ray"`.
- MVP autonomous action boundary is `READ + PREPARE`; `COMMIT`, autonomous `CLINICAL`, and `DESTRUCTIVE` are not admitted.
- Health Steward is a first-class product role.
- Local Health Kernel remains raw health Reality Canon; new product tables store references/minimized operational projections, not a second raw PHI canon.
- Supabase is operational Product State, not Health Canon or Product Law.
- GitHub is Product/Law Canon for ProductRelease, Blueprint, schemas, policies, tests, and release manifests.
- OpenAI/ChatGPT is replaceable intelligence and may propose candidate reasoning only.
- No Temporal, Cedar, Kafka, Kubernetes, microservice split, independent vector DB, multi-agent swarm, custom model training, or native iOS/Watch rebuild before Principal #003.
- No runtime/database deployment to production is implied by this plan; promotion requires fresh verification and explicit Human Gate.
- Every Principal-scoped record must resolve to `principal_id`; every Case-scoped record must resolve to `case_id`.
- Existing in-flight Cases may not silently inherit a new ProductRelease or Blueprint version.

---

## Scope Decomposition

This spec spans four independent proof stages. To avoid a monolithic implementation, this plan implements only the **G0 Product Foundation + G1 Golden Tenant foundation** needed to run Principal #000 on the standard product. G2 Config-only Replication, G3 Zero-Engineer-Touch onboarding, and G4 N5 Paid will each receive a follow-up implementation plan after the prior gate produces Reality evidence.

This plan ends when the repository contains a testable Product Kernel, multi-Principal schema, Sleep Blueprint, deterministic worker path, typed intelligence boundary, minimal Principal/Steward projections, and a Golden Tenant bootstrap that can create Principal #000 and a Sleep Case with zero Ray-specific code.

---

## File Map

### Product Canon
- Create: `product/releases/YH-MANAGED-0.1.0.yaml` — immutable release manifest.
- Create: `product/blueprints/BP-SLEEP-001.v1.yaml` — Sleep Recovery Blueprint.
- Create: `product/policies/authority-v1.yaml` — MVP role/action policy for READ/PREPARE.

### Product Schemas
- Create: `schemas/product-release.schema.json`
- Create: `schemas/blueprint.schema.json`
- Create: `schemas/principal.schema.json`
- Create: `schemas/health-case.schema.json`
- Create: `schemas/evidence-ref.schema.json`
- Create: `schemas/health-thesis.schema.json`
- Create: `schemas/battle.schema.json`
- Create: `schemas/action.schema.json`
- Create: `schemas/outcome.schema.json`
- Create: `schemas/learning.schema.json`

### Python Product Kernel
- Create: `src/yuanli_health/domain/models.py` — Pydantic domain models.
- Create: `src/yuanli_health/domain/case_engine.py` — allowed states/transitions and invariants.
- Create: `src/yuanli_health/domain/blueprint.py` — Blueprint loading/validation.
- Create: `src/yuanli_health/domain/authority.py` — READ/PREPARE authority evaluation.
- Create: `src/yuanli_health/services/intelligence.py` — typed intelligence protocol and deterministic test provider.
- Create: `src/yuanli_health/services/case_service.py` — use-cases that assemble Product Kernel operations.
- Create: `src/yuanli_health/worker/runner.py` — due-case processing loop.

### Supabase
- Create: `supabase/migrations/20260911_yh_managed_001_core.sql` — multi-Principal operational tables, constraints, indexes, RLS enablement.
- Create: `supabase/migrations/20260911_yh_managed_002_rls.sql` — explicit Principal/Steward RLS policies.
- Create: `src/yuanli_health/repositories/supabase_repository.py` — DB adapter behind repository interface.

### Web Surfaces
- Create: `apps/web/app/principal/page.tsx` — Today/Decision Cockpit projection.
- Create: `apps/web/app/principal/cases/page.tsx` — Cases projection.
- Create: `apps/web/app/steward/page.tsx` — Steward Cockpit projection.
- Create: `apps/web/lib/types.ts` — frontend projection types only.

### Tests / Fixtures
- Create: `tests/test_product_release.py`
- Create: `tests/test_blueprint_contract.py`
- Create: `tests/test_case_engine.py`
- Create: `tests/test_authority.py`
- Create: `tests/test_principal_isolation.py`
- Create: `tests/test_intelligence_contract.py`
- Create: `tests/test_worker.py`
- Create: `tests/test_zero_fork_guard.py`
- Create: `tests/fixtures/principal-000.json`
- Create: `tests/fixtures/sleep-case-0001.json`
- Create: `tests/fixtures/evidence-minimal.json`
- Create: `tests/acceptance/test_g1_golden_tenant_bootstrap.py`

---

### Task 1: Freeze `YH-MANAGED-0.1.0` Release + Sleep Blueprint Canon

**Files:**
- Create: `product/releases/YH-MANAGED-0.1.0.yaml`
- Create: `product/blueprints/BP-SLEEP-001.v1.yaml`
- Create: `product/policies/authority-v1.yaml`
- Create: `schemas/product-release.schema.json`
- Create: `schemas/blueprint.schema.json`
- Test: `tests/test_product_release.py`
- Test: `tests/test_blueprint_contract.py`

**Interfaces:**
- Produces: immutable product manifest with fields `product_release_id`, `blueprints`, `case_schema_version`, `authority_policy_version`, `intelligence_route_version`, `allowed_action_classes`.
- Produces: `BP-SLEEP-001` Blueprint with eligibility, evidence requirements, thesis sufficiency, action classes, authority boundaries, observation windows, settlement vocabulary, learning/reuse rules.
- Consumed by: Tasks 2–8.

- [ ] **Step 1: Write failing release-manifest test**

```python
from pathlib import Path
import yaml


def test_release_is_exact_mvp_contract():
    release = yaml.safe_load(Path("product/releases/YH-MANAGED-0.1.0.yaml").read_text())
    assert release["product_release_id"] == "YH-MANAGED-0.1.0"
    assert release["blueprints"] == [{"id": "BP-SLEEP-001", "version": "1.0.0"}]
    assert release["allowed_action_classes"] == ["READ", "PREPARE"]
    assert release["case_schema_version"] == "health-case-v1"
```

- [ ] **Step 2: Run test and verify RED**

Run: `pytest tests/test_product_release.py -v`
Expected: FAIL because the release file does not exist.

- [ ] **Step 3: Create release manifest and JSON Schema**

Release manifest must contain no infrastructure-specific workflow IDs and must pin all versions required by the spec.

- [ ] **Step 4: Write failing Blueprint contract test**

```python

def test_sleep_blueprint_has_no_principal_specific_fields(blueprint):
    encoded = str(blueprint).lower()
    assert "ray" not in encoded
    assert "principal_id" not in blueprint.get("defaults", {})
    assert blueprint["id"] == "BP-SLEEP-001"
    assert blueprint["version"] == "1.0.0"
    assert set(blueprint["allowed_action_classes"]) == {"READ", "PREPARE"}
    assert set(blueprint["outcome_states"]) == {
        "supported", "unsupported", "mixed", "inconclusive", "not_observed", "refuted"
    }
```

- [ ] **Step 5: Create Blueprint + authority policy and make tests GREEN**

Run: `pytest tests/test_product_release.py tests/test_blueprint_contract.py -v`
Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add product schemas tests/test_product_release.py tests/test_blueprint_contract.py
git commit -m "feat(yh-managed): freeze release and sleep blueprint"
```

---

### Task 2: Implement Canonical Product Domain Models

**Files:**
- Create: `schemas/principal.schema.json`
- Create: `schemas/health-case.schema.json`
- Create: `schemas/evidence-ref.schema.json`
- Create: `schemas/health-thesis.schema.json`
- Create: `schemas/battle.schema.json`
- Create: `schemas/action.schema.json`
- Create: `schemas/outcome.schema.json`
- Create: `schemas/learning.schema.json`
- Create: `src/yuanli_health/domain/models.py`
- Test: `tests/test_case_engine.py`

**Interfaces:**
- Produces Pydantic models: `Principal`, `ProductReleaseRef`, `BlueprintRef`, `HealthCase`, `EvidenceRef`, `HealthThesis`, `Battle`, `Action`, `Outcome`, `Learning`.
- `HealthCase` fields must include `case_id`, `principal_id`, `product_release_id`, `blueprint_id`, `blueprint_version`, `state`, `owner_role`, `next_step`, `created_at`, `updated_at`.
- Consumed by Tasks 3–8.

- [ ] **Step 1: Write failing model validation tests**

```python
import pytest
from pydantic import ValidationError
from yuanli_health.domain.models import HealthCase


def test_case_requires_explicit_principal_and_release():
    with pytest.raises(ValidationError):
        HealthCase(case_id="CASE-1", state="NEW")
```

- [ ] **Step 2: Run RED**

Run: `pytest tests/test_case_engine.py::test_case_requires_explicit_principal_and_release -v`
Expected: FAIL/ImportError because models are not implemented.

- [ ] **Step 3: Implement minimal Pydantic models**

Use string IDs, explicit enums for Case state and Outcome settlement, and no implicit current Principal global.

- [ ] **Step 4: Add JSON Schema parity test**

Assert required identifiers are required by both Pydantic and the checked-in JSON Schemas.

- [ ] **Step 5: Run GREEN**

Run: `pytest tests/test_case_engine.py -v`
Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add schemas src/yuanli_health/domain/models.py tests/test_case_engine.py
git commit -m "feat(yh-managed): add canonical product domain models"
```

---

### Task 3: Implement One Health Case Engine

**Files:**
- Create: `src/yuanli_health/domain/case_engine.py`
- Modify: `tests/test_case_engine.py`

**Interfaces:**
- Produces: `transition_case(case: HealthCase, target: CaseState, *, reason: str, actor_role: str) -> HealthCase`.
- Produces: `allowed_transitions(state: CaseState) -> set[CaseState]`.
- State set: `NEW, UNDERSTANDING, PRIORITIZED, ACTIVE, WAITING, OBSERVING, LEARNING, CLOSED, BLOCKED, ESCALATED, CANCELLED`.
- Consumed by Task 6 and Task 8.

- [ ] **Step 1: Write transition-table tests**

```python

def test_active_can_wait_or_observe_or_block_or_escalate(case_active):
    assert allowed_transitions(case_active.state) == {
        CaseState.WAITING,
        CaseState.OBSERVING,
        CaseState.BLOCKED,
        CaseState.ESCALATED,
        CaseState.CANCELLED,
    }
```

Also test that `NEW → CLOSED`, `UNDERSTANDING → ACTIVE`, and `WAITING → LEARNING` are rejected unless explicitly allowed by the canonical table.

- [ ] **Step 2: Run RED**

Run: `pytest tests/test_case_engine.py -v`
Expected: FAIL because transition engine is missing.

- [ ] **Step 3: Implement explicit transition table and immutable audit metadata**

Every transition must update `updated_at` and preserve `principal_id`, release, Blueprint version, and Case ID.

- [ ] **Step 4: Add invariant tests**

Test that transition logic cannot change `principal_id`, `product_release_id`, or `blueprint_version`.

- [ ] **Step 5: Run GREEN**

Run: `pytest tests/test_case_engine.py -v`
Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add src/yuanli_health/domain/case_engine.py tests/test_case_engine.py
git commit -m "feat(yh-managed): add single health case engine"
```

---

### Task 4: Implement MVP Authority Gate

**Files:**
- Create: `src/yuanli_health/domain/authority.py`
- Test: `tests/test_authority.py`

**Interfaces:**
- Produces: `evaluate_action(action_class: str, *, actor_role: str, principal_approved: bool, steward_approved: bool) -> AuthorityDecision`.
- `AuthorityDecision` contains `allowed: bool`, `reason: str`, `requires_human: bool`.
- MVP allows automated execution only for admitted `READ` and `PREPARE`; PREPARE requires Steward ownership where Blueprint requires it.
- `COMMIT`, autonomous `CLINICAL`, and `DESTRUCTIVE` always fail closed in `YH-MANAGED-0.1.0`.

- [ ] **Step 1: Write hard-negative tests**

```python
import pytest

@pytest.mark.parametrize("action_class", ["COMMIT", "CLINICAL", "DESTRUCTIVE"])
def test_non_mvp_action_classes_fail_closed(action_class):
    decision = evaluate_action(
        action_class,
        actor_role="ai_health_brain",
        principal_approved=True,
        steward_approved=True,
    )
    assert decision.allowed is False
```

- [ ] **Step 2: Run RED**

Run: `pytest tests/test_authority.py -v`
Expected: FAIL because authority module is missing.

- [ ] **Step 3: Implement minimal authority evaluator**

Do not introduce Cedar or a policy engine; load `authority-v1.yaml` and evaluate deterministically.

- [ ] **Step 4: Add READ/PREPARE positive tests and clinician boundary tests**

- [ ] **Step 5: Run GREEN**

Run: `pytest tests/test_authority.py -v`
Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add src/yuanli_health/domain/authority.py tests/test_authority.py product/policies/authority-v1.yaml
git commit -m "feat(yh-managed): enforce mvp authority boundary"
```

---

### Task 5: Create Multi-Principal Supabase Operational Schema + RLS

**Files:**
- Create: `supabase/migrations/20260911_yh_managed_001_core.sql`
- Create: `supabase/migrations/20260911_yh_managed_002_rls.sql`
- Create: `tests/test_principal_isolation.py`

**Interfaces:**
- Produces tables: `yh_principals`, `yh_product_releases`, `yh_health_cases`, `yh_evidence_refs`, `yh_health_theses`, `yh_battles`, `yh_actions`, `yh_outcomes`, `yh_learnings`, `yh_domain_events`.
- Every operational child table contains explicit `principal_id`; every Case child contains explicit `case_id`.
- Foreign keys prevent child records from pointing across Principal ownership.
- RLS separates Principal-scoped reads and Steward operational access.

- [ ] **Step 1: Write SQL contract test**

Use a migration-text test that fails unless every Principal-scoped table explicitly contains `principal_id`, RLS is enabled, and `health_cases` pins release/Blueprint versions.

- [ ] **Step 2: Run RED**

Run: `pytest tests/test_principal_isolation.py -v`
Expected: FAIL because migrations do not exist.

- [ ] **Step 3: Implement core migration**

Include uniqueness/indexes for `case_id`, `principal_id`, active Case lookup, due actions, and domain event chronology. Do not store raw Apple Health/clinical source payloads in these tables; `yh_evidence_refs` stores locator, provenance metadata, evidence class, observed_at, and optional minimized summary only.

- [ ] **Step 4: Implement RLS migration**

Policies must fail closed by default. Principal-facing policies resolve authorized `principal_id`; Steward policies require explicit membership/role rather than blanket authenticated access.

- [ ] **Step 5: Add cross-Principal negative test**

At minimum, test migration constraints statically and, when a test Supabase/Postgres instance is available, insert Principal A/B fixtures and assert A cannot read B through the application role.

- [ ] **Step 6: Run GREEN**

Run: `pytest tests/test_principal_isolation.py -v`
Expected: PASS.

- [ ] **Step 7: Commit**

```bash
git add supabase/migrations tests/test_principal_isolation.py
git commit -m "feat(yh-managed): add multi-principal product state and rls"
```

---

### Task 6: Implement Repository + Typed Intelligence Boundary + Case Service

**Files:**
- Create: `src/yuanli_health/repositories/base.py`
- Create: `src/yuanli_health/repositories/supabase_repository.py`
- Create: `src/yuanli_health/services/intelligence.py`
- Create: `src/yuanli_health/services/case_service.py`
- Test: `tests/test_intelligence_contract.py`
- Test: `tests/test_case_service.py`

**Interfaces:**
- `CaseRepository.get_case(case_id, principal_id) -> HealthCase`
- `CaseRepository.save_case(case: HealthCase) -> None`
- `CaseRepository.append_event(event) -> None`
- `IntelligenceProvider.form_thesis(case, evidence_refs) -> ThesisCandidate`
- `IntelligenceProvider.prioritize(case, thesis) -> PriorityCandidate`
- `CaseService` validates intelligence outputs before creating `HealthThesis`, `Battle`, or `Action` candidates.

- [ ] **Step 1: Write fake-provider contract test**

```python
class FakeIntelligence:
    def form_thesis(self, case, evidence_refs):
        return ThesisCandidate(
            conclusion="Insufficient evidence",
            confidence="low",
            unknowns=["sleep duration trend unavailable"],
            evidence_refs=[e.ref_id for e in evidence_refs],
        )
```

Assert that an intelligence result without evidence refs or with a claimed diagnosis is rejected by `CaseService`.

- [ ] **Step 2: Run RED**

Run: `pytest tests/test_intelligence_contract.py tests/test_case_service.py -v`
Expected: FAIL because interfaces do not exist.

- [ ] **Step 3: Implement repository protocol + deterministic fake provider + validation layer**

Do not call live OpenAI in unit tests. The production OpenAI adapter may be added only behind the same `IntelligenceProvider` interface.

- [ ] **Step 4: Add Evidence/Interpretation/Decision separation tests**

Candidate thesis must preserve `unknowns`, `conflicts`, source refs, and confidence. It may not write Outcome or Learning.

- [ ] **Step 5: Run GREEN**

Run: `pytest tests/test_intelligence_contract.py tests/test_case_service.py -v`
Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add src/yuanli_health/repositories src/yuanli_health/services tests/test_intelligence_contract.py tests/test_case_service.py
git commit -m "feat(yh-managed): add case service and replaceable intelligence boundary"
```

---

### Task 7: Implement Minimal Due-Case Worker

**Files:**
- Create: `src/yuanli_health/worker/runner.py`
- Test: `tests/test_worker.py`

**Interfaces:**
- Produces: `process_due_cases(now, repository, case_service) -> WorkerRunSummary`.
- Worker may refresh state, request candidate reasoning, create reminders/tasks, and advance only transitions authorized by Case Engine.
- Worker must never execute COMMIT/CLINICAL/DESTRUCTIVE actions.

- [ ] **Step 1: Write failing worker idempotency test**

```python

def test_same_due_case_is_not_double_advanced(fake_repo, service, frozen_now):
    first = process_due_cases(frozen_now, fake_repo, service)
    second = process_due_cases(frozen_now, fake_repo, service)
    assert first.advanced_count == 1
    assert second.advanced_count == 0
```

- [ ] **Step 2: Run RED**

Run: `pytest tests/test_worker.py -v`
Expected: FAIL because worker is missing.

- [ ] **Step 3: Implement minimal polling worker**

All durable state must live in repository/database; no Python global variable may be required for resumption.

- [ ] **Step 4: Add crash/restart simulation**

Instantiate a new Worker object using the same fake repository state and assert it resumes from stored Case state rather than repeating completed advancement.

- [ ] **Step 5: Run GREEN**

Run: `pytest tests/test_worker.py -v`
Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add src/yuanli_health/worker tests/test_worker.py
git commit -m "feat(yh-managed): add simple durable-state case worker"
```

---

### Task 8: Build Minimal Principal + Steward Projections

**Files:**
- Create: `apps/web/lib/types.ts`
- Create: `apps/web/app/principal/page.tsx`
- Create: `apps/web/app/principal/cases/page.tsx`
- Create: `apps/web/app/steward/page.tsx`
- Create: `apps/web/tests/principal-surface.test.tsx`
- Create: `apps/web/tests/steward-surface.test.tsx`

**Interfaces:**
- Principal Today projection fields: `current_conclusion`, `reason`, `decision_required`, `office_in_motion`, `evidence_door`.
- Cases projection fields: `case_id`, `title`, `state`, `owner_role`, `next_step`, `next_due_at`.
- Steward projection fields: `principal_id`, `case_id`, `attention_reason`, `owner_role`, `next_step`, `sla_risk`, `escalation_state`.

- [ ] **Step 1: Write failing Principal surface test**

Assert the primary surface does not render a total health score and always renders exactly the four product questions: what matters, why, what needs Principal decision, what the office is handling.

- [ ] **Step 2: Run RED**

Run: `cd apps/web && npm test -- principal-surface.test.tsx`
Expected: FAIL because surface does not exist.

- [ ] **Step 3: Implement static typed projection with fixture data**

Do not wire production auth/API yet; render from typed fixture/projection contract first.

- [ ] **Step 4: Write and implement Steward surface test**

Assert blocked/overdue Cases, next owner, escalation and closure queue are visible without exposing unrelated Principal data.

- [ ] **Step 5: Run GREEN**

Run: `cd apps/web && npm test`
Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add apps/web
git commit -m "feat(yh-managed): add principal and steward mvp projections"
```

---

### Task 9: Enforce Zero-Fork Product Discipline

**Files:**
- Create: `tests/test_zero_fork_guard.py`
- Create: `.github/workflows/yh-managed-product-guard.yml`

**Interfaces:**
- CI guard rejects Product Kernel code that contains known customer-specific identifiers/branches in `src/`, `product/blueprints/`, or `supabase/migrations/`.
- CI validates one release, one admitted initial Blueprint, schema validity, and READ/PREPARE boundary.

- [ ] **Step 1: Write failing zero-fork test**

```python
from pathlib import Path

FORBIDDEN = ["if principal ==", "if principal_id ==", "ray-specific", "customer-specific-code"]


def test_product_kernel_contains_no_customer_specific_branching():
    roots = [Path("src"), Path("product/blueprints"), Path("supabase/migrations")]
    corpus = "\n".join(p.read_text(errors="ignore") for root in roots for p in root.rglob("*") if p.is_file())
    for token in FORBIDDEN:
        assert token.lower() not in corpus.lower()
```

- [ ] **Step 2: Run RED if any legacy/new fork exists; otherwise prove test is meaningful by a temporary mutation**

Add a temporary forbidden token locally, confirm FAIL, then remove it.

- [ ] **Step 3: Add CI workflow**

CI runs Python tests, Blueprint/release schema validation, and frontend projection tests. It must not require live PHI or live OpenAI.

- [ ] **Step 4: Run complete local test suite**

Run: `pytest -q && (cd apps/web && npm test)`
Expected: all PASS.

- [ ] **Step 5: Commit**

```bash
git add tests/test_zero_fork_guard.py .github/workflows/yh-managed-product-guard.yml
git commit -m "test(yh-managed): enforce zero-fork product discipline"
```

---

### Task 10: Golden Principal #000 Bootstrap Acceptance Proof

**Files:**
- Create: `tests/fixtures/principal-000.json`
- Create: `tests/fixtures/evidence-minimal.json`
- Create: `tests/fixtures/sleep-case-0001.json`
- Create: `tests/acceptance/test_g1_golden_tenant_bootstrap.py`
- Create: `receipts/yh-strat2/YH-MANAGED-0.1.0-G1-BOOTSTRAP-CANDIDATE.md`

**Interfaces:**
- Fixture Principal is identified only as `principal-000`; no product logic depends on a personal name.
- Acceptance flow: create Principal → pin Release → instantiate Sleep Blueprint → create Case `NEW` → attach minimized EvidenceRefs → advance to `UNDERSTANDING` using deterministic fake intelligence.
- This acceptance test proves standard-product bootstrap only. It does **not** claim real 30-day Outcome/Learning/Reuse PASS.

- [ ] **Step 1: Write failing acceptance test**

```python

def test_principal_000_bootstraps_without_product_fork(app):
    principal = app.create_principal_from_fixture("tests/fixtures/principal-000.json")
    case = app.instantiate_case(
        principal_id=principal.principal_id,
        product_release_id="YH-MANAGED-0.1.0",
        blueprint_id="BP-SLEEP-001",
        blueprint_version="1.0.0",
    )
    assert case.principal_id == principal.principal_id
    assert case.product_release_id == "YH-MANAGED-0.1.0"
    assert case.blueprint_id == "BP-SLEEP-001"
    assert case.state == "NEW"
```

- [ ] **Step 2: Run RED**

Run: `pytest tests/acceptance/test_g1_golden_tenant_bootstrap.py -v`
Expected: FAIL because bootstrap composition is not yet wired.

- [ ] **Step 3: Add the smallest application composition layer necessary for the acceptance test**

Reuse ProductRelease, Blueprint loader, CaseService, repository, authority and Case Engine. Do not create a Ray-specific service or fixture loader in production code.

- [ ] **Step 4: Run acceptance GREEN**

Run: `pytest tests/acceptance/test_g1_golden_tenant_bootstrap.py -v`
Expected: PASS.

- [ ] **Step 5: Run full verification**

```bash
pytest -q
cd apps/web && npm test
```

Expected: all PASS; zero PHI required; zero live OpenAI required.

- [ ] **Step 6: Write bootstrap Reality Receipt**

The receipt must state exactly what was proven: ProductRelease/Blueprint pinning, Principal-scoped Case creation, one Case Engine, no Ray-specific fork, test-only deterministic intelligence. It must explicitly state that 30-day real Outcome/Learning/Reuse remains `NOT_YET_PROVEN`.

- [ ] **Step 7: Commit**

```bash
git add tests/fixtures tests/acceptance receipts/yh-strat2
git commit -m "test(yh-managed): prove golden principal standard bootstrap"
```

---

## Fresh Verification Before G1 Real-Health Run

After Tasks 1–10, create a fresh clone/worktree from the exact candidate head and run:

```bash
pytest -q
cd apps/web && npm ci && npm test
```

Then verify:

1. `git diff main...HEAD` contains no Principal-specific code path.
2. `YH-MANAGED-0.1.0` pins exactly one admitted Blueprint.
3. `BP-SLEEP-001 v1` contains no personal identifier or vendor-specific workflow node semantics.
4. Migrations create shared multi-Principal tables, not Ray-only tables.
5. RLS/ownership tests include at least Principal A/B hard negatives.
6. Worker restart test passes from durable repository state.
7. AI tests use typed candidate outputs and preserve Evidence/Interpretation/Decision separation.
8. Web surfaces render from common projection contracts.
9. No real health PHI is required for CI.
10. G1 receipt says `BOOTSTRAP_PROVEN`, not `REAL_HEALTH_OUTCOME_PROVEN`.

If all pass, present a Human Gate packet for authorization to begin the real 30-day Principal #000 Sleep Recovery Case.

---

## Follow-up Plans Triggered by Reality Evidence

Do not pre-implement these before the prior gate passes:

- `YH-STRAT2-G1｜Golden Principal 30-Day Reality Run` — fresh Local Health Kernel EvidenceRefs, Principal consent, Battle Contract, real Outcome Settlement, first Learning + reuse.
- `YH-STRAT2-G2｜Config-only Replication` — Principal #001 onboarding with exact same ProductRelease/Blueprint and zero fork.
- `YH-STRAT2-G3｜Zero Engineer Touch` — Steward-operated Principal #002 onboarding, `<60 min`, engineering touch `0`.
- `YH-STRAT2-G4｜N5 Paid Venture Proof` — paid delivery, renewal/referral, Steward capacity and measured unit economics.

## Plan Self-Review

- Spec coverage: Product release, canonical objects, Case Engine, Blueprint, authority boundary, Principal/Steward surfaces, Supabase multi-Principal state, replaceable intelligence, zero-fork discipline, G1 bootstrap and verification are mapped to Tasks 1–10.
- Explicitly deferred by scope: the real 30-day health Outcome/Learning/Reuse run and P001/P002/N5 proof. They require Reality evidence and separate plans.
- Placeholder scan: no TBD/TODO/implement-later instructions are permitted.
- Type consistency: `principal_id`, `case_id`, `product_release_id`, `blueprint_id`, `blueprint_version` are used consistently across domain, DB, worker, UI, fixtures and acceptance tests.
- Anti-complexity: no new workflow engine, policy engine, event bus, native app, model training or autonomous clinical execution is introduced.
