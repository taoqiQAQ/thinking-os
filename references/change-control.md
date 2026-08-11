# Change Control & Promotion Gate

Self-improvement is a release process.

## Proposal states

- `captured`
- `triaged`
- `pattern_confirmed`
- `candidate`
- `testing`
- `ready_for_review`
- `rejected`
- `promoted`
- `rolled_back`

The automated engine may advance through `ready_for_review`.
Core policy promotion requires an explicit release decision.

## Pattern gate

Normal:
- recurrence >= 3;
- distinct prompt forms >= 2;
- same pattern key;
- at least one reproducible/eval-backed example.

Critical:
- P0 or strong P1 may bypass recurrence threshold for mitigation/testing;
- still requires tests before permanent promotion.

## Proposal quality gate

Must include:
- general causal mechanism;
- current rule;
- proposed rule;
- scope;
- affected files;
- supporting incidents;
- expected improvements;
- regression risks;
- required tests;
- rollback.

An exact-string patch is rejected.

## Deterministic integrity gate

Required deterministic suites must be 100% passing unless the suite itself is being intentionally and audibly revised.

A failed suite blocks promotion.

## Live quality gate

When live metrics are available, use the relevant frozen benchmark.

Default answer-quality gates from v1.2:
- mean quality delta >= +3;
- Thinking OS pairwise win >= 55%;
- baseline wins <= 25%;
- no major domain regression >3 points without explicit accepted trade-off.

Default tool gates from v1.4:
- trace pass >= 90%;
- NO_TOOL false positive <= 5%;
- first-call precision >= 90%;
- forbidden-call rate <= 2%;
- read-before-write = 100%;
- synthetic action correctness = 100%.

If live metrics are unavailable, mark the promotion decision as `offline_validated`, not live-proven.

## Regression budget

Never trade a critical integrity failure for average-score improvement.

Priority:
1. safety / destructive action / privacy / state integrity
2. correct source-of-truth and action scope
3. task success / correctness
4. calibration
5. efficiency / verbosity

## Rollback

Every promoted change must identify:
- previous version/package;
- files/rules changed;
- trigger for rollback;
- rollback procedure;
- data/state migration concern if any.

## Change isolation

Prefer one behavioral hypothesis per candidate release.

If several changes are bundled, attribution becomes weak and rollback becomes harder.
