create or replace function public.yh_rex0_action_rank(p_action_class text)
returns integer
language sql
immutable
strict
set search_path = public
as $$
  select case p_action_class
    when 'READ' then 0
    when 'PREPARE' then 1
    when 'COMMIT' then 2
    when 'CLINICAL' then 3
    when 'DESTRUCTIVE' then 4
    else -1
  end;
$$;

alter table public.yh_rex0_contracts
  add constraint yh_rex0_contract_body_identity_check
  check (
    contract_body->>'contract_id' = contract_id
    and contract_body->>'principal_ref' = principal_ref
    and contract_body->>'action_class' = action_class
    and contract_body->>'idempotency_key' = idempotency_key
  ) not valid;

alter table public.yh_rex0_contracts
  validate constraint yh_rex0_contract_body_identity_check;

alter table public.yh_rex0_receipts
  add constraint yh_rex0_receipt_has_lease_token_check
  check (receipt ? 'lease_token') not valid;

alter table public.yh_rex0_receipts
  validate constraint yh_rex0_receipt_has_lease_token_check;

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
  v_max_action_class text;
begin
  if p_lease_seconds < 5 or p_lease_seconds > 900 then
    raise exception 'invalid_lease_seconds';
  end if;

  select max_action_class into v_max_action_class
  from public.yh_rex0_workers
  where worker_id = p_worker_id
    and status = 'active'
    and p_principal_ref = any(principal_refs);

  if v_max_action_class is null then
    raise exception 'worker_not_authorized_for_principal';
  end if;

  select c.contract_id into v_contract_id
  from public.yh_rex0_contracts c
  where c.principal_ref = p_principal_ref
    and c.state in ('queued','retry_wait')
    and c.next_attempt_at <= now()
    and c.expires_at > now()
    and c.attempt_count < c.max_attempts
    and public.yh_rex0_action_rank(c.action_class) <= public.yh_rex0_action_rank(v_max_action_class)
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

drop function if exists public.yh_rex0_accept_receipt(text,text,text,jsonb,text);
create function public.yh_rex0_accept_receipt(
  p_worker_id text,
  p_contract_id text,
  p_lease_token uuid,
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
  if v_contract.lease_token is distinct from p_lease_token then raise exception 'lease_token_mismatch'; end if;
  if v_contract.lease_expires_at is null or v_contract.lease_expires_at <= now() then raise exception 'lease_expired'; end if;

  if not exists (
    select 1 from public.yh_rex0_workers
    where worker_id = p_worker_id
      and status = 'active'
      and v_contract.principal_ref = any(principal_refs)
  ) then
    raise exception 'worker_not_authorized_for_principal';
  end if;

  if p_receipt->>'principal_ref' is distinct from v_contract.principal_ref then raise exception 'principal_mismatch'; end if;
  if p_receipt->>'contract_id' is distinct from v_contract.contract_id then raise exception 'contract_mismatch'; end if;
  if p_receipt->>'lease_token' is distinct from p_lease_token::text then raise exception 'receipt_lease_token_mismatch'; end if;
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

drop function if exists public.yh_rex0_record_failure(text,text,text,text);
create function public.yh_rex0_record_failure(
  p_worker_id text,
  p_contract_id text,
  p_lease_token uuid,
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
  if v_contract.lease_token is distinct from p_lease_token then raise exception 'lease_token_mismatch'; end if;
  if v_contract.lease_expires_at is null or v_contract.lease_expires_at <= now() then raise exception 'lease_expired'; end if;

  if not exists (
    select 1 from public.yh_rex0_workers
    where worker_id = p_worker_id
      and status = 'active'
      and v_contract.principal_ref = any(principal_refs)
  ) then
    raise exception 'worker_not_authorized_for_principal';
  end if;

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

revoke all on function public.yh_rex0_action_rank(text) from public, anon, authenticated;
revoke execute on function public.yh_rex0_claim_next(text,text,integer) from public, anon, authenticated;
revoke execute on function public.yh_rex0_accept_receipt(text,text,uuid,text,jsonb,text) from public, anon, authenticated;
revoke execute on function public.yh_rex0_record_failure(text,text,uuid,text,text) from public, anon, authenticated;

grant execute on function public.yh_rex0_action_rank(text) to service_role;
grant execute on function public.yh_rex0_claim_next(text,text,integer) to service_role;
grant execute on function public.yh_rex0_accept_receipt(text,text,uuid,text,jsonb,text) to service_role;
grant execute on function public.yh_rex0_record_failure(text,text,uuid,text,text) to service_role;
