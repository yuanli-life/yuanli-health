import "jsr:@supabase/functions-js/edge-runtime.d.ts";

type Json = null | boolean | number | string | Json[] | { [key: string]: Json };
type RecordJson = Record<string, any>;

const SUPABASE_URL = Deno.env.get("SUPABASE_URL") || "";
const SERVICE_KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY") || "";
const CLOCK_SKEW_MS = 2 * 60 * 1000;
const NONCE_TTL_MS = 5 * 60 * 1000;
const ACTIONS = ["READ", "PREPARE", "COMMIT", "CLINICAL", "DESTRUCTIVE"] as const;

function reply(body: unknown, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" },
  });
}

function canonical(value: any): string {
  if (value === null || typeof value === "boolean" || typeof value === "number" || typeof value === "string") {
    return JSON.stringify(value);
  }
  if (Array.isArray(value)) return `[${value.map(canonical).join(",")}]`;
  if (typeof value === "object") {
    const keys = Object.keys(value).sort();
    return `{${keys.map((key) => `${JSON.stringify(key)}:${canonical(value[key])}`).join(",")}}`;
  }
  throw new Error("non_json_value");
}

function b64Bytes(value: string): Uint8Array {
  const raw = atob(value);
  const out = new Uint8Array(raw.length);
  for (let i = 0; i < raw.length; i += 1) out[i] = raw.charCodeAt(i);
  return out;
}

async function verifyEd25519(publicKeyB64: string, body: unknown, signatureB64: string): Promise<boolean> {
  try {
    const key = await crypto.subtle.importKey("raw", b64Bytes(publicKeyB64), { name: "Ed25519" }, false, ["verify"]);
    return await crypto.subtle.verify(
      { name: "Ed25519" },
      key,
      b64Bytes(signatureB64),
      new TextEncoder().encode(canonical(body)),
    );
  } catch {
    return false;
  }
}

function dbHeaders(extra: Record<string, string> = {}): HeadersInit {
  return {
    apikey: SERVICE_KEY,
    authorization: `Bearer ${SERVICE_KEY}`,
    "content-type": "application/json",
    ...extra,
  };
}

async function dbGet(path: string): Promise<RecordJson[]> {
  const response = await fetch(`${SUPABASE_URL}/rest/v1/${path}`, { headers: dbHeaders() });
  if (!response.ok) throw new Error(`db_get_${response.status}`);
  return await response.json();
}

async function dbInsert(table: string, body: RecordJson): Promise<{ rows: RecordJson[]; status: number; error?: string }> {
  const response = await fetch(`${SUPABASE_URL}/rest/v1/${table}`, {
    method: "POST",
    headers: dbHeaders({ Prefer: "return=representation" }),
    body: JSON.stringify(body),
  });
  const text = await response.text();
  if (!response.ok) return { rows: [], status: response.status, error: text.slice(0, 400) };
  return { rows: text ? JSON.parse(text) : [], status: response.status };
}

async function dbPatch(path: string, body: RecordJson): Promise<void> {
  const response = await fetch(`${SUPABASE_URL}/rest/v1/${path}`, {
    method: "PATCH",
    headers: dbHeaders({ Prefer: "return=minimal" }),
    body: JSON.stringify(body),
  });
  if (!response.ok) throw new Error(`db_patch_${response.status}`);
}

async function rpc(name: string, body: RecordJson): Promise<any> {
  const response = await fetch(`${SUPABASE_URL}/rest/v1/rpc/${name}`, {
    method: "POST",
    headers: dbHeaders(),
    body: JSON.stringify(body),
  });
  const text = await response.text();
  if (!response.ok) throw new Error(`rpc_${name}_${response.status}:${text.slice(0, 240)}`);
  return text ? JSON.parse(text) : null;
}

function inScope(principalRef: string, scopes: unknown): boolean {
  return Array.isArray(scopes) && (scopes.includes(principalRef) || scopes.includes("*"));
}

function requiredRoles(actionClass: string): string[] {
  if (actionClass === "READ") return [];
  if (actionClass === "PREPARE") return ["steward"];
  if (actionClass === "COMMIT") return ["steward", "principal"];
  if (actionClass === "CLINICAL" || actionClass === "DESTRUCTIVE") return ["steward", "principal", "clinician"];
  return ["__invalid_action_class__"];
}

function authorityError(contract: RecordJson): string | null {
  if (!ACTIONS.includes(contract.action_class)) return "invalid_action_class";
  const roles = new Set(
    Array.isArray(contract.approval_receipts)
      ? contract.approval_receipts.filter((x: any) => x && typeof x.actor_role === "string").map((x: any) => x.actor_role)
      : [],
  );
  for (const role of requiredRoles(contract.action_class)) {
    if (!roles.has(role)) return `missing_${role}_approval`;
  }
  if (contract.action_class === "DESTRUCTIVE" && contract?.payload?.destructive_confirmed !== true) {
    return "missing_destructive_confirmation";
  }
  return null;
}

