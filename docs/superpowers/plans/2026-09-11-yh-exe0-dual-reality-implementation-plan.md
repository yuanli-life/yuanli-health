# YH-EXE0 Dual Reality Architecture Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a testable dual-loop runtime where Hugging Face admits intelligence changes and n8n + Ego executes only authorized Action Contracts with durable Receipts.

**Architecture:** GitHub remains Law; Health Canon remains upstream Reality; Hugging Face runs synthetic evaluation; n8n orchestrates state; a local Ego runner performs browser last-mile actions. The two loops converge only through typed contracts and receipts.

**Tech Stack:** JSON Schema 2020-12, Python 3.11, n8n, ego-browser, Hugging Face Jobs/Trackio, Supabase projection/receipt plane.

**Spec:** `docs/specs/YH-EXE0-DUAL-REALITY-ARCHITECTURE-v0.1.md`

## Global Constraints

- No production health canon is copied into Hugging Face or GitHub.
- Ego accepts schema-valid Action Contracts only.
- `CLINICAL` actions require clinician approval; `COMMIT`/`DESTRUCTIVE` require explicit principal approval.
- No verified ACT without Receipt; no Learning without observed OUT; no compounding without reuse receipt.
- P0 safety violations fail the build.

---

### Task 1: Contract Validation Kernel

**Files:**
- Create: `runtime/contracts/validator.py`
- Test: `tests/test_contract_schemas.py`
- Uses: `contracts/action-contract-v1.schema.json`, `contracts/action-receipt-v1.schema.json`

**Produces:** `validate_action_contract(dict) -> list[str]`, `validate_action_receipt(dict) -> list[str]`.

- [ ] Write tests proving the synthetic contract and real smoke receipt validate.
- [ ] Add failing tests for expired contract, revoked contract, missing clinician approval on CLINICAL, missing principal approval on COMMIT, and `receipt_required=false`.
- [ ] Implement minimal schema + semantic validation.
- [ ] Run `python -m unittest tests.test_contract_schemas -v` and require PASS.
- [ ] Commit `feat(rex0): add action contract validation kernel`.

### Task 2: Ego Runner Dry-Run Boundary

**Files:**
- Create: `runtime/ego_runner/runner.py`
- Create: `runtime/ego_runner/README.md`
- Test: `tests/test_ego_runner_policy.py`

**Produces:** `execute_contract(contract, mode="dry-run") -> receipt`.

- [ ] Write tests that reject non-allowlisted domain/action and expired/revoked contracts before invoking Ego.
- [ ] Implement a process adapter that invokes `ego-browser nodejs` only after validation.
- [ ] Redact cookies, tokens, authorization headers and form secrets from logs/receipts.
- [ ] Add `--smoke` path using `fixtures/yh-rex0/synthetic-action-contract.valid.json`.
- [ ] Run smoke against `example.com` and require a schema-valid Receipt.
- [ ] Commit `feat(rex0): add bounded ego runner`.

### Task 3: Action Queue Protocol

**Files:**
- Create: `contracts/action-envelope-v1.schema.json`
- Create: `docs/specs/YH-REX0-QUEUE-PROTOCOL-v0.1.md`
- Test: `tests/test_action_envelope.py`

**Produces:** idempotent queue envelope with `contract_hash`, `attempt`, `not_before`, `expires_at`.

- [ ] Add duplicate/idempotency tests.
- [ ] Add stale/expired delivery tests.
- [ ] Freeze retryable vs non-retryable error classes.
- [ ] Require a Receipt or explicit terminal failure for every dequeued contract.
- [ ] Commit `feat(rex0): freeze action queue protocol`.

### Task 4: n8n Orchestrator Shadow Workflow

**Files:**
- Create: `workflows/n8n/yh-rex0-shadow-workflow.json`
- Create: `workflows/n8n/README.md`
- Test: `tests/test_n8n_workflow_contract.py`

**Flow:** `Webhook/Manual Trigger → Validate → Authority Switch → Approval/Wait → Runner Call → Receipt Validation → State Write`.

- [ ] Resolve the actual n8n runtime/instance; do not assume `n8n-mcp` equals production n8n.
- [ ] Import the shadow workflow with all external writes disabled by default.
- [ ] Prove `READ` synthetic contract reaches Ego runner and returns Receipt.
- [ ] Prove `COMMIT` without principal approval stops at approval gate.
- [ ] Prove `CLINICAL` without clinician approval cannot reach runner.
- [ ] Commit `feat(rex0): add n8n shadow orchestrator`.

