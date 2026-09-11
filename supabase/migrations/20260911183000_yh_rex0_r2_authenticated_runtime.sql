create extension if not exists pgcrypto;

create table if not exists public.yh_rex0_workers (
  worker_id text primary key,
  display_name text not null,
  public_key_b64 text not null,
  public_key_fingerprint text not null unique,
  principal_refs text[] not null,
  status text not null default 'active' check (status in ('active','revoked')),
  max_action_class text not null default 'READ' check (max_action_class in ('READ','PREPARE','COMMIT','CLINICAL','DESTRUCTIVE')),
  registered_at timestamptz not null default now(),
  last_seen_at timestamptz,
  metadata jsonb not null default '{}'::jsonb,
  check (cardinality(principal_refs) > 0)
);

create table if not exists public.yh_rex0_contract_issuers (
  issuer_id text primary key,
  display_name text not null,
  public_key_b64 text not null,
  public_key_fingerprint text not null unique,
  principal_refs text[] not null,
  status text not null default 'active' check (status in ('active','revoked')),
  registered_at timestamptz not null default now(),
  metadata jsonb not null default '{}'::jsonb,
  check (cardinality(principal_refs) > 0)
);

create table if not exists public.yh_rex0_contracts (
  contract_id text primary key,
  principal_ref text not null,
  issuer_id text not null references public.yh_rex0_contract_issuers(issuer_id),
  nonce text not null unique,
  idempotency_key text not null,
  action_class text not null check (action_class in ('READ','PREPARE','COMMIT','CLINICAL','DESTRUCTIVE')),
  contract_body jsonb not null,
  issuer_signature_b64 text not null,
  state text not null default 'queued' check (state in ('queued','leased','retry_wait','completed','dead_letter','rejected')),
  attempt_count integer not null default 0 check (attempt_count >= 0),
  max_attempts integer not null default 3 check (max_attempts between 1 and 10),
  lease_owner text references public.yh_rex0_workers(worker_id),
  lease_token uuid,
  lease_expires_at timestamptz,
  next_attempt_at timestamptz not null default now(),
  expires_at timestamptz not null,
  last_error_class text,
  last_error_detail text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (principal_ref, idempotency_key)
);

create index if not exists yh_rex0_contracts_dispatch_idx
  on public.yh_rex0_contracts (principal_ref, state, next_attempt_at, created_at);

create table if not exists public.yh_rex0_worker_nonces (
  worker_id text not null references public.yh_rex0_workers(worker_id),
  nonce text not null,
  used_at timestamptz not null default now(),
  expires_at timestamptz not null,
  primary key (worker_id, nonce)
);

create table if not exists public.yh_rex0_receipts (
  receipt_id text primary key,
  contract_id text not null references public.yh_rex0_contracts(contract_id),
  principal_ref text not null,
  worker_id text not null references public.yh_rex0_workers(worker_id),
  receipt jsonb not null,
  worker_signature_b64 text not null,
  status text not null check (status in ('COMPLETED','FAILED','REJECTED')),
  created_at timestamptz not null default now()
);

create unique index if not exists yh_rex0_one_completed_receipt_per_contract
  on public.yh_rex0_receipts (contract_id)
  where status = 'COMPLETED';

create table if not exists public.yh_rex0_dead_letters (
  dead_letter_id uuid primary key default gen_random_uuid(),
  contract_id text not null unique references public.yh_rex0_contracts(contract_id),
  principal_ref text not null,
  worker_id text references public.yh_rex0_workers(worker_id),
  error_class text not null,
  error_detail text,
  attempt_count integer not null,
  created_at timestamptz not null default now()
);

alter table public.yh_rex0_workers enable row level security;
alter table public.yh_rex0_contract_issuers enable row level security;
alter table public.yh_rex0_contracts enable row level security;
alter table public.yh_rex0_worker_nonces enable row level security;
alter table public.yh_rex0_receipts enable row level security;
alter table public.yh_rex0_dead_letters enable row level security;

create or replace function public.yh_rex0_consume_worker_nonce(
  p_worker_id text,
  p_nonce text,
  p_expires_at timestamptz
) returns boolean
language plpgsql
security definer
set search_path = public
as $$
declare
  v_rows integer;
