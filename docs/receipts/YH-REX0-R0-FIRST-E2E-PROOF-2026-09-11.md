# YH-REX0-R0｜First End-to-End World Reality Proof

Status: `PASS_SHADOW_READ_ONLY`

Date: `2026-09-11`

## Proven chain

`Action Contract → n8n Admission Gate → bounded Ego Runner → external public READ → Action Receipt → n8n Receipt Acceptance`

## Exact reality evidence

- n8n instance: `hay2045.app.n8n.cloud`
- n8n workflow: `oRBIb8EfBj6I26os`
- workflow version: `5a258e79-4824-4aa8-b812-0b18c8070a0c`
- contract execution: `1` → `ADMITTED`
- Ego execution: `ego-task-38` / Task Space `38`
- observed page: `https://example.com/`
- observed title: `Example Domain`
- Action Receipt: `RCP-YH-REX0-SMOKE-001` → `COMPLETED`
- receipt execution: `2` → `RECEIPT_ACCEPTED`
- n8n execution history shows five webhook executions, all technically completed.

## Hard negatives

Three additional contracts were intentionally sent to the admission gate and were rejected before Ego execution:

1. `COMMIT_NO_PRINCIPAL` → `REJECTED: R0 only admits READ`
2. `CLINICAL_NO_CLINICIAN` → `REJECTED: R0 only admits READ`
3. `UNSUPPORTED_ACTION` → `REJECTED: unsupported action`

## Authority boundary

This proof used only synthetic/public data. It did not use any real Principal health data, medical record, credential payload, clinical action, form submission, booking, purchase, medication action, or irreversible browser action.

The temporary public webhook was deactivated immediately after proof. Current workflow state: `active=false`.

## What this proves

This proves the first bounded `World Reality` spine for YH-REX0: a typed Action Contract can be admitted by n8n, dispatched to a capability-limited Ego runner, executed against a real external web page, returned as a typed Action Receipt, and accepted back into n8n.

## What this does NOT prove

- production-grade authentication between n8n and the local runner;
- unattended n8n → local Ego transport;
- real health-data handling;
- COMMIT or DESTRUCTIVE actions;
- clinical authority flows;
- Outcome (`OUT`) adjudication;
- Learning (`LRN`) or Task2 reuse;
- YH-HF0 Intelligence Admission integration.

## Next hard gate

`YH-REX0-R1｜Authenticated Queue Bridge × Local Ego Worker × Receipt Projection`

The next proof must remove the human/chat relay between n8n and the local Ego runner, while keeping the same Action Contract, authority gate and Receipt boundary.
