# Router Policy v1.1

This policy sharpens the v1.0 router with **priority rules, negative triggers, escalation gates, and de-escalation gates**.

## 1. Priority order

Apply routing decisions in this order:

1. **Explicit user override** (`/action`, `/red`, `/first`, `/simple`, etc.).
2. **Safety / severe irreversibility** — do not suppress necessary warnings.
3. **Information need** — current/private facts may require tools before reasoning.
4. **Primary intent** — decide what kind of work the user actually wants.
5. **De-escalation** — remove unnecessary models for trivial/reversible tasks.
6. **Escalation** — add rigor only for consequence, uncertainty, or irreversibility.
7. **Domain pack** — add domain-specific checks only after the core route is clear.

The most common routing failure is doing step 6 before step 5.

## 2. Negative triggers — when NOT to use heavy reasoning

### Do not use Red Team when

- the user asks for routine rewriting, formatting, translation, ideation, or direct execution;
- the choice is cheap and fully reversible;
- there is not yet a coherent proposal to attack;
- the task is primarily factual and the answer depends on fresh evidence, not adversarial reasoning;
- disagreement would not change action or reduce meaningful risk.

### Do not use First Principles when

- the task is a direct fact lookup;
- the user only wants execution of an already-decided low-risk path;
- industry convention is not constraining the solution;
- rebuilding from fundamentals would not change the answer.

### Do not use Premortem when

- the task is not a plan/commitment;
- failure cost is negligible;
- the next action is a tiny reversible experiment;
- the user is still exploring options and has not selected a candidate path.

### Do not use Base Rate when

- the task is creative generation rather than prediction/decision;
- no meaningful reference class exists;
- the decision can be resolved directly by inspecting current evidence.

### Do not decompose when

- the answer is one step;
- the decomposition would be longer than the task itself;
- the user explicitly requests a compact answer and no important dependency is hidden.

## 3. Explicit override precedence

- `/action`: suppress strategic reopening. Keep only warnings that prevent severe harm or irreversible error.
- `/simple`: prefer direct answer; model budget 0–1 unless high-stakes.
- `/fast`: compress analysis but do not skip critical evidence or safety.
- `/red`: force adversarial review after first steelmanning the plan.
- `/first`: force first-principles reframing but still respect real constraints.
- `/data`: increase evidence bar; reduce speculation.
- `/idea`: stay in exploration; delay convergence unless asked.
- `/deep` / `/max`: increase depth only where it improves the decision; never disables stop rules.

## 4. Evidence gate before model gate

If a central fact is current, private, or externally verifiable, fetch/inspect it before adding reasoning layers.

Examples:

- API price comparison → current sources, not First Principles.
- Repository build-vs-buy → inspect repository, then decision models.
- Metric drop → inspect analytics if available, then diagnose.
- Current regulation → authoritative current source, then implications.

## 5. Red Team escalation formula

Red Team is justified when at least one is true:

- `risk >= R3` and `reversibility <= REV-C`;
- explicit adversarial request;
- unjustified certainty in a consequential claim;
- several critical assumptions are both uncertain and untested;
- a failure mode could create ruin, lock-in, major loss, or long recovery.

Red Team is usually **not** justified for R0–R1 + REV-A unless explicitly requested.

## 6. Analysis depth de-escalation

Reduce depth by one or more levels when:

- next step costs little;
- next step can be rolled back quickly;
- the test is bounded;
- the user already asked for execution;
- further information would not change the next action.

A C3 problem can still deserve an L1 answer when the next move is a cheap reversible test.

## 7. Model budget hard guardrails

- L0: 0 models.
- L1: 0–1 model.
- L2: 1–2 models.
- L3: 2–4 models.
- L4: 3–5 models.
- L5: staged reasoning; no more than 6 models active in one stage.

If selected models exceed the budget, remove the model with the lowest marginal decision value.

## 8. Model redundancy rules

Avoid redundant pairs unless each has a distinct job:

- Five Whys + Issue Tree: tree first, Five Whys only on top branch.
- Red Team + Premortem: Red Team attacks structure; Premortem surfaces realistic future failure causes.
- Probability + Expected Value: probability estimates feed EV; do not repeat uncertainty prose twice.
- MECE + Issue Tree: use MECE for plan structure; Issue Tree for diagnostic hypotheses.
- 80/20 + TOC: TOC identifies the constraint; 80/20 prioritizes actions around it.

## 9. Output silence rule

The router score, model names, and internal classification should normally remain invisible.

Expose them only if:

- the user explicitly asks what framework is being used;
- showing the uncertainty/risk classification helps the decision;
- the user is debugging or evaluating the skill itself.

## 10. Final preflight

Before answering, ask:

1. Is this actually an information problem?
2. Can I remove one model without reducing answer quality?
3. Am I red-teaming because it matters, or because the trigger word appeared?
4. Would a real action teach more than another paragraph?
5. Did the user explicitly ask me to stop analyzing?
