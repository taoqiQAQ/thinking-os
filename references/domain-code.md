# Code Domain Pack

Use for software architecture, implementation planning, build-vs-buy, migrations, reliability, performance, and technical decisions.

## Technical decision map

1. **Requirement** — functional and non-functional.
2. **Constraints** — language, platform, latency, security, budget, team.
3. **Current system** — source of truth before proposing changes.
4. **Architecture** — boundaries, dependencies, data flow.
5. **Build vs buy** — total cost, lock-in, control, speed.
6. **Complexity** — cognitive and operational.
7. **Maintainability** — ownership, upgrades, observability.
8. **Security / privacy**
9. **Reliability / failure domains**
10. **Performance**
11. **Testing**
12. **Migration / rollback**
13. **Technical debt**
14. **Acceptance criteria**

## Debug route

Reproduce → localize → hypothesis tree → discriminating test → smallest fix → regression test.

## Architecture route

Requirements → alternatives → reversibility → failure modes → migration plan → rollback → acceptance.

## Anti-patterns

- designing before inspecting the codebase;
- adding infrastructure without a measured bottleneck;
- rewriting when migration is safer;
- optimizing benchmarks irrelevant to workload;
- ignoring operational burden;
- no rollback for risky change.

## Output

- technical recommendation;
- trade-offs;
- affected components;
- migration/implementation steps;
- tests;
- rollback;
- acceptance criteria.