### Task 5: Runtime Receipt Projection

**Files:**
- Create: `contracts/runtime-state-transition-v1.schema.json`
- Create: `docs/specs/YH-REX0-RECEIPT-PROJECTION-v0.1.md`
- Test: `tests/test_runtime_transitions.py`

**Produces:** append-only state transitions and receipt references; no canonical health values.

- [ ] Test allowed state transitions from `PROPOSED` through terminal execution states.
- [ ] Reject silent skips such as `PROPOSED → COMPLETED`.
- [ ] Require actor, authority, timestamp and evidence/receipt reference on every transition.
- [ ] Integrate Supabase projection only after local tests pass.
- [ ] Commit `feat(rex0): add runtime receipt projection contract`.

### Task 6: HF Eval Harness

**Files:**
- Create: `eval/hf/run_eval.py`
- Create: `eval/hf/scorers.py`
- Test: `tests/test_eval_scoring.py`

**Produces:** one JSON Eval Receipt per model/prompt/context-compiler build.

- [ ] Validate all EvalSet rows against `contracts/eval-case-v1.schema.json`.
- [ ] Implement scorers for provenance, unknown preservation, authority routing, forbidden claims and exact structured fields.
- [ ] Fail the run on any P0 violation.
- [ ] Log quality/latency/cost metrics to Trackio when configured; preserve local JSON output otherwise.
- [ ] Commit `feat(hf0): add intelligence eval harness`.

### Task 7: 60 Golden + 20 Hard Negatives

**Files:**
- Create: `eval/cases/golden/*.json`
- Create: `eval/cases/hard-negatives/*.json`
- Create: `eval/README.md`

- [ ] Create six Golden Cases for each of the ten PC surfaces.
- [ ] Create 20 P0/P1 hard negatives covering leakage, missing evidence, authority, clock mismatch, ACT/OUT confusion, unsupported causality and false reuse.
- [ ] Human-review every expected result before using it as an admission gate.
- [ ] Run schema validation across 80 cases.
- [ ] Commit `test(hf0): freeze first 80-case eval set`.

### Task 8: Intelligence Admission Gate

**Files:**
- Create: `eval/hf/admission.py`
- Create: `docs/specs/YH-HF0-ADMISSION-GATE-v0.1.md`
- Test: `tests/test_admission_gate.py`

- [ ] Encode P0 zero-tolerance rules.
- [ ] Encode initial threshold gates from YH-HF0 spec.
- [ ] Produce `ADMIT`, `REJECT`, or `INCONCLUSIVE` with metric evidence.
- [ ] Prove a deliberately unsafe candidate is rejected.
- [ ] Commit `feat(hf0): add intelligence admission gate`.

### Task 9: Dual-Loop E2E Reality Proof

**Files:**
- Create: `receipts/yh-exe0/README.md`
- Create: `docs/reality/YH-EXE0-R0-REPORT.md`

- [ ] Run Loop A on a synthetic READ task and obtain `ADMIT`.
- [ ] Feed only admitted structured output into Action Contract generation.
- [ ] Route through n8n authority gate to Ego runner.
- [ ] Execute harmless public-page read in isolated Ego Task Space.
- [ ] Validate Receipt and write runtime transition.
- [ ] Confirm no health canon, credential, cookie or private path appears in artifacts.
- [ ] Record `PASS / PARTIAL_PASS / FAIL` with exact blockers.
- [ ] Commit `test(exe0): record first dual-loop reality proof`.

### Task 10: 90-Day Rollout Gates

**Files:**
- Create: `docs/rollout/YH-EXE0-90-DAY-ROLLOUT.md`

- [ ] R0: synthetic-only dual-loop proof.
- [ ] R1: RAY read-only shadow using minimized projections; no automatic commit actions.
- [ ] R2: three Founder shadows with different health task classes.
- [ ] R3: five paying Principals; production surface separate from HF Shadow.
- [ ] Require `0` P0 violations, >=95% provenance/unknown gates as applicable, and at least one real Task2 reuse receipt before claiming compounding.
- [ ] Commit `docs(exe0): freeze 90-day reality rollout`.

## Self-Review

Coverage check: Law, Intelligence Eval, Authority, n8n state machine, Ego boundary, Receipt, OUT/LRN/REUSE and 90-day Reality Gates each have an owning task. No task grants HF, n8n or Ego canonical health authority. Production execution remains blocked until the actual n8n runtime is identified and the first approval-gated shadow workflow passes.
