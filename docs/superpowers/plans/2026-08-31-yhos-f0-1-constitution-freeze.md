# YHOS-F0.1 Constitution Freeze Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Freeze a single public founder-facing orchestration constitution for `One Kernel × Two Engines × One Learning System` without creating a second Health Domain Canon, a second health truth, or a public personal-health datastore.

**Architecture:** `yuanli-life/yuanli-health` is the public invocation/orchestration layer. The active upstream Health Domain Constitution remains authoritative for Health Optionality, truth discipline, Health Clock, privacy, clinical authority and Golden Loop. Performance and Healthspan are two coordinated engines over one shared kernel, one shared H01–H12 scientific backbone and one reality learning system.

**Tech Stack:** Markdown, YAML contracts, Python standard-library validators, GitHub Actions, protected-branch workflow, synthetic evaluation fixtures; future atomic capabilities are federated from `yuanli-health-skills`.

**Spec:** `constitution/YHOS-F0.1.md`

## Global Constraints

- Health Optionality is the only North Star.
- `One Kernel × Two Engines × One Learning System`.
- Performance cannot override Healthspan safety.
- Founder Intent is invocation, not ontology.
- Recover / Adapt / Energize / Move / Think / Connect are **Six Human Functional Capacities**, not Health Domains and not the six FHP2 runtime capabilities.
- H01–H12 remain the shared scientific completeness backbone callable by both Engines.
- Healthspan owns completeness scanning, not separate Domain truth.
- Context and Clock modify judgment; they do not create truth.
- Evidence does not confer Authority; AI capability does not confer clinical authority.
- No verified Outcome → no Learning; no Task2 preload → no Reuse.
- Public Law × Private Reality.
- Do not copy atomic Skill implementations into this repository.
- F0.1 remains `proposed` until adversarial Human Review, validation, governed merge and Acceptance Receipt.

---

### Task 1: Bootstrap and authority boundary

**Files:**
- Create/confirm: `README.md`
- Create: `constitution/YHOS-F0.1.md`
- Create: `constitution/upstream-authority.yaml`

**Produces:** A non-active candidate constitution with explicit upstream precedence and anti-parallel-canon rules.

- [x] Bootstrap default branch without claiming active Constitution.
- [x] Create candidate branch.
- [x] Add YHOS-F0.1 candidate Constitution.
- [x] Add upstream authority manifest.
- [x] Adversarially review conflict precedence and all non-claims.
- [x] Pin Health Constitution, FHP2 Strategic Charter and frozen FHP2 Product Architecture source SHAs.
- [ ] Human approve candidate semantics.

### Task 2: Dual-system identity and ontology boundary

**Files:**
- Create: `systems/dual-system-registry.yaml`
- Create: `ontology/registry.yaml`
- Create: `mappings/architecture.yaml`

**Produces:** Stable identities for Shared Kernel, Performance Engine, Healthspan Engine, Six Human Functional Capacities, shared H01–H12 Domains, Health Clock and upstream identity pins.

- [x] Register Shared Kernel and both Engines.
- [x] Register Six Human Functional Capacities as projections.
- [x] Disambiguate Human Functional Capacities from FHP2's six product runtime capabilities.
- [x] Pin H01–H12 exact Domain IDs/names from frozen FHP2 architecture.
- [x] Pin C01–C04 exact Context IDs/names.
- [x] Preserve five canonical collaboration-role labels while marking local routing IDs non-authoritative.
- [x] Freeze H01–H12 as shared scientific backbone callable by both Engines.
- [x] Register Health Clock public projection.
- [x] Freeze orthogonal mapping relation semantics without fake numeric weights.

### Task 3: Founder invocation and dual-system routing

**Files:**
- Create: `intents/registry.yaml`
- Create: `routing/dual-system-router.yaml`

**Produces:** Five Founder Intent classes and deterministic routing semantics into Performance-first, Healthspan-first or Coupled modes.

- [x] Register five top-level Founder Intents.
- [x] Freeze cross-system arbitration priority.
- [x] Freeze Founder Brief output contract shape.
- [x] Freeze `Performance cannot override Healthspan safety`.
- [ ] F2: implement executable semantic router against synthetic fixtures.

### Task 4: Agent-callable protocol

**Files:**
- Create: `AGENTS.md`

**Produces:** A deterministic read order, reasoning sequence, public/private boundary and non-negotiable safety rules for ChatGPT/Codex/agents.

