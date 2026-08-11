# Red Team Engine

Use this reference when adversarial review is justified. The goal is **risk reduction**, not performative disagreement.

## Entry gate

Enter Red Team when one or more are true:

- R3/R4 consequence;
- REV-C/REV-D commitment;
- explicit `/red`, premortem, or adversarial request;
- plan depends on multiple uncertain assumptions;
- user states certainty unsupported by evidence;
- failure would create a large strategic, financial, operational, legal, security, or reputational downside.

Do not enter for trivial, creative, or easily reversible tasks unless explicitly requested.

## Stage 1 — Build the strongest plan

Before attacking, summarize the plan in its strongest plausible form:

- intended outcome;
- core mechanism;
- strongest supporting evidence;
- key constraints;
- why a reasonable person would choose it.

Never attack a straw man.

## Stage 2 — Assumption map

List assumptions in four classes:

1. **Demand / behavior** — users, customers, counterparties behave as expected.
2. **Capability / execution** — the team/technology can deliver.
3. **Economics / resources** — costs, margins, cash, time, capacity work.
4. **Environment** — regulation, competition, platforms, suppliers, macro conditions remain compatible.

Rank each by:

`criticality × uncertainty`

Attack the top-ranked items first.

## Stage 3 — Failure modes

Generate failure paths from:

- internal execution;
- wrong model/strategy;
- external reaction;
- dependency failure;
- incentive mismatch;
- tail risk;
- timing;
- hidden coupling;
- data/measurement error.

Rank:

`plausibility × impact × detectability delay`

## Stage 4 — Premortem

Assume the plan failed after a realistic horizon.

Ask:

- What most likely killed it?
- What did we know but dismiss?
- What early signal appeared first?
- What decision made the failure expensive?
- What would we wish we had tested before committing?

Convert each material cause into a prevention or early-detection action.

## Stage 5 — Falsification

For the central thesis, complete:

> I would materially reduce confidence if ______.

Prefer observable thresholds:

- conversion below X after N qualified trials;
- CAC remains above LTV after Y cohorts;
- migration error rate exceeds threshold;
- dependency cannot meet required SLA;
- regulatory interpretation blocks the mechanism.

Avoid unfalsifiable wording.

## Stage 6 — Tail risk

Check low-probability, high-impact events separately.

Do not let expected value hide ruin risk.

Ask:

- Can one failure wipe out the ability to continue?
- Is there a single point of failure?
- Is rollback possible?
- Is liability capped?
- Can exposure be staged?

## Stage 7 — Mitigation

For each top risk choose one:

- eliminate;
- reduce probability;
- reduce impact;
- detect earlier;
- transfer;
- cap exposure;
- accept consciously.

## Red Team output

Keep it compact:

1. **Strongest vulnerability**
2. **Top 3–5 failure modes**
3. **Evidence that would falsify the plan**
4. **Mitigations**
5. **Verdict:** proceed / proceed with guardrails / test first / reject

Do not output a long generic risk catalog.
