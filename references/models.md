# Core Models v0.1

Use models as executable reasoning modules, not decorative labels.

## M01 — Problem Reframing

**Purpose:** Verify that the stated question matches the desired outcome.

**Triggers:** XY problem, solution-first framing, narrow optimization, user asks "how" before "whether".

**Procedure:**
1. State the desired outcome.
2. State the current framing.
3. Ask what must be true for the framing to be the right one.
4. Offer a better question if it changes the solution space.

**Avoid:** Reframing simple direct requests; turning every request into philosophy.

**Output:** One-sentence "real problem" when materially different.

---

## M02 — First Principles

**Purpose:** Rebuild a solution from irreducible facts and true constraints.

**Triggers:** industry convention, high cost/complexity, fundamental redesign, "everyone does it this way".

**Procedure:**
1. Define the required outcome.
2. Separate physical/legal/technical constraints from convention.
3. Identify irreducible facts.
4. Delete inherited assumptions.
5. Rebuild the minimal solution.

**Avoid:** Pretending real constraints do not exist; applying to routine factual tasks.

**Output:** Bottom facts → removable assumptions → rebuilt approach.

---

## M03 — Five Whys

**Purpose:** Move from symptom to root cause.

**Triggers:** recurring failure, defect, metric drop, operational problem.

**Procedure:** Ask "why" only while each answer remains causally plausible; branch when multiple causes exist; stop at an actionable root.

**Avoid:** Forcing exactly five layers; inventing causal certainty.

**Output:** Symptom → causal chain → root hypothesis → test.

---

## M04 — MECE Decomposition

**Purpose:** Split a complex problem into minimally overlapping, collectively useful parts.

**Triggers:** broad plan, analysis tree, multiple workstreams.

**Procedure:** Define scope; partition by one clear dimension; check overlap/gaps; recurse only until each part is actionable.

**Avoid:** Over-decomposition; fake completeness where the world is fuzzy.

**Output:** 3–7 major branches, then only necessary sub-branches.

---

## M05 — Issue Tree

**Purpose:** Turn a broad question into testable sub-questions.

**Triggers:** diagnosis, business analysis, investigation.

**Procedure:** Root question → hypotheses/drivers → evidence/test under each branch → prioritize discriminating branches.

**Avoid:** Listing categories without a decision purpose.

**Output:** Tree + priority branch to test first.

---

## M06 — Systems Thinking

**Purpose:** Understand feedback, interactions, delays, and unintended effects.

**Triggers:** repeated interventions fail, multi-actor systems, long-term effects.

**Procedure:** Identify actors/state variables → flows → feedback loops → delays → leverage points.

**Avoid:** Making a simple linear problem needlessly systemic.

**Output:** Key loop(s), delay(s), and leverage point(s).

---

## M07 — Theory of Constraints

**Purpose:** Find the single constraint currently limiting system throughput.

**Triggers:** "everything needs improvement", stalled project, capacity bottleneck.

**Procedure:** Identify → exploit → subordinate → elevate → repeat.

**Avoid:** Optimizing non-bottlenecks; naming vague "lack of effort" as a constraint.

**Output:** Current bottleneck + one action to relieve it.

---

## M08 — Pareto 80/20

**Purpose:** Focus effort on the few inputs driving most value.

**Triggers:** long task list, resource scarcity, optimization.

**Procedure:** Estimate impact distribution → identify high-leverage minority → deprioritize low-value work.

**Avoid:** Treating 80/20 as literal law.

**Output:** Top leverage actions + explicit "not now" items.

---

## M09 — Base Rate / Outside View

**Purpose:** Anchor predictions in comparable historical outcomes.

**Triggers:** forecasts, startup success, project duration, rare outcomes, overconfident narrative.

**Procedure:** Define reference class → obtain/estimate base rate → adjust only for material differences.

**Avoid:** Cherry-picking a reference class.

**Output:** Outside-view baseline + justified adjustments.

---

## M10 — Probabilistic Thinking

**Purpose:** Replace false certainty with calibrated likelihoods.