function basicContractError(contract: RecordJson): string | null {
  if (!contract || typeof contract !== "object") return "missing_contract";
  if (typeof contract.contract_id !== "string" || !contract.contract_id.startsWith("ACT-")) return "invalid_contract_id";
  if (typeof contract.principal_ref !== "string" || contract.principal_ref.length < 3) return "invalid_principal_ref";
  if (typeof contract.idempotency_key !== "string" || contract.idempotency_key.length < 8) return "missing_idempotency_key";
  if (contract.receipt_required !== true) return "receipt_required";
  if (contract.revoked === true) return "contract_revoked";
  const expires = Date.parse(String(contract.expires_at || ""));
  if (!Number.isFinite(expires) || expires <= Date.now()) return "contract_expired";
  if (!Array.isArray(contract.allowed_domains) || contract.allowed_domains.length < 1) return "missing_allowed_domains";
  if (!Array.isArray(contract.allowed_actions) || contract.allowed_actions.length < 1) return "missing_allowed_actions";
  return authorityError(contract);
}

async function loadIssuer(issuerId: string): Promise<RecordJson | null> {
  const rows = await dbGet(`yh_rex0_contract_issuers?issuer_id=eq.${encodeURIComponent(issuerId)}&status=eq.active&select=*`);
  return rows[0] || null;
}

async function loadWorker(workerId: string): Promise<RecordJson | null> {
  const rows = await dbGet(`yh_rex0_workers?worker_id=eq.${encodeURIComponent(workerId)}&status=eq.active&select=*`);
  return rows[0] || null;
}

async function admitContract(input: RecordJson): Promise<Response> {
  const { issuer_id, nonce, contract, signature_b64 } = input;
  if (typeof issuer_id !== "string" || typeof nonce !== "string" || typeof signature_b64 !== "string") {
    return reply({ ok: false, error: "invalid_signed_contract_envelope" }, 400);
  }
  const issuer = await loadIssuer(issuer_id);
  if (!issuer) return reply({ ok: false, error: "issuer_not_active" }, 401);
  if (!inScope(contract?.principal_ref, issuer.principal_refs)) return reply({ ok: false, error: "issuer_principal_scope_denied" }, 403);
  const signedBody = { issuer_id, nonce, contract };
  if (!(await verifyEd25519(issuer.public_key_b64, signedBody, signature_b64))) {
    return reply({ ok: false, error: "contract_signature_invalid" }, 401);
  }
  const invalid = basicContractError(contract);
  if (invalid) return reply({ ok: false, error: invalid }, 403);
  const inserted = await dbInsert("yh_rex0_contracts", {
    contract_id: contract.contract_id,
    principal_ref: contract.principal_ref,
    issuer_id,
    nonce,
    idempotency_key: contract.idempotency_key,
    action_class: contract.action_class,
    contract_body: contract,
    issuer_signature_b64: signature_b64,
    state: "queued",
    max_attempts: 3,
    expires_at: contract.expires_at,
  });
  if (inserted.status === 409) return reply({ ok: false, error: "contract_replay_or_idempotency_conflict" }, 409);
  if (inserted.error) return reply({ ok: false, error: "contract_persistence_failed" }, 502);
  return reply({ ok: true, status: "QUEUED_DURABLE", contract_id: contract.contract_id, principal_ref: contract.principal_ref }, 201);
}

async function authenticateWorker(input: RecordJson, expectedOp: string): Promise<{ worker: RecordJson; signed: RecordJson } | Response> {
  const { worker_id, nonce, timestamp, op, principal_ref, body, signature_b64 } = input;
  if ([worker_id, nonce, timestamp, op, signature_b64].some((x) => typeof x !== "string")) {
    return reply({ ok: false, error: "invalid_worker_envelope" }, 400);
  }
  if (op !== expectedOp) return reply({ ok: false, error: "operation_mismatch" }, 400);
  const time = Date.parse(timestamp);
  if (!Number.isFinite(time) || Math.abs(Date.now() - time) > CLOCK_SKEW_MS) {
    return reply({ ok: false, error: "worker_timestamp_out_of_window" }, 401);
  }
  const worker = await loadWorker(worker_id);
  if (!worker) return reply({ ok: false, error: "worker_not_active" }, 401);
  const signed = { worker_id, nonce, timestamp, op, principal_ref: principal_ref ?? null, body: body ?? null };
  if (!(await verifyEd25519(worker.public_key_b64, signed, signature_b64))) {
    return reply({ ok: false, error: "worker_signature_invalid" }, 401);
  }
  if (principal_ref && !inScope(principal_ref, worker.principal_refs)) {
    return reply({ ok: false, error: "worker_principal_scope_denied" }, 403);
  }
  const nonceAccepted = await rpc("yh_rex0_consume_worker_nonce", {
    p_worker_id: worker_id,
    p_nonce: nonce,
    p_expires_at: new Date(time + NONCE_TTL_MS).toISOString(),
  });
  if (nonceAccepted !== true) return reply({ ok: false, error: "worker_nonce_replay" }, 409);
  return { worker, signed };
}

