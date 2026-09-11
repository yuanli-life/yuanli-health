# YH-REX0-R2｜Authenticated Runtime v0.1

Status: `IMPLEMENTATION_SPEC`
Date: `2026-09-11`
Parent: `YH-REX0｜Reality Execution Plane`

## Purpose

R2 upgrades the proven R1 shadow chain from an ephemeral queue into an authenticated, replay-resistant, Principal-isolated runtime with durable receipts. It does not widen clinical authority and does not admit real health data during proof.

## Seven gates

1. **Worker Identity** — every pull/fail/receipt operation is signed by a registered Ed25519 worker key. Only active workers are admitted.
2. **Signed Action Contract** — every Action Contract is signed by a registered Ed25519 issuer. Signature verification covers a canonical JSON representation of the complete contract body.
3. **Nonce / Replay Protection** — contract nonce and `(principal_ref, idempotency_key)` are unique; worker request nonces are one-time and time-bounded.
4. **Principal Isolation** — a worker has an explicit Principal allowlist. Atomic claim may only return contracts for both the requested Principal and the worker's registered scope.
5. **Durable Receipt Projection** — accepted receipts are committed to the controlled Supabase runtime plane and remain independently queryable after n8n is disabled.
6. **Retry / Timeout / Dead Letter** — leases expire; failures become `retry_wait` until `max_attempts`; exhausted or terminal work becomes `dead_letter`; completion is never inferred from workflow success.
7. **Authority Escalation** — runtime policy, not caller text, computes minimum approval roles for each action class.

## Authority matrix

| Action class | Minimum authority | R2 real execution |
|---|---|---|
| `READ` | registered issuer + registered worker + policy/domain scope | Allowed only on synthetic/public fixture |
| `PREPARE` | `steward` approval | Admission logic test only |
| `COMMIT` | `steward + principal` approvals | Never executed in R2 |
| `CLINICAL` | `steward + principal + clinician` approvals | Never executed in R2 |
| `DESTRUCTIVE` | `steward + principal + clinician` approvals + explicit destructive confirmation | Never executed in R2 |

An approval requirement declared by the caller cannot weaken this matrix. Approval receipts are evidence of approval; `requires_approval` alone is not authorization.

## Cryptographic boundary

R2 uses asymmetric Ed25519 keys.

- Issuer private keys remain outside n8n/Supabase and sign Action Contracts.
- Worker private keys remain on the authorized worker device and sign pull/fail/receipt request envelopes.
- Supabase stores only public keys.
- n8n is an orchestrator/relay. It is not trusted to create authority or to validate a health truth.
- Private keys, login credentials, raw Health Canon records and secrets are prohibited from Action Contract payloads and receipts.

Canonical signing bytes are deterministic UTF-8 JSON with object keys sorted recursively and no extra whitespace. The exact algorithm must be implemented identically by issuer, worker and Edge Runtime.

## Runtime topology

```text
Signed Action Contract
        ↓
n8n orchestration
        ↓
YH-REX0 Runtime Edge
  ├─ verify issuer signature
  ├─ authority matrix
  ├─ nonce/idempotency gate
  └─ durable contract queue
        ↓
Signed Worker Pull
        ↓
atomic Principal-scoped lease
        ↓
Local Worker verifies contract signature again
        ↓
Bounded Ego Runner
        ↓
Signed Action Receipt / Failure
        ↓
n8n orchestration
        ↓
YH-REX0 Runtime Edge
        ↓
Supabase durable receipt / retry / dead letter
```

## Durable objects

R2 creates isolated operational tables:

- `yh_rex0_workers`
- `yh_rex0_contract_issuers`
- `yh_rex0_contracts`
- `yh_rex0_worker_nonces`
- `yh_rex0_receipts`
- `yh_rex0_dead_letters`

These tables are Runtime Projection, not Health Canon. RLS is enabled and no user-facing policies are created. Only the service role / R2 Edge Runtime may mutate them.

## State machine

```text
queued
  ↓ claim
leased
  ├─ receipt accepted → completed
  ├─ signed failure → retry_wait → queued/leased
  └─ lease timeout → retry_wait
                     ↓ attempts exhausted
                  dead_letter
```

Terminal states: `completed`, `dead_letter`, `rejected`.

## Hard invariants

- A worker cannot claim a Principal outside its registered scope.
- A contract signature failure is terminal rejection before queue admission.
- The same contract nonce cannot be admitted twice.
- The same Principal idempotency key cannot create a second executable contract.
- A worker request nonce cannot be reused.
- A receipt from a worker other than the current lease owner is rejected.
- A receipt Principal must equal the contract Principal.
- A completed contract cannot be leased again.
- n8n execution success never means health action success.
- No R2 proof contains real clinical data or performs `PREPARE`, `COMMIT`, `CLINICAL`, or `DESTRUCTIVE` world actions.

## R2 proof suite

Required positive proof:

`Signed synthetic READ contract → n8n → Supabase durable queue → signed Principal-A worker pull → local signature verification → Ego public READ → signed receipt → n8n → durable Supabase receipt → completed contract`

Required hard negatives:

1. tampered contract signature rejected;
2. duplicate contract nonce/idempotency rejected;
3. unknown or revoked worker rejected;
4. Worker-B cannot claim Principal-A;
5. reused worker request nonce rejected;
6. wrong-worker receipt rejected;
7. missing authority rejected for PREPARE / COMMIT / CLINICAL / DESTRUCTIVE;
8. timed-out lease becomes retryable and eventually dead-lettered;
9. completed contract cannot be executed twice;
10. durable receipt remains queryable after temporary n8n workflow is disabled.

## R2 PASS definition

`PASS_SHADOW_AUTHENTICATED_RUNTIME` may only be declared after fresh evidence proves every positive and hard-negative case above, all temporary public n8n workflows are disabled, and the durable receipt is queryable from Supabase independently of n8n.

R2 PASS still does **not** authorize real health actions. The next gate is a separately approved low-risk shadow case restricted to public information and Principal confirmation before any commitment.