**Triggers:** uncertain outcomes, "definitely", "never", forecasting.

**Procedure:** Express ranges/probabilities → list main uncertainty drivers → update when evidence changes.

**Avoid:** Fake precision.

**Output:** Probability/range + confidence + update triggers.

---

## M11 — Expected Value

**Purpose:** Compare uncertain options by probability-weighted outcomes.

**Triggers:** bets, experiments, investments, asymmetric opportunities.

**Procedure:** Enumerate material outcomes → estimate probabilities/payoffs → include downside and optionality → compare EV qualitatively or quantitatively.

**Avoid:** Ignoring ruin risk, non-monetary effects, or probability uncertainty.

**Output:** EV comparison + sensitivity driver.

---

## M12 — Opportunity Cost

**Purpose:** Make the cost of foregone alternatives visible.

**Triggers:** resource allocation, long commitments, "free" projects, time-intensive choices.

**Procedure:** Identify scarce resource → best alternative use → compare incremental value.

**Avoid:** Comparing against unrealistic alternatives.

**Output:** "Choosing X means giving up Y."

---

## M13 — Second-Order Thinking

**Purpose:** Consider reactions and downstream consequences.

**Triggers:** policy, pricing, incentives, competitive behavior, long-term strategy.

**Procedure:** First-order effect → likely responses → second/third-order effects → time horizon → feedback.

**Avoid:** Endless speculation.

**Output:** 2–3 material downstream effects.

---

## M14 — Reversibility

**Purpose:** Match decision speed to cost of reversal.

**Triggers:** commitment, launch, architecture, purchase, strategy.

**Procedure:** Classify REV-A..D → scale evidence/review accordingly → prefer experiments for reversible choices.

**Avoid:** Treating emotional discomfort as irreversibility.

**Output:** Reversibility class + speed recommendation.

---

## M15 — Red Team

**Purpose:** Find vulnerabilities in an important plan.

**Triggers:** R3/R4, irreversible commitment, explicit request, strong confidence.

**Procedure:** Identify critical assumptions → attack strongest version → rank failure paths by plausibility × impact → propose mitigations.

**Avoid:** Contrarian theater; bizarre edge cases.

**Output:** Top 3–5 vulnerabilities + mitigations.

---

## M16 — Premortem

**Purpose:** Surface failure modes before commitment.

**Triggers:** plan launch, large project, team decision.

**Procedure:** Assume failure at a future date → independently generate causes → cluster → rank → add prevent/detect actions.

**Avoid:** Generic risk lists.

**Output:** Ranked failure causes + early warning signals.

---

## M17 — Falsification

**Purpose:** Define evidence that would prove the current belief wrong.

**Triggers:** strong claim, confirmation bias, thesis testing.

**Procedure:** State claim → derive observable disconfirmers → define threshold → seek the most informative disconfirming evidence.

**Avoid:** impossible standards of proof.

**Output:** "I would change my mind if…"

---

## M18 — Key Assumption Check

**Purpose:** Expose hidden dependencies in a conclusion or plan.

**Triggers:** multi-step plan, new business, recommendation with sparse evidence.

**Procedure:** List must-be-true assumptions → rank by importance × uncertainty → validate top assumption first.

**Avoid:** Validating low-impact assumptions first.

**Output:** Top assumptions + validation order.

---

## M19 — Minimum Validation Action (MVA)

**Purpose:** Learn the most with the least cost.

**Triggers:** uncertainty blocks action, new idea, reversible experiment.

**Procedure:** Identify the decision-changing uncertainty → design smallest real-world test → define signal, threshold, duration, next decision.

**Avoid:** "Small action" that yields no useful information.

**Output:** One test with success/fail/continue criteria.

---

## M20 — OODA

**Purpose:** Learn and adapt through fast reality-contact loops.

**Triggers:** dynamic environments, execution after enough analysis, iterative optimization.

**Procedure:** Observe → Orient → Decide → Act → repeat with new evidence.

**Avoid:** Acting fast without orientation; looping without metrics.

**Output:** Next loop: observation, decision, action, review point.
