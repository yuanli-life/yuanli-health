# YH-STRAT2-G0｜Repeatable Principal Health Office Product Constitution × MVP Contract Freeze

Status: `HUMAN_REVIEW_REQUIRED`

Date: `2026-09-11`

Authority parent:
- `YH2-C1-HEALTH-CONSTITUTION.md`
- `cases/YH-CGE1/README.md`
- `cases/YH-CGE1/protocol.yaml`

Strategic stage: `YH2_REALITY_CONVERGENCE → PRODUCT_REPLICATION_PROOF`

---

## 0. Crown Definition

Yuanli Health is not a health dashboard, an AI doctor, a data warehouse, or a collection of workflows.

It is a **Sovereign Principal Health Office** for entrepreneurs: a managed health office that continuously remembers the Principal, understands the current health state, manages the next important actions, and learns from real outcomes while preserving Principal sovereignty and clinical authority.

Highest goal:

> **Health Optionality｜长期生命选择权**

Product promise:

> **Maximum Sovereignty × Minimum Management**

MVP venture thesis:

> If one standard product can serve Principal #000, #001 and #002 with the same Product Kernel, the same Case Engine and the same Blueprint contract, while only changing context/configuration and never forking customer-specific code, Yuanli Health has crossed from founder-specific system to repeatable product.

Primary proof:

> **One Product × Three Principals × Zero Fork**

---

## 1. Strategic Problem

The customer problem is not lack of health data. The customer problem is fragmentation, reset cost, and management burden.

A high-agency entrepreneur may already have Apple Health, medical reports, clinicians, fitness support, nutrition information and AI. Yet no single system continuously knows:

- what this person is optimizing life for;
- what is truly happening now;
- what matters most now;
- what has already been tried;
- who owns the next action;
- what actually happened;
- what should be learned and reused.

Therefore the category is not “AI Health Assistant”. The category is:

> **Sovereign Principal Health Office｜企业家的主权私人健康办公室**

The product must reduce Principal management burden while increasing decision quality, continuity and long-term optionality.

---

## 2. Product Constitution

The following rules are normative for `YH Managed v0.1`.

### C01｜Health Optionality is the crown goal
Local metric optimization must never silently outrank whole-life function and long-term optionality.

### C02｜Principal owns intent and final authorization
Life goals, value ordering, risk preference and major health choices remain with the Principal.

### C03｜Clinical authority remains clinical
AI may organize evidence, identify gaps and propose candidate interpretations/actions; diagnosis, prescription and medical treatment decisions requiring clinical judgment remain with qualified clinicians.

### C04｜The Principal must not become the health project manager
The system and Health Steward own continuity, follow-up and closure; the Principal is asked only for decisions that genuinely require Principal authority.

### C05｜Evidence ≠ Interpretation ≠ Decision ≠ Action ≠ Outcome
The product must preserve these layers explicitly. No layer may silently upgrade itself into the next.

### C06｜One Product Kernel, no customer-specific fork
Customer differences must be expressed as context, configuration, permissions, evidence and Case data. `if principal == Ray` is forbidden in Product Kernel logic.

### C07｜One Case Engine, many Blueprints
Sleep, metabolic health, clinical follow-up and future domains must run on one Case Engine. A domain-specific Blueprint may vary; the Product Kernel may not fork.

### C08｜Managed closure before automation
Human Steward action is a first-class product capability. Automation is added only when it improves outcome, burden, replication or safety.

### C09｜Learning requires Reality
Advice saved in a note is not Learning. Learning requires observed Outcome and explicit adjudication; reusable compounding additionally requires later pre-task reuse.

### C10｜Infrastructure is replaceable
Supabase, OpenAI, n8n, Ego, Hugging Face, Notion or any future runtime are implementation adapters, not the product definition or health truth.

---

## 3. Product Surface

The external product for the MVP is exactly one offer:

# `YH Managed Health Office v0.1`

It delivers four customer-facing capabilities:

1. **REMEMBER｜永远记得我**
   - preserve longitudinal health history and decision history;
   - reduce repeated explanation and reset cost.

2. **UNDERSTAND｜持续懂我现在发生了什么**
   - form a Current Health Thesis from authorized evidence;
   - distinguish known, unknown, conflict and uncertainty;
   - identify the 1–3 priorities that actually matter.

3. **MANAGE｜替我把事情持续推进**
   - create and track actions;
   - coordinate Steward / Principal / clinician;
   - follow up until closure or explicit blockage.

4. **LEARN｜越来越知道什么对我有效**
   - settle outcomes;
   - adjudicate supported / unsupported / mixed / inconclusive / not_observed / refuted;
   - carry applicable learnings into future Cases.

