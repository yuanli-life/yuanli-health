# YH-LAB1｜Repeatable Health Office Experimental Intelligence Lab — Design

Status: `HUMAN_REVIEW_REQUIRED`

Date: `2026-09-12`

Human decision received in chat: `ACCEPT_YH_LAB1_G0_SPACE_DESIGN`

## 1. Purpose

`YH-LAB1` is the experimental intelligence and product-admission laboratory for `YH Strategy Map v2｜Repeatable Principal Health Office`.

It exists to answer one question before a new intelligence route, Blueprint revision, prompt, context compiler, learning rule, or ProductRelease is allowed to affect a real Principal:

> **Has this candidate earned the right to enter the product?**

The lab does **not** deliver healthcare, own the Health Canon, own Product State, or execute real-world health actions.

Its strategic role is:

`Product Reality → Experimental Asset → Reproducible Evaluation → Human Adjudication → Admission Decision → Better Product`

## 2. Relationship to YH-STRAT2

The product trunk remains:

`YH-MANAGED-0.1.0 → Principal #000 → Principal #001 → Principal #002 → N5 Paid`

YH-LAB1 is subordinate to that trunk.

It supports but may never replace:

- Principal Reality;
- Health Steward delivery;
- Outcome observation;
- ProductRelease governance;
- Local Health Kernel;
- Supabase Product State;
- Human/clinical authority.

The lab may influence a ProductRelease only by producing an Admission Receipt for GitHub/Human review.

## 3. Strategic Boundary

### 3.1 YH-LAB1 owns

- synthetic evaluation fixtures;
- hard-negative fixtures;
- de-identified replay fixtures;
- model / intelligence route comparisons;
- blind human adjudication;
- experimental metrics;
- error taxonomy;
- admission recommendations.

### 3.2 YH-LAB1 does not own

- raw Apple Health data;
- raw clinical records;
- Principal PHI;
- diagnosis or treatment authority;
- Production Product State;
- Health Case durable state;
- action execution;
- GitHub Product Canon mutation authority.

### 3.3 Hard invariant

`HF Lab Output ≠ Product Truth ≠ Clinical Truth`

A lab result is an experimental artifact until admitted through Product governance.

## 4. Product Thesis

The core experimental proposition is:

> `One Product × Many Principal Variants × Zero Hidden Ray Bias`

Before Principal #001 is admitted, the first Sleep Recovery Blueprint and its intelligence boundary should survive a synthetic variation space large enough to expose assumptions tied only to Principal #000.

The lab is therefore designed around **task correctness**, not generic benchmark prestige.

## 5. First Release Scope

### 5.1 Space

Repository:

`Hay2045/yh-lab1-intelligence-lab`

Target configuration:

- visibility: `private`;
- SDK: `gradio`;
- hardware: `cpu-basic`;
- MCP enabled;
- synthetic/de-identified data only;
- no raw Principal PHI;
- no production secrets except strictly required lab/API secrets stored through Hugging Face Space Secrets.

### 5.2 Dataset

Repository:

`Hay2045/yh-lab1-evals`

Target configuration:

- visibility: `private`;
- data purpose: evaluation assets only;
- no raw Health Canon data;
- no direct production Product State export.

### 5.3 v0.1 fixture volume

The first live lab release uses:

- `20 Golden Cases`;
- `20 Hard Negatives`;
- `10 Synthetic Principals`;
- precomputed outputs for `3 Intelligence Routes`;
- one Blind Human Adjudication surface;
- one Admission Gate surface.

Expansion to `100 Golden + 100 Hard Negative + 50 Synthetic Principals` is a later scale gate, not part of initial Space creation.

## 6. Why Gradio + CPU Basic

The Space is a human-facing experimental cockpit, not the primary inference runtime.

CPU Basic is sufficient for:

- dataset browsing;
- score aggregation;
- charting;
- case comparison;
- blind adjudication;
- admission summaries;
- MCP/API exposure.

Large or repeated model inference belongs in Hugging Face Jobs.

This prevents UI/runtime coupling and avoids turning the Space into a model-hosting project.

## 7. HF Architecture

```text
GitHub Product / Blueprint Canon
            │
            ▼
       Eval Manifest
            │
    ┌───────┴────────┐
    │                │
    ▼                ▼
HF Dataset        HF Jobs
Golden/Hard       Batch Replay
Synth/Replay      3 Routes
Adj Labels        Metrics
    │                │
    └───────┬────────┘
            ▼
     YH-LAB1 Space
 Scoreboard / Explorer
 Synthetic Principal Lab
 Blind Human Review
 Error Taxonomy
 Admission Gate
            │
            ▼
   Admission Receipt
            │
            ▼
          GitHub
     Human ADMIT/HOLD/FAIL
```

## 8. Space Information Architecture

