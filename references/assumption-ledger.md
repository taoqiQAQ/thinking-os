# Assumption Ledger

Question:
> What must be true for the current recommendation to work?

Fields:
- assumption_id
- statement
- criticality 1–5
- uncertainty 1–5
- status
- evidence_refs
- created_at / updated_at
- falsification_condition
- notes

Priority = `criticality × uncertainty`.

Statuses:
- untested
- supported
- weakened
- falsified
- superseded

A falsified assumption cannot silently become supported again. Supersede it and create a new assumption if the mechanism/definition changed.

Prefer observable falsification conditions.

Flag **assumption debt** when high-criticality/high-uncertainty assumptions remain untested while commitment increases.