---

## 4. Roles and Authority

### Principal
Owns life intent, final sovereignty, risk preference, consent, major choices and approvals requiring Principal authority.

### AI Health Brain
Owns evidence organization, synthesis, candidate thesis, prioritization support, action preparation and explanation. It does not own medical authority or Product Canon.

### Health Steward
Owns operational continuity, follow-up, coordination, reminders, exception handling and closure. Steward is a permanent product role, not a temporary workaround for weak automation.

### Clinician / Expert
Owns diagnosis, prescription, treatment and other decisions requiring professional clinical authority.

### Product Kernel
Owns product state, Case lifecycle, schema, policy/version references and auditable transitions. It does not own raw medical truth.

---

## 5. Canonical Product Objects

The MVP Product Kernel has ten business objects. New objects require explicit Product Constitution amendment.

1. `Principal`
2. `ProductRelease`
3. `Blueprint`
4. `HealthCase`
5. `EvidenceRef`
6. `HealthThesis`
7. `Battle`
8. `Action`
9. `Outcome`
10. `Learning`

`Receipt` is an audit attachment to significant transitions/actions rather than a separate top-level product domain.

Every Principal-scoped operational record must resolve to:

- `principal_id`
- `case_id` where applicable
- `product_release_id`
- `blueprint_version` where applicable

No implicit “current Ray” context is allowed.

---

## 6. Health Case Engine

All managed health work runs through one standard lifecycle:

`NEW → UNDERSTANDING → PRIORITIZED → ACTIVE → WAITING → OBSERVING → LEARNING → CLOSED`

Exceptional states:

- `BLOCKED`
- `ESCALATED`
- `CANCELLED`

### State semantics

**NEW** — Case instantiated but not yet sufficiently contextualized.

**UNDERSTANDING** — evidence is being gathered/organized; Current Health Thesis is not yet ready.

**PRIORITIZED** — thesis and priority are sufficient to define a Battle and next actions.

**ACTIVE** — one or more approved actions are being managed.

**WAITING** — waiting on Principal, Steward, clinician, external result or time window.

**OBSERVING** — action occurred; system is waiting for or collecting Outcome evidence.

**LEARNING** — Outcome is being adjudicated into a Learning candidate.

**CLOSED** — the Case has an explicit terminal settlement and next-step disposition.

**BLOCKED** — progress cannot continue without a missing dependency; owner and unblock condition must be explicit.

**ESCALATED** — case requires a higher authority, including clinician escalation.

**CANCELLED** — intentionally stopped by authorized decision; reason must be preserved.

No runtime engine may invent alternate customer-specific lifecycle states.

---

## 7. Blueprint Contract

A Blueprint describes **how a class of health problem is managed**, not a customer workflow implementation.

The first and only MVP Blueprint is:

# `BP-SLEEP-001｜Sleep Recovery Blueprint v1`

Every Blueprint must define:

- eligibility and exclusions;
- required and optional Evidence categories;
- minimum evidence sufficiency rule before Thesis formation;
- uncertainty / conflict preservation rule;
- priority and Battle formation rule;
- allowed Action classes;
- Principal / Steward / clinician authority boundaries;
- observation windows;
- stop / escalation rules;
- Outcome settlement vocabulary;
- Learning adjudication rule;
- reuse eligibility rule.

A Blueprint must never contain:

- Principal-specific code;
- raw credentials;
- customer-specific prompts copied as code forks;
- hard-coded personal identifiers;
- infrastructure-vendor-specific node IDs as product semantics.

---

## 8. MVP Action Boundary

`YH Managed v0.1` supports only:

- `READ`
- `PREPARE`

`COMMIT`, `CLINICAL` automation and `DESTRUCTIVE` automation are **not admitted into the MVP product runtime**.

Clinical work may still occur through human clinician participation; the prohibition applies to autonomous product execution, not to access to care.

This keeps the product focused on managed understanding, preparation, coordination and follow-up while the replication thesis is tested.

---

## 9. Product Surfaces

### Principal Surface
Four primary views only:

1. `Today / Decision Cockpit`
   - what matters now;
   - why;
   - what needs Principal decision;
   - what the Health Office is already handling.

2. `My Health`
   - Current Health Thesis;
   - current Battles;
   - meaningful changes / uncertainty.

3. `Cases`
   - all active / waiting / observing / closed Health Cases;
   - owner, next step and closure state.

4. `History & Learning`
   - Evidence → Decision → Action → Outcome → Learning chronology.

### Steward Cockpit
Must show:

- Principals requiring attention;
- Cases blocked or overdue;
- next action owner;
- approvals needed;
- clinical escalations;
- SLA risk;
- closure queue.

