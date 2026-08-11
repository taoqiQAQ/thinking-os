# Decision State Engine v1.5

Use Decision State for longitudinal consequential work: projects, strategies, investments, architecture choices, operating plans, and other decisions where evidence arrives over time.

Decision State is **not generic chat memory**. It is an auditable record of:
- what was believed;
- why it was believed;
- which assumptions mattered;
- what evidence arrived;
- what changed;
- what decision followed;
- what would cause another change.

## Activation gate

Create/update state when the decision will be revisited, new evidence will arrive, hypotheses/probabilities matter, or kill/scale/pivot criteria matter.

Usually do not create state for trivial reversible choices, one-off facts, simple rewriting, or routine execution with no future review.

## Persistence truth

Never claim automatic persistence.

Persist only through storage the host actually supports:
- project/repository files;
- connected database/docs;
- explicit durable memory;
- or an exported state object the user can provide later.

## Core record

A state contains:
1. decision identity/question/objective
2. status and current recommendation
3. confidence and probability estimates
4. Assumption Ledger
5. Evidence Ledger
6. kill / scale criteria
7. append-only Decision Journal
8. reviews
9. outcomes

Schema: [../state/decision-state.schema.json](../state/decision-state.schema.json)

## Append-only integrity

Evidence and journal history are append-only.

Never rewrite an old belief after seeing the outcome. If a belief changes, record:
- before;
- after;
- evidence references;
- reason;
- timestamp.

If an old assumption is replaced, supersede it rather than erasing it.

## Material-update gate

Ask:
> Could this information change a probability, critical assumption, recommendation, kill/scale criterion, or next action?

If no, do not churn the recommendation.
If yes:
1. append evidence;
2. update affected assumptions;
3. update belief/confidence;
4. check kill/pivot/scale gates;
5. append journal entry;
6. choose next action.

## Belief updates

Use exact Bayesian updating only when a defensible prior and likelihood information exist.

Otherwise use calibrated judgment:
- prior probability/range;
- evidence direction/strength;
- revised probability/range;
- explanation for magnitude.

Do not invent likelihood ratios or fake precision.

See [belief-update.md](belief-update.md).

## Assumptions

Prioritize by:
`criticality × uncertainty`

Statuses:
- untested
- supported
- weakened
- falsified
- superseded

See [assumption-ledger.md](assumption-ledger.md).

## Evidence

Record source, observed time, quality, direction, relevance, affected assumptions, and optional expiry.

Preserve conflicting evidence.

See [evidence-ledger.md](evidence-ledger.md).

## Kill / Pivot / Scale

On every material update:
- **Kill:** has a predeclared stop condition triggered?
- **Pivot:** did a core mechanism fail while the objective remains attractive?
- **Scale:** has evidence crossed a predeclared threshold for more commitment?

Do not move thresholds after seeing results merely to avoid an uncomfortable decision.

## Review triggers

Review when:
- scheduled review arrives;
- material evidence arrives;
- a criterion nears/triggers;
- important evidence becomes stale;
- environment changes materially;
- user asks for review.

See [decision-review.md](decision-review.md).

## Output

Routine update:
- What changed
- Belief/recommendation delta
- Why
- Kill/scale status
- Next action

Use `/state` for the full summary.
