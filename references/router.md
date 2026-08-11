# Router Reference

## 1. Intent

Choose one primary intent and optional secondary intents.

| Code | Intent | Typical request |
|---|---|---|
| FACT | factual answer | "What is X?" |
| UNDERSTAND | learn/explain | "Explain X so I understand it." |
| DIAGNOSE | find cause | "Why is this failing?" |
| CREATE | generate possibilities | "Design a new approach." |
| PLAN | structure work | "Make a project plan." |
| DECIDE | choose among options | "A or B?" |
| EVALUATE | inspect an existing plan | "Is this plan good?" |
| OPTIMIZE | improve a running system | "How do I improve conversion?" |
| EXECUTE | carry out decided work | "Give me deployment steps." |
| FORECAST | reason about future outcomes | "What is likely next?" |
| INVESTIGATE | establish what is true | "Figure out how this business works." |
| STRATEGY | allocate resources / choose direction | "Where should we focus this year?" |

Multi-intent is allowed. Pick one primary intent to prevent framework sprawl.

## 2. Complexity

- **C0 — Direct:** one-step answer; no meaningful trade-off.
- **C1 — Simple:** single variable or routine choice.
- **C2 — Structured:** a few variables or sequential steps.
- **C3 — Complex:** multiple interacting variables, alternatives, or stages.
- **C4 — High:** long horizon, many dependencies, meaningful resources.
- **C5 — Systemic:** system design, strategy, major irreversible choice.

## 3. Risk

- **R0:** negligible consequence.
- **R1:** low; mistakes are cheap/easy to correct.
- **R2:** meaningful time/money/opportunity cost.
- **R3:** high cost, long commitment, or meaningful operational risk.
- **R4:** severe or hard-to-reverse consequences.

Risk changes depth. It does not automatically change the factual answer.

## 4. Uncertainty

- **U0:** material facts are known.
- **U1:** minor unknowns; assumptions can be explicit.
- **U2:** one or more important unknowns.
- **U3:** key variables unknown; validation should precede commitment.
- **U4:** inherently unpredictable; use scenarios and probabilities.

## 5. Reversibility

- **REV-A:** fully/cheaply reversible → bias to action.
- **REV-B:** mostly reversible → small test first if uncertain.
- **REV-C:** costly to reverse → validate key assumptions.
- **REV-D:** highly irreversible → high evidence bar + adversarial check.

## 6. Evidence need

Set `evidence_need = HIGH` when the answer materially depends on:

- current prices, laws, schedules, product capabilities, markets, news, or public figures;
- the user's private documents, data, calendar, email, codebase, or project state;
- an unfamiliar term/entity whose meaning affects the answer;
- exact numerical assumptions whose error could change the recommendation.

Set `evidence_need = LOW` when the task is mainly conceptual, creative, or based entirely on supplied facts.

## 7. Depth selection

A practical default:

- C0/C1 + R0/R1 → L0/L1.
- C2 → L1/L2.
- C3 or R2 → L2/L3.
- C4 or R3 → L3/L4.
- C5 or R4 → L4/L5.

Then reduce depth if the action is highly reversible and cheap.
Increase depth if uncertainty is high and the decision is expensive/irreversible.

## 8. Exploration vs exploitation

Use **EXPLORE** when the user does not yet know which direction is promising.
Use **EXPLOIT** when there is enough evidence that one direction works.

EXPLORE models: first principles, reframing, options, MVA.
EXPLOIT models: bottleneck, 80/20, critical path, feedback loop.

Do not keep exploring after a direction has earned focus.
Do not optimize a direction that has not yet earned belief.
