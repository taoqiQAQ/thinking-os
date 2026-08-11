# Evidence Ledger

Evidence is append-only and source-aware.

Required:
- evidence_id
- observed_at
- source
- summary
- quality
- direction
- relevance
- assumption_refs
- optional expires_at

Quality:
- verified
- probable
- anecdotal
- speculative

Direction:
- supports
- challenges
- neutral
- mixed

Before counting evidence independently, check shared upstream sources.

When evidence becomes stale, preserve it but reduce its weight and refresh only if decision-relevant.

When evidence conflicts:
1. preserve both;
2. compare source quality/relevance;
3. check segment/time differences;
4. carry unresolved uncertainty explicitly.