### Expert Case Packet
Clinician-facing projection contains only the minimized evidence, question, relevant context, provenance and requested decision needed for professional review.

All three surfaces are projections from one Product Kernel, not parallel truths.

---

## 10. Data and Truth Boundaries

### Health Reality Canon
`Local Health Kernel` remains the owner of raw longitudinal health reality and sensitive local-first evidence where required.

### Operational Product State
`Supabase/PostgreSQL` is the MVP operational state plane for Principal, Case, Action, Outcome, Learning references, events and receipts.

### Product / Law Canon
`GitHub` owns Product Constitution, Blueprint definitions, schemas, policies, release manifests, tests and admission artifacts.

### Intelligence
OpenAI/ChatGPT is the default MVP intelligence provider behind a replaceable interface. Intelligence output is candidate reasoning, not autonomous authority.

### Human Projection
Notion may remain a human projection / research surface. It is not Product Runtime or Product SSOT.

### Integration Adapters
n8n, Ego, Playwright, Hugging Face or future tools may be used when useful, but no adapter may own Case state, Principal identity, health truth or Product Canon.

---

## 11. MVP Technical Boundary

The first product implementation is intentionally constrained to five primary components:

1. `Next.js / PWA` — Principal and Steward product UI.
2. `Supabase` — Auth, PostgreSQL, RLS, operational product state.
3. `Python Worker` — scheduled Case progression, AI calls, reminders and capability dispatch.
4. `OpenAI / ChatGPT` — default reasoning capability via structured interfaces.
5. `GitHub` — Product Canon, Blueprints, schemas, policy and release versioning.

Existing `Local Health Kernel` remains a foundational health-data Canon and is not counted as a new MVP product component.

Explicitly deferred before Principal #003:

- Temporal;
- Cedar;
- Kafka;
- Kubernetes;
- microservice decomposition;
- independent vector database cluster;
- multi-agent swarm runtime;
- native iOS/Watch product rebuild;
- autonomous clinical or destructive browser execution;
- custom model training.

---

## 12. Product Release Contract

The first release is:

# `YH-MANAGED-0.1.0`

Every new HealthCase must pin:

- `product_release_id`
- `blueprint_id`
- `blueprint_version`
- `case_schema_version`
- `authority_policy_version`
- `intelligence_route_version`

Existing in-flight Cases do not silently inherit a new product release. Migration requires explicit migration logic and receipt.

`YH-MANAGED-0.1.0` includes:

- one Product Kernel;
- one Case Engine;
- one Blueprint: `BP-SLEEP-001 v1`;
- READ + PREPARE only;
- one Principal Surface;
- one Steward Cockpit;
- Expert Case Packet projection;
- 30-day Outcome Settlement;
- Learning + first reuse proof.

---

## 13. Replication Gates

### G0｜Product Contract Freeze
PASS when Product Constitution, canonical objects, Case Engine, Blueprint contract, surface contract, technical boundary, release contract and scorecard are human-ratified.

### G1｜Principal #000 — Golden Tenant
Principal #000 is Ray, but Ray must use the standard product exactly as a future customer would.

PASS requires one complete `Sleep Recovery` Case:

`Evidence → Thesis → Battle → Action → Outcome → Learning → Reuse`

Forbidden:

- Ray-specific code;
- private workflow fork;
- dedicated database schema/table solely for Ray;
- hidden manual state that cannot be represented in Product Kernel.

### G2｜Principal #001 — Config-only Replication
The second Principal must be onboarded using the same Product Release and Blueprint.

Allowed change:

- Principal row;
- permissions / consent;
- evidence links;
- configuration;
- Case instance.

Must equal zero:

- customer-specific code;
- copied workflow;
- new customer-specific table;
- customer-specific webhook;
- prompt fork;
- agent fork.

### G3｜Principal #002 — Zero Engineer Touch
A Health Steward must onboard the third Principal without engineering intervention.

Target:

- technical onboarding time `< 60 minutes`, excluding waiting for external clinical records;
- engineering touch `0` during standard onboarding;
- Product Kernel reuse `100%`.

PASS state:

> `ONE_PRODUCT_THREE_PRINCIPALS_ZERO_FORK`

### G4｜N5 Paid Venture Proof
Only after G3 passes, recruit five real paying Principals to evaluate willingness to pay, renewal, referral, Steward capacity and unit economics.

---

## 14. MVP Scorecard

### Safety / sovereignty
- unauthorized clinical action: `0`
- cross-Principal data leakage: `0`
- customer-specific hidden authority bypass: `0`

