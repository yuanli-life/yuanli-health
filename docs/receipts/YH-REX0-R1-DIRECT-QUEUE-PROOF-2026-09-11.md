# YH-REX0-R1｜Direct n8n Queue → Ego → Receipt Proof

Status: `PASS_SHADOW_DIRECT_QUEUE`

Date: `2026-09-11`

## Proven chain

`Action Contract → n8n queue → local worker pull → bounded Ego runner → Action Receipt → n8n receipt store`

This proof removed the chat-mediated handoff between n8n admission and Ego execution. A one-shot local worker performed the complete transport sequence after it was started.

## Exact evidence

- n8n workflow: `eTQuQj690rcvYj1f`
- workflow version: `f9f332bf-a169-4d41-8e02-e7348a86e5e6`
- queue execution: `6` → `QUEUED`
- pull execution: `7` → `DISPATCH`
- Action Contract: `ACT-YH-REX0-R1-DIRECT-001`
- Ego execution: `ego-task-45`, Task Space `45`
- observed page: `https://example.com/`
- observed title: `Example Domain`
- Receipt: `RCP-YH-REX0-R1-DIRECT-001` → `COMPLETED`
- receipt-store execution: `8` → `RECEIPT_STORED`
- temporary queue workflow was deactivated immediately after proof (`active=false`).

## Authority and privacy boundary

This was a synthetic/public READ-only proof. No real Principal health data, clinical decision, hospital portal, credential payload, form submission, booking, purchase, medication action or irreversible action was used.

## Interpretation

R0 proved that n8n could admit a typed contract and later accept a typed receipt. R1 additionally proves that a local worker can autonomously pull the admitted work from n8n, invoke the bounded Ego capability, and return the receipt to n8n without a human/chat relay between those steps.

## Remaining boundary

The R1 bridge uses an ephemeral shadow queue and temporary public webhook paths. It is **not** production-grade authentication. Real Principal data remains prohibited.

## Next hard gate

`YH-REX0-R2｜Authenticated Queue Bridge × Durable Receipt Projection × Principal Isolation`

Required before any real health action:

1. authenticated worker identity;
2. signed/nonce-protected Action Contract transport;
3. durable controlled Receipt projection;
4. per-Principal isolation and leakage hard negatives;
5. replay/idempotency controls;
6. dead-letter / timeout / retry semantics;
7. no real clinical action until the Clinical Authority Gate is independently proven.