begin
  if not exists (
    select 1 from public.yh_rex0_workers
    where worker_id = p_worker_id and status = 'active'
  ) then
    return false;
  end if;

  delete from public.yh_rex0_worker_nonces where expires_at < now();

  insert into public.yh_rex0_worker_nonces(worker_id, nonce, expires_at)
  values (p_worker_id, p_nonce, p_expires_at)
  on conflict do nothing;
  get diagnostics v_rows = row_count;
  return v_rows = 1;
end;
$$;

create or replace function public.yh_rex0_claim_next(
  p_worker_id text,
  p_principal_ref text,
  p_lease_seconds integer default 60
) returns setof public.yh_rex0_contracts
language plpgsql
security definer
set search_path = public
as $$
declare
  v_contract_id text;
begin
  if p_lease_seconds < 5 or p_lease_seconds > 900 then
    raise exception 'invalid_lease_seconds';
  end if;

  if not exists (
    select 1 from public.yh_rex0_workers
    where worker_id = p_worker_id
      and status = 'active'
      and p_principal_ref = any(principal_refs)
  ) then
    raise exception 'worker_not_authorized_for_principal';
  end if;

  select c.contract_id into v_contract_id
  from public.yh_rex0_contracts c
  where c.principal_ref = p_principal_ref
    and c.state in ('queued','retry_wait')
    and c.next_attempt_at <= now()
    and c.expires_at > now()
    and c.attempt_count < c.max_attempts
  order by c.created_at
  for update skip locked
  limit 1;

  if v_contract_id is null then
    return;
  end if;

  update public.yh_rex0_contracts
  set state = 'leased',
      lease_owner = p_worker_id,
      lease_token = gen_random_uuid(),
      lease_expires_at = now() + make_interval(secs => p_lease_seconds),
      attempt_count = attempt_count + 1,
      updated_at = now()
  where contract_id = v_contract_id;

  return query
  select * from public.yh_rex0_contracts where contract_id = v_contract_id;
end;
$$;

create or replace function public.yh_rex0_accept_receipt(
  p_worker_id text,
  p_contract_id text,
  p_receipt_id text,
  p_receipt jsonb,
  p_worker_signature_b64 text
) returns public.yh_rex0_contracts
language plpgsql
security definer
set search_path = public
as $$
declare
  v_contract public.yh_rex0_contracts;
begin
  select * into v_contract
  from public.yh_rex0_contracts
  where contract_id = p_contract_id
  for update;

  if not found then raise exception 'contract_not_found'; end if;
  if v_contract.state <> 'leased' then raise exception 'contract_not_leased'; end if;
  if v_contract.lease_owner is distinct from p_worker_id then raise exception 'wrong_lease_owner'; end if;
  if v_contract.lease_expires_at is null or v_contract.lease_expires_at <= now() then raise exception 'lease_expired'; end if;
  if p_receipt->>'principal_ref' is distinct from v_contract.principal_ref then raise exception 'principal_mismatch'; end if;
  if p_receipt->>'contract_id' is distinct from v_contract.contract_id then raise exception 'contract_mismatch'; end if;
  if p_receipt->>'status' <> 'COMPLETED' then raise exception 'receipt_not_completed'; end if;

  insert into public.yh_rex0_receipts(
    receipt_id, contract_id, principal_ref, worker_id, receipt, worker_signature_b64, status
  ) values (
    p_receipt_id, p_contract_id, v_contract.principal_ref, p_worker_id, p_receipt, p_worker_signature_b64, 'COMPLETED'
  );

  update public.yh_rex0_contracts
  set state = 'completed',
      lease_owner = null,
      lease_token = null,
      lease_expires_at = null,
      updated_at = now()
  where contract_id = p_contract_id
  returning * into v_contract;

  return v_contract;
end;
$$;

create or replace function public.yh_rex0_record_failure(
  p_worker_id text,
  p_contract_id text,
  p_error_class text,
  p_error_detail text default null
) returns public.yh_rex0_contracts
language plpgsql
security definer
set search_path = public
as $$
declare
  v_contract public.yh_rex0_contracts;
  v_delay integer;
