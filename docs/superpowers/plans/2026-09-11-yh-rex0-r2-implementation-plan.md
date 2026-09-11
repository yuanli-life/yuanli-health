# YH-REX0-R2 Authenticated Runtime Implementation Plan

> Execute with TDD. Do not promote any gate from design to PASS without fresh runtime evidence.

**Goal:** Prove an authenticated, signed, replay-resistant, Principal-isolated `Action Contract → n8n → durable queue → local Ego worker → signed Receipt → durable Supabase projection` shadow loop.

**Architecture:** GitHub defines Law/Schema. n8n remains orchestration. A custom-auth Supabase Edge Runtime verifies Ed25519 signatures and owns durable REX0 state. The local worker keeps its private key and re-verifies the signed Action Contract before bounded Ego execution. No real health data is used.

## Task 1 — Freeze R2 law and RED tests

Create:
- `docs/specs/YH-REX0-R2-AUTHENTICATED-RUNTIME-v0.1.md`
- `tests/test_rex0_crypto.py`
- `tests/test_rex0_authority.py`
- `tests/test_rex0_worker_policy.py`

RED assertions:
- valid Ed25519 signature verifies; tampered body fails;
- authority matrix cannot be weakened by caller fields;
- Worker-B cannot execute/claim Principal-A;
- replayed nonce/idempotency is rejected by runtime integration tests;
- wrong-worker receipt is rejected.

## Task 2 — Local cryptographic and authority kernel

Create:
- `runtime/rex0/__init__.py`
- `runtime/rex0/canonical.py`
- `runtime/rex0/crypto.py`
- `runtime/rex0/authority.py`
- `runtime/rex0/worker_policy.py`

Implementation:
- recursively canonicalize JSON and sign/verify bytes using Ed25519;
- encode public keys/signatures as base64;
- define immutable authority matrix:
  - READ: none
  - PREPARE: steward
  - COMMIT: steward + principal
  - CLINICAL: steward + principal + clinician
  - DESTRUCTIVE: all three + explicit destructive confirmation;
- validate Worker identity, Principal scope, lease/receipt ownership.

Run targeted tests RED → GREEN, then full unit suite.

## Task 3 — Durable Supabase runtime schema

Create migration:
- `supabase/migrations/20260911183000_yh_rex0_r2_authenticated_runtime.sql`

Create isolated runtime tables:
- workers, issuers, contracts, worker nonces, receipts, dead letters.

Requirements:
- RLS on, no anon/authenticated policies;
- unique contract nonce;
- unique `(principal_ref, idempotency_key)`;
- atomic claim with `FOR UPDATE SKIP LOCKED`;
- only registered active Worker scoped to Principal may lease;
- atomic receipt accept transitions leased → completed;
- signed failure/expired lease transitions retry_wait or dead_letter;
- revoke function execution from PUBLIC/anon/authenticated; service_role only.

Apply migration to existing Yuanli Health Supabase project. Query information_schema and function definitions to verify.

## Task 4 — R2 Edge Runtime

Create/deploy:
- `supabase/functions/yh-rex0-runtime/index.ts`

Custom-auth operations:
- `admit_contract`
- `pull`
- `receipt`
- `fail`
- `sweep`
- `heartbeat`

The function must:
- verify issuer/worker Ed25519 signatures;
- consume one-time worker nonces;
- enforce clock-skew window;
- enforce runtime authority matrix;
- preserve Principal isolation;
- use service role only internally;
- never log secrets/private keys/raw health records.

Deploy with `verify_jwt=false` only because function-body custom cryptographic authentication is mandatory for every mutating/worker operation.

## Task 5 — Synthetic identities and registration

Generate locally:
- one issuer keypair;
- Worker-A scoped only to `synthetic-principal-A`;
- Worker-B scoped only to `synthetic-principal-B`.

Never commit private keys. Register only public keys in Supabase.

Write a synthetic signed READ contract for Principal-A against `https://example.com/`.

## Task 6 — n8n R2 shadow orchestrator

Create temporary inactive-first workflow:

`Contract Intake → R2 Edge admit_contract`
`Worker Pull → R2 Edge pull`
`Receipt / Failure → R2 Edge receipt|fail`

No health data. No n8n static queue. No authority stored solely in n8n.

Activate only for bounded proof and deactivate immediately afterward.

## Task 7 — Local authenticated worker

Create:
- `runtime/rex0/worker.py`

Flow:
1. sign pull envelope with Worker private key + fresh nonce/timestamp + requested Principal;
2. send through n8n;
3. verify returned Action Contract issuer signature locally;
4. verify principal scope and action-class support;
5. run existing bounded Ego READ runner;
6. sign Receipt envelope;
7. post Receipt through n8n;
8. do not treat transport/network success as ACT success.

## Task 8 — Positive E2E proof

Fresh run:

`issuer sign → n8n → Edge admission → durable queue → signed Worker-A pull → lease → local verify → Ego example.com READ → signed Receipt → n8n → Edge receipt → durable Supabase row`.

Record exact:
- contract id / nonce / issuer id;
- n8n workflow/version/execution ids;
- worker id and public-key fingerprint only;
- Ego task space/execution id;
- receipt id;
- Supabase contract final state and durable receipt projection.

## Task 9 — Hard negatives

Run and capture evidence for:
- contract tamper;
- duplicate contract replay;
- replayed worker nonce;
- unknown worker;
- revoked worker;
- Worker-B → Principal-A isolation attempt;
- wrong-worker receipt;
- PREPARE missing steward;
- COMMIT missing principal/steward;
- CLINICAL missing clinician/principal/steward;
- DESTRUCTIVE missing all approvals/explicit confirmation;
- lease timeout → retry;
- attempts exhausted → dead letter;
- completed contract cannot lease again.

No negative test may invoke Ego if admission/authority/isolation should have rejected it earlier.

## Task 10 — Independent durability proof and settlement

Deactivate temporary R2 n8n workflow.

Then query Supabase directly and prove:
- contract remains `completed`;
- Receipt remains queryable;
- no second completed Receipt for same contract;
- DLQ/retry fixtures are in expected terminal/intermediate states;
- Worker/Principal scopes remain intact.

Run fresh local unit tests and schema verification.

Create:
- `receipts/yh-rex0/2026-09-11-YH-REX0-R2-AUTHENTICATED-RUNTIME-PROOF.json`
- `docs/receipts/YH-REX0-R2-AUTHENTICATED-RUNTIME-PROOF-2026-09-11.md`

Update Draft PR #8 but keep it Draft. Declare `PASS_SHADOW_AUTHENTICATED_RUNTIME` only if every gate has current evidence.