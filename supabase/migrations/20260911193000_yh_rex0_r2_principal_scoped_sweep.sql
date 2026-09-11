create or replace function public.yh_rex0_sweep_expired_leases_for_principal(
  p_principal_ref text
) returns table(retried integer, dead_lettered integer)
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
  where principal_ref = p_principal_ref
    and state = 'leased'
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
  where principal_ref = p_principal_ref
    and state = 'leased'
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
  where principal_ref = p_principal_ref
    and state = 'leased'
    and lease_expires_at <= now()
    and attempt_count < max_attempts;
  get diagnostics v_retried = row_count;

  return query select v_retried, v_dead;
end;
$$;

revoke execute on function public.yh_rex0_sweep_expired_leases_for_principal(text) from public, anon, authenticated;
grant execute on function public.yh_rex0_sweep_expired_leases_for_principal(text) to service_role;