begin
  select * into v_contract
  from public.yh_rex0_contracts
  where contract_id = p_contract_id
  for update;

  if not found then raise exception 'contract_not_found'; end if;
  if v_contract.state <> 'leased' then raise exception 'contract_not_leased'; end if;
  if v_contract.lease_owner is distinct from p_worker_id then raise exception 'wrong_lease_owner'; end if;

  if v_contract.attempt_count >= v_contract.max_attempts then
    insert into public.yh_rex0_dead_letters(contract_id, principal_ref, worker_id, error_class, error_detail, attempt_count)
    values (v_contract.contract_id, v_contract.principal_ref, p_worker_id, p_error_class, p_error_detail, v_contract.attempt_count)
    on conflict (contract_id) do nothing;

    update public.yh_rex0_contracts
    set state = 'dead_letter',
        lease_owner = null,
        lease_token = null,
        lease_expires_at = null,
        last_error_class = p_error_class,
        last_error_detail = p_error_detail,
        updated_at = now()
    where contract_id = p_contract_id
    returning * into v_contract;
  else
    v_delay := least(300, (5 * power(2, greatest(v_contract.attempt_count - 1, 0)))::integer);
    update public.yh_rex0_contracts
    set state = 'retry_wait',
        lease_owner = null,
        lease_token = null,
        lease_expires_at = null,
        next_attempt_at = now() + make_interval(secs => v_delay),
        last_error_class = p_error_class,
        last_error_detail = p_error_detail,
        updated_at = now()
    where contract_id = p_contract_id
    returning * into v_contract;
  end if;

  return v_contract;
end;
$$;

create or replace function public.yh_rex0_sweep_expired_leases()
returns table(retried integer, dead_lettered integer)
language plpgsql
security definer
set search_path = public
as $$
declare
  v_retried integer := 0;
  v_dead integer := 0;
begin
  insert into public.yh_rex0_dead_letters(contract_id, principal_ref, worker_id, error_class, error_detail, attempt_count)
  select contract_id, principal_ref, lease_owner, 'LEASE_TIMEOUT', 'lease expired after max attempts', attempt_count
  from public.yh_rex0_contracts
  where state = 'leased'
    and lease_expires_at <= now()
    and attempt_count >= max_attempts
  on conflict (contract_id) do nothing;
  get diagnostics v_dead = row_count;

  update public.yh_rex0_contracts
  set state = 'dead_letter',
      lease_owner = null,
      lease_token = null,
      lease_expires_at = null,
      last_error_class = 'LEASE_TIMEOUT',
      last_error_detail = 'lease expired after max attempts',
      updated_at = now()
  where state = 'leased'
    and lease_expires_at <= now()
    and attempt_count >= max_attempts;

  update public.yh_rex0_contracts
  set state = 'retry_wait',
      lease_owner = null,
      lease_token = null,
      lease_expires_at = null,
      next_attempt_at = now() + interval '5 seconds',
      last_error_class = 'LEASE_TIMEOUT',
      last_error_detail = 'lease expired; retry scheduled',
      updated_at = now()
  where state = 'leased'
    and lease_expires_at <= now()
    and attempt_count < max_attempts;
  get diagnostics v_retried = row_count;

  return query select v_retried, v_dead;
end;
$$;

revoke all on public.yh_rex0_workers from anon, authenticated;
revoke all on public.yh_rex0_contract_issuers from anon, authenticated;
revoke all on public.yh_rex0_contracts from anon, authenticated;
revoke all on public.yh_rex0_worker_nonces from anon, authenticated;
revoke all on public.yh_rex0_receipts from anon, authenticated;
revoke all on public.yh_rex0_dead_letters from anon, authenticated;

revoke execute on function public.yh_rex0_consume_worker_nonce(text,text,timestamptz) from public, anon, authenticated;
revoke execute on function public.yh_rex0_claim_next(text,text,integer) from public, anon, authenticated;
revoke execute on function public.yh_rex0_accept_receipt(text,text,text,jsonb,text) from public, anon, authenticated;
revoke execute on function public.yh_rex0_record_failure(text,text,text,text) from public, anon, authenticated;
revoke execute on function public.yh_rex0_sweep_expired_leases() from public, anon, authenticated;

grant execute on function public.yh_rex0_consume_worker_nonce(text,text,timestamptz) to service_role;
grant execute on function public.yh_rex0_claim_next(text,text,integer) to service_role;
grant execute on function public.yh_rex0_accept_receipt(text,text,text,jsonb,text) to service_role;
grant execute on function public.yh_rex0_record_failure(text,text,text,text) to service_role;
grant execute on function public.yh_rex0_sweep_expired_leases() to service_role;