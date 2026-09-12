# YH-LW1 Business Model Canon × Notion Projection Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Research Longevity World × MORROW as a verified business system, freeze a Yuanli Health Pattern Admission, and publish a governed GitHub Canon Candidate plus a human-readable Notion projection.

**Architecture:** GitHub is the machine-authoritative research candidate containing sources, fact/inference separation, pattern admission and receipts. Notion is a human projection under YHT0 and may summarize but never outrank GitHub. Both surfaces share stable object ID `YH-LW1`.

**Tech Stack:** GitHub repository contents/PR workflow, Notion page projection, web evidence from first-party and independent sources.

**Spec:** Conversation-approved `YH-LW1-G0｜Business Model Canon × Pattern Admission × GitHub/Notion Projection Freeze`.

## Global Constraints

- Object ID is exactly `YH-LW1`.
- Authority remains `research_candidate` until Human Review / merge.
- Company expansion, funding and revenue numbers must be labelled as public management claims/targets unless independently verified.
- Notion is Human Projection only; it must not become a second research canon.
- No personal health data or PHI enters this research object.
- Pattern Admission must distinguish `ADMIT`, `STRONG ADMIT`, `PARTIAL ADMIT`, `DO NOT COPY`, and `REJECT / EVIDENCE GATE`.

---

### Task 1: Reality research and evidence registry

**Files:**
- Create: `research/benchmark/longevity-world-morrow/YH-LW1-business-model-reality-audit.md`
- Create: `research/benchmark/longevity-world-morrow/source-registry.yaml`

**Interfaces:**
- Consumes: first-party Longevity World / MORROW pages, independent reporting, Singapore entity data.
- Produces: verified fact base and explicit source registry used by Pattern Admission and Notion projection.

- [x] Search first-party product, pricing, care-team, leasing and journey pages.
- [x] Cross-check with independent industry/media sources and entity registry.
- [x] Separate verified facts, company targets and Yuanli inference.
- [x] Freeze business-model decomposition and risk analysis.

### Task 2: Pattern Admission

**Files:**
- Create: `research/benchmark/longevity-world-morrow/admissions/YH-LW1-PATTERN-ADMISSION.md`

**Interfaces:**
- Consumes: Task 1 fact base.
- Produces: Yuanli-specific pattern decisions and differentiation thesis.

- [x] Evaluate each pattern against Health Optionality and Sovereign Principal Health Office.
- [x] Strongly admit managed state transition, one relationship owner, medical+lifestyle coordination, bounded plans and repeatable methodology.
- [x] Reject copying asset-heavy centres, modality-led moats and weak-evidence claims.

### Task 3: Notion human projection

**Files / Surfaces:**
- Create Notion child page under `YHT0｜Yuanli Health Think Tank Constitution`.

**Interfaces:**
- Consumes: Tasks 1–2.
- Produces: executive human-readable projection with stable object ID and links back to GitHub.

- [x] Create page `YH-LW1｜Longevity World × MORROW｜商业模式 × Pattern Admission`.
- [x] Include 30-second thesis, two-business model, revenue stack, flywheel, risks, admission matrix and Yuanli synthesis.
- [x] Declare Notion projection authority boundary.

### Task 4: Cross-surface binding and receipt

**Files:**
- Modify: `research/benchmark/longevity-world-morrow/YH-LW1-business-model-reality-audit.md`
- Create: `research/benchmark/longevity-world-morrow/receipts/YH-LW1-G0-PROJECTION-RECEIPT.json`

**Interfaces:**
- Consumes: Notion page URL from Task 3.
- Produces: bidirectional locator metadata without creating dual authority.

- [ ] Bind Notion page URL into GitHub frontmatter.
- [ ] Record GitHub branch, object ID, Notion projection URL, as-of date and authority in immutable-style receipt.
- [ ] Fresh-read GitHub files and Notion page to verify stable ID and authority text.

### Task 5: Human Review PR

**Files / Surfaces:**
- Open Draft PR from `research/yh-lw1-longevity-world-morrow-20260912` to `main`.

**Interfaces:**
- Consumes: Tasks 1–4.
- Produces: explicit Human Gate before promotion from research candidate.

- [ ] Create Draft PR summarizing verified facts, admitted patterns, non-admitted patterns and projection location.
- [ ] Keep PR Draft; do not merge without explicit Human approval.
