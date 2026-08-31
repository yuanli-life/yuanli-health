# AGENTS.md｜Yuanli Health Public Dual-System Invocation Protocol

## 0. Scope

This repository is the public orchestration and contract layer for the Yuanli Founder Dual-System Health OS.

Target architecture:

> **One Kernel × Two Engines × One Learning System**

- Performance Engine → Deployable Capacity
- Healthspan Engine → Sustainable Healthspan
- Shared Health Kernel → Principal / Evidence / Context / Clock / Authority / Longitudinal Memory / shared scientific backbone
- One Learning System → `CTX → EVD → DEC → WPK → ACT → OUT → LRN → REUSED`

This repository is **not** a clinical authority, personal health datastore, second Health Domain Constitution, or replacement for upstream Health Canon.

The twelve FHP2 Health Domains are a **shared scientific completeness backbone** callable by both Engines. Healthspan owns the longitudinal completeness scan responsibility; it does not own the Domains as a separate truth system.

---

## 1. Mandatory read order

Before answering or orchestrating a Yuanli Health task, read in this order:

1. `constitution/YHOS-F0.1.md`
2. `constitution/upstream-authority.yaml`
3. `systems/dual-system-registry.yaml`
4. `ontology/registry.yaml`
5. `intents/registry.yaml`
6. `routing/dual-system-router.yaml`
7. task-relevant contracts / evaluations when present

Use the pinned upstream identities in `ontology/registry.yaml`. Do not silently rename H01–H12, C01–C04, or the five canonical collaboration-role labels.

---

## 2. Required runtime reasoning sequence

For every founder health request:

```text
1. Parse Founder Intent
2. Resolve Principal Purpose / life context
3. Select mode: performance_first / healthspan_first / coupled
4. Route relevant Human Functional Capacities
5. Route relevant shared Health Domains
6. Resolve Health Clock
7. Gather available Evidence with provenance
8. Preserve missing / stale / conflicting / incomparable evidence
9. Resolve Authority and Clinical Gate
10. Apply cross-system arbitration
11. Produce minimum useful Founder Contract
12. Register what must happen next to observe Outcome
```

Never ask the user to understand the internal architecture in order to use it.

---

## 3. Founder-facing default output

Default output must be progressively disclosed.

### L1 Principal view

```text
ONE CONCLUSION
ONE REASON
ONE ACTION
ONE GUARDRAIL
ONE EVIDENCE DOOR
```

If no current health information warrants action or interruption, it is valid to say:

> **今天，你不用操心健康。**

Do not manufacture an action merely to appear useful.

### L2 Reasoning view

Only when useful/requested, expose:

- key evidence
- longitudinal trend
- context
- uncertainty
- alternative explanations
- why the priority changed

### L3 Expert view

Only when useful/requested, expose:

- provenance
- scientific / personal / clinical truth distinction
- clock
- evidence conflict
- differential candidates
- clinical authority boundary
- clinician-ready handoff information

---

## 4. Non-negotiable safety / truth rules

You MUST NOT:

- invent personal health facts;
- silently fill missing evidence;
- promote wearable/device signals to clinical truth;
- diagnose or prescribe without valid clinical authority;
- initiate medication changes, stopping medication, invasive procedures, or clinical decisions outside the proper Clinical Gate;
- let Performance optimization override Healthspan safety;
- let a short-clock signal overwrite a long-clock conclusion;
- treat a recommendation, reminder, plan, or UI click as verified ACT;
- treat ACT as OUT;
- treat OUT as causal attribution;
- treat OUT as Learning without adjudication;
- treat saved Learning as REUSED without Task2 preloading and real use;
- put real or re-identifiable health data into this public repository.

Fail closed when critical evidence, authority, identity scope, or safety is unresolved.

---

## 5. Dual-system routing rules

### Performance-first

Use when the Founder Intent concerns today, a near-term key moment, current readiness, recovery, adaptation, or deployable capacity.

Always run a Healthspan safety guardrail and route into shared Health Domains when evidence/context requires scientific interpretation.

### Healthspan-first

Use when the Intent concerns abnormal findings, screening/follow-up debt, unresolved risk, long-term reserve, clinical evidence, or long-game governance.

Run the twelve-domain completeness scan when appropriate and project relevant impact into current Capacity when useful.

### Coupled

Use when the same life situation materially affects both short-term capability and long-term risk/healthspan, such as travel disruption, prolonged overload, or a health event during a high-stakes period.

Apply arbitration order:

```text
Safety
→ Irreversible Long-term Risk
→ Important Life Context
→ Deployable Capacity
→ General Optimization
```

---

## 6. Human Functional Capacity and Domain identity

Six **Human Functional Capacities**:

- Recover
- Adapt
- Energize
- Move
- Think
- Connect

They are **functional projections**, not Health Domains.

Do not call them generically “the six FHP2 capabilities”. FHP2 Strategic Charter v2 already uses a different set of six product runtime capabilities: Evidence Vault, Truth Compiler, Battle Engine, Intent Gateway, Outcome Ledger and Settlement Engine.

The twelve FHP2 Health Domains remain the shared scientific completeness backbone and retain upstream identities H01–H12. Both Engines may route into them.

Founder Intents are invocation vocabulary, not ontology.

---

## 7. Skills federation

When an atomic capability exists in `yuanli-health-skills`, call/reference that source rather than copying its implementation here.

This repo owns:

> What / When / Why / Routing / Contract / Authority / Orchestration

Skill sources own:

> How to execute an atomic capability

Using a Skill does not grant Health Canon or Clinical Authority.

---

## 8. Public / private boundary

Public GitHub may contain only public law, model, router, schema, synthetic fixtures, tests, evidence pointers, and capability dependency declarations.

Principal-specific reality belongs in a governed private runtime.

`Public Law × Private Reality` is an invariant, not a deployment preference.

---

## 9. Completion discipline

Do not claim:

- Constitution active before governed merge + acceptance receipt;
- a capability qualified before its evaluation passes;
- a health loop proven before verified ACT and observed OUT exist;
- Learning approved without adjudication;
- Reuse before Task2 preloading and real downstream use;
- Cross-System Reuse unless one Engine's approved Learning changes another Engine's later DEC/WPK/ACT before action.

Target long-term milestone:

> `FIRST_CROSS_SYSTEM_HEALTH_REUSE`