### Product value
- important active Cases with explicit owner + next step: `≥ 95%`
- completed important Cases with explicit settlement: `≥ 80%`
- Principal management time: `< 30 min / week` target after stabilization
- important judgments traceable to Evidence: `≥ 95%`

### Learning
- completed Case with adjudicated Learning: `≥ 1 per Case` when Outcome is sufficiently observed
- first valid Learning reuse before a future task: required for G1 full compounding PASS

### Replication
- customer-specific code after G0: `0`
- workflow copy required for P001/P002: `0`
- customer-specific table: `0`
- P001 engineering setup: `< 30 min` target
- P002 engineer touch: `0`
- P002 Steward onboarding: `< 60 min`
- Product Kernel reuse: `100%`

### Venture (G4)
- paying Principals: `≥ 5`
- 90-day renewal signal: `≥ 60%`
- referral intent: recorded for every Principal
- Steward time per Principal/week: measured, not assumed
- gross-margin model: measured from real delivery effort, not projected from synthetic runs

---

## 15. 90-Day Program

### Day 0–14｜G0 Freeze
Deliver and ratify:

- `YH-MANAGED-0.1.0` Product Contract;
- canonical objects;
- Case Engine;
- `BP-SLEEP-001 v1`;
- Principal / Steward surface contracts;
- Outcome Settlement contract;
- replication scorecard.

No infrastructure expansion during this phase unless required to make the Product Contract testable.

### Day 15–45｜G1 Golden Tenant
Run Principal #000 through a real 30-day Sleep Recovery Case on the standard Product Kernel.

Primary questions:

- does the office reduce Principal management burden;
- does it correctly identify the important problem;
- do important actions actually close;
- does Reality return;
- is Learning adjudicated;
- does at least one Learning alter a later decision/action.

### Day 46–65｜G2 Config-only Principal #001
Onboard Principal #001 with no product fork. Every discovered need must be classified as either:

- general Product Capability; or
- Principal Configuration.

Customer-specific code is not an allowed third category.

### Day 66–90｜G3 Zero-engineer Principal #002
Health Steward independently onboards and operates Principal #002.

If G3 passes, prepare G4 `N5 Paid` recruitment and commercial test.

---

## 16. Anti-Complexity Constitution

Before any new technology, service, agent, workflow engine or database is admitted, it must materially improve at least one of:

1. Principal Outcome;
2. Principal Management Burden;
3. Replication;
4. Safety / Sovereignty.

If all four are `NO`, the capability is not admitted.

Additional rules before G3:

- no new orchestration framework without observed runtime failure that the current Worker cannot reasonably solve;
- no new AI agent framework solely for architectural elegance;
- no platform may become a second Case state source;
- no customer-specific fork may be accepted as “temporary” without failing the replication Gate;
- no feature ships without a named Product object, user value and acceptance evidence.

---

## 17. Relationship to Existing YH-CGE1 / REX0 / HF Work

Existing work is retained but demoted to supporting capabilities:

- `YH-CGE1` remains the zero-PHI architecture/eval proof and scientific compounding benchmark.
- `YH-REX0` remains a governed execution capability for cases that need bounded external action.
- `YH-HF0` remains an Intelligence Evaluation Plane, not the Product Kernel.
- n8n remains an optional integration/orchestration adapter, not a product dependency.
- Ego remains an optional last-mile browser adapter, not the default execution model.

No existing supporting system is allowed to redefine the Product Constitution.

---

## 18. Final Admission Rule

`YH-STRAT2-G0` may be ratified only if the Principal accepts all of the following as the governing MVP constraints:

1. one product: `YH Managed Health Office v0.1`;
2. one common Case Engine;
3. one initial Blueprint: Sleep Recovery v1;
4. READ + PREPARE only in autonomous product runtime;
5. Health Steward is a first-class product role;
6. Ray is Golden Principal #000, not a special product fork;
7. Principal #001 must be config-only;
8. Principal #002 must be zero-engineer-touch;
9. infrastructure remains subordinate and replaceable;
10. the MVP is judged by customer value + replication + safety, not architecture completeness.

If ratified, the next authorized artifact is an implementation plan. No runtime/database implementation is authorized by this design document alone.

---

## Decision Summary

**Strategic shift:** `Health OS invention → Repeatable Principal Health Office productization`.

**MVP product:** `YH-MANAGED-0.1.0`.

**Core proof:** `One Product × Three Principals × Zero Fork`.

**Golden Case:** `Sleep Recovery`.

**Primary runtime discipline:** `Context varies; Product Kernel does not fork`.

**Next Gate after human ratification:** `YH-STRAT2-G0 Implementation Plan`.
