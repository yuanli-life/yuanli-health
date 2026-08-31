# Main Governance Gate｜F0.1 Freeze Preconditions

Status: `REQUIRED_BEFORE_CONSTITUTION_FREEZE`

Real-time audit on 2026-08-31 found:

```text
main.protected = false
required_status_checks = none
```

YHOS-F0.1 therefore must remain `proposed` until repository governance is installed.

## Minimum required governance

Before an F0.1 Constitution Freeze can be claimed, `main` should be governed so that semantic changes use a pull request and the F0.1 validation workflow is enforced.

Minimum target policy:

1. changes to `main` through pull request;
2. require successful status check from `Validate YHOS F0.1 Candidate`;
3. explicit Human review before Constitution-semantic merge;
4. stale review invalidation or equivalent head-specific review discipline where available;
5. no candidate branch, CI run, or automated agent may activate Constitution semantics by itself;
6. merge authorization must refer to the exact reviewed PR head;
7. independent Acceptance Receipt remains separate from the candidate claim.

## Non-claim

This file records a governance requirement. It does not itself protect the branch, install a ruleset, authorize merge, or activate YHOS-F0.1.