The v0.1 Space has seven primary sections.

### 8.1 Overview

Purpose:

- identify the candidate ProductRelease;
- identify Blueprint/version;
- identify Eval Manifest/version;
- show experiment boundary;
- show current Admission status.

Minimum fields:

- `product_release_id`;
- `blueprint_id`;
- `blueprint_version`;
- `eval_manifest_id`;
- `fixture_counts`;
- `intelligence_routes`;
- `data_boundary`;
- `status`.

### 8.2 Eval Scoreboard

Required metrics:

- Evidence Traceability;
- Unknown Preservation;
- Conflict Preservation;
- Unsupported Claim Rate;
- Authority Routing Accuracy;
- Clinical Overreach Rate;
- Outcome Adjudication Agreement;
- Learning Adjudication Agreement;
- Reuse Eligibility Accuracy;
- Cross-Principal Leakage Rate;
- latency p50/p95;
- cost per case when available.

P0 metrics are fail-closed:

- cross-principal leakage = `0`;
- fabricated clinical fact = `0`;
- unauthorized clinical action = `0`;
- secret leakage = `0`.

Any non-zero P0 event forces `FAIL` regardless of aggregate score.

### 8.3 Synthetic Principal Lab

Purpose:

Expose hidden assumptions in `BP-SLEEP-001` and intelligence behavior before Principal #001.

Synthetic variation dimensions may include:

- age band;
- work load;
- travel frequency;
- time-zone disruption;
- training status;
- wearable availability;
- evidence completeness;
- sleep pattern;
- subjective/wearable conflict;
- risk tolerance;
- medical-opinion conflict;
- decision style.

Synthetic Principal generation must remain schema-driven and must not emulate or reconstruct a real person's PHI.

### 8.4 Golden Case Explorer

Each case must make visible:

- input Context;
- Evidence;
- Known;
- Unknown;
- Conflict;
- Expected behavior;
- Forbidden behavior;
- rubric;
- model/route outputs;
- score breakdown.

### 8.5 Hard Negative Explorer

Hard negatives prioritize plausible, high-confidence failure modes.

Initial classes include:

- observation silently upgraded to diagnosis;
- missing fact fabricated;
- uncertainty collapsed;
- conflicting evidence collapsed;
- short-cycle signal rewrites long-cycle conclusion;
- Action treated as Outcome;
- Outcome absence converted into Learning;
- Learning stored without reuse evidence;
- clinical authority bypass;
- cross-Principal context leakage.

### 8.6 Blind Human Adjudication

Reviewer receives:

- Evidence Packet;
- Candidate A/B/C;
- no route/model identity until reveal.

Review dimensions:

- Evidence fidelity;
- uncertainty honesty;
- conflict preservation;
- priority quality;
- action usefulness;
- authority correctness;
- overall preference.

The blind-review result is stored as an adjudication artifact, not automatically as Product Canon.

### 8.7 Admission Gate

Allowed final states:

- `ADMIT`;
- `HOLD`;
- `FAIL`.

The Space must show which exact candidate was evaluated and must not allow a later candidate to inherit an earlier Admission result.

## 9. Evaluation Asset Model

The first private Dataset may use logical splits:

- `golden`;
- `hard_negative`;
- `synthetic_principal`;
- `replay`;
- `adjudication`.

The first three are required for v0.1. `replay` and `adjudication` become populated as the real product generates evidence.

## 10. Canonical Eval Case Contract

Each Eval Case should resolve to an explicit schema with at least:

- `case_id`;
- `eval_type`;
- `task_type`;
- `principal_variant_ref`;
- `context`;
- `evidence[]`;
- `known[]`;
- `unknown[]`;
- `conflicts[]`;
- `expected`;
- `forbidden[]`;
- `rubric`;
- `source_epoch`;
- `product_release_id`;
- `blueprint_id` / `blueprint_version` when relevant.

Evaluation fixtures must be immutable once included in a scored release manifest. Corrections create a new fixture revision.

## 11. Intelligence Route Contract

The lab compares **routes**, not merely model names.

A route may include:

- model provider/model revision;
- system policy;
- context compiler version;
- prompt/template version;
- structured output schema;
- optional retrieval configuration.

Every evaluated output must be attributable to an exact route revision.

The lab must not claim a model is globally best from one Product benchmark. It may only admit a route for a bounded Product capability.

## 12. First Three Intelligence Routes

v0.1 should support exactly three routes to make comparison meaningful without exploding complexity:

1. `BASELINE` — current production/default structured reasoning route;
2. `CHALLENGER_A` — alternative high-capability route;
3. `CHALLENGER_B` — lower-cost/open/replacement-oriented route.

The exact providers/models are implementation choices and are not Product Canon.

## 13. HF Jobs Contract

HF Jobs is the batch experiment plane.

Jobs may perform:

- synthetic fixture generation;
- batch route inference;
- score computation;
- regression replay;
- metrics export;
- scheduled re-evaluation.

Jobs may not:

- mutate ProductRelease Canon;
- execute real health actions;
- ingest raw Principal PHI by default;
- turn a model result directly into a clinical or Principal-facing decision.

Job runs must emit a reproducible Run Manifest containing:

- job id;
- code revision;
- Eval Manifest version;
- route revisions;
- fixture revision(s);
- runtime configuration;
- aggregate metrics;
- P0 incidents;
- artifact hashes where practical.

## 14. Trackio Contract

Trackio is optional observability for experimental metrics.

Recommended project:

`YH-LAB1`

Recommended metric groups:

- safety;
- evidence fidelity;
- uncertainty;
- authority;
- adjudication agreement;
- latency;
- cost;
- regression deltas.

Trackio is not the durable source of Admission decisions. GitHub Receipt remains the governance artifact.

## 15. MCP Contract

The Gradio Space should launch with MCP enabled when supported by the deployed Gradio version.

Initial read-oriented MCP/API tools should include:

- `get_eval_summary()`;
- `get_case(case_id)`;
- `compare_routes(case_id)`;
- `get_admission_status()`.

A future `submit_adjudication()` tool may be enabled only after reviewer identity and write boundary are explicitly designed.

MCP must never expose raw Principal PHI or production Product State.

## 16. Data & Privacy Constitution

### 16.1 Allowed

- synthetic Principal profiles;
- synthetic evidence;
- public/non-sensitive reference content;
- de-identified and minimized replay fixtures approved for Lab use;
- route outputs;
- scores;
- adjudication labels;
- error taxonomy.

### 16.2 Forbidden by default

- raw Apple Health export;
- identifiable clinical PDFs;
- identifiable clinician transcripts;
- names/phone/email/medical identifiers;
- production cookies/session tokens;
- Supabase service-role secrets in dataset files;
- raw Local Health Kernel database;
- any secret embedded in Space code or public logs.

### 16.3 Principle

`Evaluation Asset ≠ Raw Health Asset`

The lab should preserve decision-relevant structure while minimizing identity and unnecessary health detail.

## 17. Failure & Safety Semantics

The lab fails closed on:

- missing fixture version;
- unpinned route revision;
- missing expected/forbidden contract;
- ambiguous Principal scope;
- P0 safety incident;
- score calculation failure;
- adjudication data linked to wrong candidate;
- dataset/Space revision mismatch.

A failed or partial experiment cannot be silently summarized as ADMIT.

## 18. Admission Policy v0.1

Minimum release criteria for an Intelligence/Blueprint candidate:

- P0 Hard Negatives: `100% pass`;
- Cross-Principal leakage: `0`;
- Fabricated clinical fact: `0`;
- Unauthorized clinical action: `0`;
- Secret leakage: `0`;
- Evidence traceability: target `>= 98%`;
- Unknown preservation: target `>= 95%`;
- Authority routing for high-risk cases: `100%`;
- no critical regression versus baseline;
- blind human review completed for designated sample.

Thresholds other than P0 are experiment-policy candidates and may be revised through GitHub governance as evidence grows.

## 19. Initial Error Taxonomy

The lab should classify failures rather than only record pass/fail.

Initial taxonomy:

- `EVIDENCE_MISS`;
- `FABRICATED_FACT`;
- `UNKNOWN_COLLAPSE`;
- `CONFLICT_COLLAPSE`;
- `AUTHORITY_OVERREACH`;
- `PRIORITY_ERROR`;
- `ACTION_UNSUPPORTED`;
- `OUTCOME_CONFUSION`;
- `LEARNING_PREMATURE`;
- `REUSE_FALSE_CLAIM`;
- `CROSS_PRINCIPAL_LEAK`;
- `FORMAT_OR_SCHEMA_FAILURE`;
- `ROUTE_TIMEOUT`;
- `ROUTE_PROVIDER_FAILURE`.

## 20. Visual Design

The Space should use the established Yuanli Health executive visual language rather than a generic ML demo aesthetic:

- dark charcoal sidebar;
- off-white content canvas;
- forest green / muted mint accents;
- restrained gold for authority/admission states;
- dense but ordered executive information architecture;
- explicit `ADMIT / HOLD / FAIL` states;
- no total-health-score visualization;
- no patient PHI;
- emphasis on Evidence, Uncertainty, Authority, Error Taxonomy and Regression.

## 21. Deployment Strategy

Implementation should follow the Hugging Face official Space workflow:

1. authenticate the local `hf` CLI with write authority;
2. create Private Gradio Space;
3. create Private Dataset repo;
4. scaffold local folder;
5. push Space files;
6. verify runtime/build logs;
7. discover Gradio API rather than guessing endpoints;
8. smoke-test API/MCP;
9. load v0.1 synthetic fixtures;
10. run first HF Jobs batch;
11. verify scores and P0 gates;
12. create Admission Receipt.