async function workerPull(input: RecordJson): Promise<Response> {
  const auth = await authenticateWorker(input, "pull");
  if (auth instanceof Response) return auth;
  const principal = String(input.principal_ref || "");
  const rows = await rpc("yh_rex0_claim_next", {
    p_worker_id: input.worker_id,
    p_principal_ref: principal,
    p_lease_seconds: 60,
  });
  if (!Array.isArray(rows) || rows.length === 0) return reply({ ok: true, status: "NO_WORK" });
  const row = rows[0];
  return reply({
    ok: true,
    status: "DISPATCH",
    contract_id: row.contract_id,
    principal_ref: row.principal_ref,
    issuer_id: row.issuer_id,
    contract_nonce: row.nonce,
    contract: row.contract_body,
    issuer_signature_b64: row.issuer_signature_b64,
    lease_token: row.lease_token,
    lease_expires_at: row.lease_expires_at,
    attempt_count: row.attempt_count,
    max_attempts: row.max_attempts,
  });
}

async function workerReceipt(input: RecordJson): Promise<Response> {
  const auth = await authenticateWorker(input, "receipt");
  if (auth instanceof Response) return auth;
  const receipt = input?.body?.receipt;
  if (!receipt || typeof receipt !== "object") return reply({ ok: false, error: "missing_receipt" }, 400);
  if (receipt.principal_ref !== input.principal_ref) return reply({ ok: false, error: "receipt_principal_envelope_mismatch" }, 403);
  try {
    const contract = await rpc("yh_rex0_accept_receipt", {
      p_worker_id: input.worker_id,
      p_contract_id: receipt.contract_id,
      p_receipt_id: receipt.receipt_id,
      p_receipt: receipt,
      p_worker_signature_b64: input.signature_b64,
    });
    return reply({ ok: true, status: "RECEIPT_DURABLE", contract_id: receipt.contract_id, receipt_id: receipt.receipt_id, contract_state: contract?.state || "completed" });
  } catch (error) {
    return reply({ ok: false, error: "receipt_rejected", detail: error instanceof Error ? error.message.slice(0, 160) : "unknown" }, 409);
  }
}

async function workerFail(input: RecordJson): Promise<Response> {
  const auth = await authenticateWorker(input, "fail");
  if (auth instanceof Response) return auth;
  const body = input.body || {};
  try {
    const contract = await rpc("yh_rex0_record_failure", {
      p_worker_id: input.worker_id,
      p_contract_id: body.contract_id,
      p_error_class: String(body.error_class || "WORKER_FAILURE"),
      p_error_detail: typeof body.error_detail === "string" ? body.error_detail.slice(0, 500) : null,
    });
    return reply({ ok: true, status: contract?.state || "retry_wait", contract_id: body.contract_id, attempt_count: contract?.attempt_count });
  } catch (error) {
    return reply({ ok: false, error: "failure_report_rejected", detail: error instanceof Error ? error.message.slice(0, 160) : "unknown" }, 409);
  }
}

async function workerSweep(input: RecordJson): Promise<Response> {
  const auth = await authenticateWorker(input, "sweep");
  if (auth instanceof Response) return auth;
  const result = await rpc("yh_rex0_sweep_expired_leases", {});
  return reply({ ok: true, status: "SWEEP_COMPLETE", result });
}

async function workerHeartbeat(input: RecordJson): Promise<Response> {
  const auth = await authenticateWorker(input, "heartbeat");
  if (auth instanceof Response) return auth;
  await dbPatch(`yh_rex0_workers?worker_id=eq.${encodeURIComponent(input.worker_id)}`, { last_seen_at: new Date().toISOString() });
  return reply({ ok: true, status: "HEARTBEAT_ACCEPTED", worker_id: input.worker_id });
}

Deno.serve(async (request: Request) => {
  if (request.method !== "POST") return reply({ ok: false, error: "method_not_allowed" }, 405);
  if (!SUPABASE_URL || !SERVICE_KEY) return reply({ ok: false, error: "runtime_unavailable" }, 503);
  let input: RecordJson;
  try { input = await request.json(); } catch { return reply({ ok: false, error: "invalid_json" }, 400); }
  try {
    switch (input.op) {
      case "admit_contract": return await admitContract(input);
      case "pull": return await workerPull(input);
      case "receipt": return await workerReceipt(input);
      case "fail": return await workerFail(input);
      case "sweep": return await workerSweep(input);
      case "heartbeat": return await workerHeartbeat(input);
      default: return reply({ ok: false, error: "unknown_operation" }, 400);
    }
  } catch (error) {
    console.error("yh-rex0-runtime", error instanceof Error ? error.message : "unknown");
    return reply({ ok: false, error: "runtime_error" }, 500);
  }
});