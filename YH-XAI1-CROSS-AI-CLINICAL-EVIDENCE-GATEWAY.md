# YH-XAI1｜Cross-AI Clinical Evidence Gateway

Status: `IMPLEMENTED_CANDIDATE`

Date: `2026-09-09`

## 1. Purpose

YH-XAI1 makes reviewed health evidence portable across AI environments without creating a second Health Canon.

It exists so ChatGPT, Claude, Gemini, Dify, Codex, future models, or a private agent can retrieve the same governed health context instead of each maintaining its own private copy of the person.

> **One Health Evidence Plane → Many AI Surfaces**

## 2. Constitutional alignment

YH-XAI1 inherits `YH2-C1-HEALTH-CONSTITUTION.md`:

- the Principal retains final authority;
- `Data ≠ Diagnosis`;
- `Knowledge ≠ Authority`;
- `Intelligence ≠ Authority`;
- the gateway is a projection, never the upstream clinical Canon;
- stronger models do not automatically gain broader data access.

## 3. Evidence model

The gateway preserves authority separation instead of flattening all health content into generic RAG chunks.

```text
Health Canon / source evidence
        ↓
health_sources
        ├─ health_observations   # measured/report facts
        ├─ health_findings       # reviewed report findings
        ├─ health_opinions       # clinician/report/AI opinions
        ├─ health_actions        # recommendations / authorized actions
        └─ health_evidence_chunks
             # de-identified transcript/report context with source locators
        ↓
YH-XAI1 Evidence Pack
        ↓
ChatGPT / Claude / Gemini / Dify / Codex / other clients
```

The gateway MUST NOT silently promote clinician opinion into observation, AI synthesis into diagnosis, or recommendation into user-authorized action.

## 4. `health_evidence_chunks`

YH-XAI1 adds a de-identified evidence-chunk projection for source-level context that structured observations alone cannot preserve.

Each chunk includes:

- `source_id`
- `event_date`
- `domain`
- `topic`
- `content_kind`
- `quote_fidelity`
- `speaker_role`
- optional transcript `start_seconds` / `end_seconds`
- `authority_class`
- `privacy_class`
- `review_status`
- provenance / source locator

Allowed fidelity states:

```text
verbatim
near_verbatim
summary
```

A model must be able to distinguish an exact/near-exact transcript excerpt from a summary.

## 5. Retrieval contract

Runtime function:

`health_xai1_search(query, domains, source_kinds, limit)`

The search plane returns heterogeneous evidence objects in one stable envelope while preserving each object type and authority:

- `observation`
- `finding`
- `opinion`
- `evidence_chunk`

Each item returns source identity, date, issuer, domain/topic, authority class, review status, content, provenance/locator, and retrieval score.

## 6. Cross-AI gateway

Production Edge Function:

`yh-xai1-clinical-evidence-gateway`

Request body:

```json
{
  "query": "铁蛋白",
  "domains": ["iron", "liver"],
  "source_kinds": ["checkup_report", "clinician_consult"],
  "limit": 12
}
```

Response contract:

`YH-XAI1/EvidencePack@1`

The response contains:

- query/filter echo;
- authority rules;
- coverage counts;
- source keys;
- typed evidence objects;
- provenance locators.

The endpoint requires a valid authenticated user JWT and separately checks that the user is an enabled Health Principal. It does not expose direct table access.

## 7. Privacy and security

- Raw direct identifiers are not copied into YH-XAI1 chunks.
- Evidence chunks are `P2` projection data unless explicitly reclassified.
- Direct `anon` / `authenticated` table access is denied.
- Retrieval RPC is executable only by `service_role`; callers go through the authenticated gateway.
- The Edge Function uses JWT verification plus Principal allow-list verification.
- `cache-control: no-store` is required for returned clinical evidence.

## 8. Initial runtime settlement

At initial implementation, the existing reviewed clinical evidence plane contained:

- prior checkup and lab reports;
- two clinician consultations from 2026-08-08;
- reproductive-health laboratory evidence from 2026-08-28;
- the 2026-08-29 follow-up checkup.

YH-XAI1 additionally admitted the 2026-09-09 clinician consultation as a governed `clinician_consult` projection and created timestamped/de-identified evidence chunks for the three consultation sessions plus source-level checkup context.

Important epistemic behavior is preserved: different clinician opinions remain separate. For example, a later clinician opinion about elevated ferritin is stored as a clinician opinion rather than overwriting report recommendations or earlier evidence.

## 9. Reality gates

YH-XAI1 is `PASS` only when all are true:

1. a reviewed source is traceable to its Canon reference;
2. a keyword query returns both structured facts and relevant clinician context when available;
3. evidence types remain distinguishable;
4. transcript chunks expose locator/fidelity metadata;
5. unauthenticated direct table access remains unavailable;
6. the gateway requires authenticated Principal access;
7. no model can write clinical Canon through the gateway.

## 10. Next gate

`YH-XAI1-G2｜External AI Client Reality Proof`

Run the same Golden Queries from at least two independent AI environments and compare:

- evidence recall;
- source attribution;
- opinion/fact separation;
- conflict preservation;
- answer consistency;
- privacy leakage.

The target is not identical prose. The target is **the same governed evidence substrate under different models**.