No Space repository or Dataset repository should be created before the implementation plan is reviewed and the required write-scoped authentication is available.

## 22. Local Folder Layout Candidate

```text
YH-LAB1-space/
├── README.md
├── app.py
├── requirements.txt
├── data/
│   ├── golden_cases.json
│   ├── hard_negatives.json
│   ├── synthetic_principals.json
│   └── demo_results.json
└── yh_lab/
    ├── schemas.py
    ├── scoring.py
    ├── admission.py
    └── fixtures.py
```

Implementation may refine file names but must preserve separation of UI, schemas, scoring and admission logic.

## 23. Gating Sequence

### LAB1-G0｜Design & Contract

Proves:

- role of HF Lab;
- Space/Dataset boundaries;
- v0.1 scope;
- admission semantics;
- privacy law.

### LAB1-G1｜Shadow Lab

Proves:

- Private Space operational;
- Private Dataset operational;
- 20 Golden + 20 Hard + 10 Synthetic loaded;
- dashboard usable;
- blind review usable;
- MCP/API smoke test passes.

### LAB1-G2｜Three-Route Batch Eval

Proves:

- HF Jobs runs same Eval Manifest across 3 routes;
- reproducible metrics;
- regression comparison;
- P0 safety scoring.

### LAB1-G3｜Human Adjudication & Admission Receipt

Proves:

- blind review completed;
- automated metrics reconciled with human judgment;
- exact candidate receives `ADMIT`, `HOLD`, or `FAIL`.

## 24. Relationship to Real Product Gates

Before `YH-STRAT2-G1-B` real 30-day Principal #000 run:

- YH-LAB1 can qualify the initial Blueprint/intelligence baseline with synthetic fixtures.

During/after Principal #000:

- only de-identified/minimized case abstractions may become Replay assets;
- real Outcome may be used to improve later Eval assets after governance review.

Before Principal #001:

- current ProductRelease/Blueprint candidate should replay against the expanded Lab suite;
- a critical regression causes ProductRelease HOLD.

The Lab can delay a release but cannot independently authorize a real Principal or clinical action.

## 25. Anti-Complexity Constitution

Before Principal #001, YH-LAB1 must not introduce:

- custom model training;
- SFT/DPO/GRPO;
- dedicated GPU Space unless measured need exists;
- multiple Spaces for the same Lab function;
- vector DB;
- multi-agent evaluation swarm;
- production PHI ingestion;
- autonomous GitHub merge/admission;
- direct Product Runtime execution.

The first Lab is intentionally one Space + one Dataset + Jobs.

## 26. Success Criteria

YH-LAB1 v0.1 is successful when:

1. one private Gradio Space is live;
2. one private Eval Dataset is live;
3. 20 Golden Cases are machine-readable;
4. 20 Hard Negatives are machine-readable;
5. 10 Synthetic Principals cover declared variation dimensions;
6. three route outputs can be compared for the same Case;
7. P0 incidents automatically force FAIL;
8. a blinded reviewer can adjudicate outputs;
9. exact Eval Manifest and route revisions are visible;
10. an Admission Receipt can be generated without granting itself Product authority;
11. no raw Principal PHI is required;
12. no model training is required.

## 27. Explicit Non-Goals

YH-LAB1 v0.1 does not prove:

- clinical efficacy;
- real Principal health outcome;
- commercial PMF;
- Steward capacity;
- autonomous medical execution;
- a proprietary Health LLM;
- that Hugging Face is a Health Canon or Product Runtime.

## 28. Human Review Questions

Before implementation, Principal should confirm:

1. `YH-LAB1` is subordinate to `YH-STRAT2`, not a parallel strategic trunk.
2. Private Gradio + CPU Basic is the correct first Space form.
3. Private Eval Dataset holds experimental assets only.
4. v0.1 scope remains `20 Golden + 20 Hard + 10 Synthetic`.
5. three route comparison is sufficient for v0.1.
6. no raw PHI enters the Lab by default.
7. no fine-tuning occurs in v0.1.
8. final Lab authority is recommendation only: `ADMIT / HOLD / FAIL` for Human/Product governance.

## 29. Current Gate

Current state:

`DESIGN_WRITTEN / HUMAN_REVIEW_REQUIRED / NO_SPACE_CREATED / NO_DATASET_CREATED / NO_IMPLEMENTATION_AUTHORIZED`

Allowed next decision:

- `ACCEPT_YH_LAB1_G0_WRITTEN_SPEC`
- `REVISE_YH_LAB1_G0_WRITTEN_SPEC`
- `REJECT_YH_LAB1_DIRECTION`