- [x] Add mandatory read order.
- [x] Add L1/L2/L3 progressive expertise disclosure.
- [x] Add fail-closed and false-claim prohibitions.
- [x] Add shared-domain and Human Functional Capacity naming guardrails.
- [ ] F4: add `capabilities/dependencies.yaml` and verified Skill source pins.

### Task 5: Pre-registered Golden Journeys

**Files:**
- Create: `evaluations/golden-journeys.yaml`

**Produces:** Eight synthetic founder journeys plus one future cross-system reality reuse gate.

- [x] Pre-register Performance-primary journeys.
- [x] Pre-register Healthspan-primary journeys.
- [x] Pre-register Coupled journeys.
- [x] Define future `FIRST_CROSS_SYSTEM_HEALTH_REUSE` gate without claiming it exists.
- [ ] F2/F3: build executable expected-route fixtures and scoring harness.

### Task 6: Minimal validation and privacy CI

**Files:**
- Create: `scripts/validate_repository.py`
- Create: `scripts/scan_public_content.py`
- Create: `.github/workflows/validate-f0-1.yml`
- Test: `tests/test_repository_contract.py`

**Interfaces:**
- Consumes: all F0.1 registries, router, agent protocol and Constitution invariants.
- Produces: deterministic PASS/FAIL for missing assets, identity/routing invariants, upstream pins and obvious public PHI/secret patterns.

- [x] Pre-register failing repository contract tests before validator/scanner implementation.
- [x] Verify RED when validator/scanner scripts did not yet exist.
- [x] Implement minimal structural validator.
- [x] Implement minimal public-content/privacy scanner.
- [x] Add GitHub Actions CI.
- [x] Verify initial green candidate run (`33390141571`).
- [x] Observe expected RED after replacing pending upstream identities with exact pinned identities (`33390370666`).
- [x] Update validator for exact H01–H12/C01–C04 identity contract.
- [x] Verify hardened candidate green (`33390577168`).
- [ ] Re-verify exact Draft PR head after review/status updates.

### Task 7: Constitution candidate PR and Human Freeze

**Files:**
- Create: `reviews/F0.1-ADVERSARIAL-SELF-REVIEW.md`
- Update: `status/F0.1-CANDIDATE.md`
- Future: independent Acceptance Receipt only after legal merge/acceptance.

**Produces:** Governed transition from candidate to active only after explicit approval.

- [x] Complete adversarial self-review against seven invariants and dual-system boundary.
- [x] Resolve Human Functional Capacity naming collision.
- [x] Resolve shared H01–H12 scientific-backbone semantics.
- [x] Resolve exact upstream identity pins where source identities exist.
- [x] Inspect real GitHub governance state.
- [x] Identify current blocker: `main.protected = false` and no required status checks.
- [ ] Create governance issue for `main` protection / ruleset installation.
- [ ] Open Draft PR from `yhos-f0-1-constitution-candidate` to `main`.
- [ ] Review exact changed-file set and PR diff.
- [ ] Verify pull-request-triggered CI is green on exact PR head.
- [ ] Install repository governance before any Freeze claim.
- [ ] Obtain explicit Human semantic acceptance.
- [ ] Obtain explicit Human merge authorization for exact PR head.
- [ ] Merge through governed path.
- [ ] Add independent Acceptance Receipt.
- [ ] Transition `status: proposed → active` only through a separately governed change if required by the final governance contract.

## Exit Criteria

F0.1 is not complete merely because files exist or CI is green. Exit requires:

```text
NO_SECOND_CANON
+ ONE_KERNEL_TWO_ENGINES_ONE_LEARNING_SYSTEM
+ UPSTREAM_AUTHORITY_PINNED
+ HUMAN_FUNCTIONAL_CAPACITY_IDENTITY_CLEAR
+ H01_H12_SHARED_SCIENTIFIC_BACKBONE
+ FOUNDER_INTENT_NOT_ONTOLOGY
+ PUBLIC_LAW_PRIVATE_REALITY
+ GOLDEN_JOURNEYS_PREREGISTERED
+ VALIDATION_GREEN_ON_EXACT_PR_HEAD
+ MAIN_GOVERNANCE_INSTALLED
+ HUMAN_ACCEPTED
+ GOVERNED_MERGE
+ ACCEPTANCE_RECEIPT
```

Only then may Domain capability content expand under an active F0.1 architecture.
