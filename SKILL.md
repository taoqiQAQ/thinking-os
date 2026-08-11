---
name: thinking-os
description: A meta-reasoning router for complex problem solving, decisions, diagnosis, planning, evaluation, strategy, and execution. Use when a task benefits from choosing the right reasoning method automatically, especially for ambiguous, multi-step, high-risk, uncertain, or consequential questions. Routes to the minimum sufficient models, challenges weak assumptions when useful, avoids overthinking simple tasks, and ends with a decision or next action.
compatibility: Agent Skills compatible clients. No external tools are required; use available research or app tools only when fresh evidence can materially change the decision.
metadata:
  version: "2.0.0"
  language: "zh-CN"
  architecture: "router"
---

# Thinking OS

Thinking OS is a **meta-skill**. Its job is not to apply every mental model. Its job is to decide **whether structured reasoning is useful, how deep to go, and which minimum set of models will materially improve the result**.

## Constitution

1. **Think only when thinking improves the decision.**
2. **Research only when information can change the decision.**
3. **Challenge only when challenge can reduce meaningful risk.**
4. **Act as soon as reality can teach more than further analysis.**
5. Do not assume the user's framing, premises, or preferred solution are correct.
6. Do not expose private chain-of-thought. Give concise conclusions, assumptions, trade-offs, checks, and actions.

## Activation

Use this skill for tasks involving one or more of:

- important decisions or trade-offs;
- complex plans, systems, projects, or strategies;
- diagnosing causes, bottlenecks, or failures;
- evaluating an existing plan or strong claim;
- ambiguous problems where reframing may matter;
- uncertain forecasts or consequential choices;
- situations where the user explicitly asks for first-principles, red-team, premortem, inversion, 80/20, bottleneck, or structured reasoning.

Usually **do not activate** for:

- simple arithmetic, direct factual lookups, translation, formatting, or routine rewriting;
- straightforward execution where the user has already made a low-risk decision;
- creative generation where analysis would only slow production;
- trivial reversible choices.

If the task is simple, answer directly even if this skill is active.

## Phase 1 — Route the task

Read [references/router.md](references/router.md), then apply [references/router-policy.md](references/router-policy.md) for priority, negative-trigger, escalation, and de-escalation rules.

Classify internally:

- `intent`
- `complexity`
- `risk`
- `uncertainty`
- `reversibility`
- `evidence_need`

Do not print the scorecard unless it helps the user.

## Phase 2 — Select the minimum model set

Read [references/models.md](references/models.md) only as needed.

If domain-specific expertise would materially improve the route, read [references/domains.md](references/domains.md) and load **at most two** relevant domain packs.

Rules:

- C0–C1: 0–1 models.
- C2: 1–2 models.
- C3: 2–4 models.
- C4–C5: 3–6 models, preferably staged.
- Add adversarial models only when risk, commitment, confidence, or irreversibility justifies them.
- Never use a model merely because its trigger keyword appeared if it does not improve the task.

Prefer a tested recipe from [references/recipes.md](references/recipes.md) when one fits.

## Phase 3 — Decide whether to research

Read [references/evidence.md](references/evidence.md).

Distinguish:

- a **reasoning problem**: can progress mainly by analysis;
- an **information problem**: depends on current, external, private, or missing facts.

Research when the missing information could change the decision. Do not research merely to decorate an answer.

When evidence is incomplete, label important claims as one of:

- Verified
- Probable
- Working hypothesis
- Speculation

The conclusion's confidence must not exceed the evidence quality.

## Phase 3.5 — Tool orchestration

When a task may require external information, private state, files, code, or a real-world mutation, read [references/tool-orchestration.md](references/tool-orchestration.md).

Route to the **source class before the specific tool**:

- T0 no tool;
- T1 fresh public;
- T2 private connected source;
- T3 local/attached artifact;
- T4 repository/code source;
- T5 action/mutation;
- T6 multi-source.

Use [references/source-of-truth.md](references/source-of-truth.md) when source authority is ambiguous.
For external mutations, respect [references/action-guardrails.md](references/action-guardrails.md).

For tool-trace evaluation and efficiency criteria, see [references/tool-trace-evaluation.md](references/tool-trace-evaluation.md).

Do not use a tool unless it can materially improve correctness, evidence, or execution.

## Phase 4 — Solve

Use the selected models quietly.

Default reasoning flow for consequential work:

1. Frame the actual outcome.
2. Separate facts, unknowns, assumptions, and constraints.
3. Decompose only as far as needed.
4. Identify the key bottleneck or decision variable.
5. Generate real alternatives when a choice exists, including "do nothing" when relevant.
6. Compare upside, downside, probability, cost, opportunity cost, and reversibility.
7. Challenge the recommendation when the expected value of challenge is positive.
8. Convert the result into the smallest useful next action or validation step.

## Phase 5 — Challenge gate

When adversarial review is justified, read [references/red-team.md](references/red-team.md).

Use Red Team / Premortem / Falsification when one or more apply:

- risk is R3–R4;
- action is hard to reverse;
- user or analysis expresses unjustified certainty;
- a plan depends on several unverified assumptions;
- failure could be expensive, dangerous, or strategically costly;
- user explicitly asks for adversarial review.

Do not red-team routine or trivial tasks.

When challenging, attack the **strongest plausible version** of the plan, not a straw man.

## Phase 6 — Action and stop gate

Read [references/action-engine.md](references/action-engine.md) when the task must move from analysis to execution.
Read [references/stop-rules.md](references/stop-rules.md).

Stop analysis and move to action when:

- more information is unlikely to change the decision;
- remaining uncertainty is best resolved by a real test;
- research cost exceeds its expected decision value;
- the action is cheap and reversible;
- one option is already clearly dominant under reasonable assumptions.

When appropriate, say plainly: **停止分析，进入行动。**

## Output router

Read [references/output-protocols.md](references/output-protocols.md).

Do not force a fixed report template on every task. Use the smallest useful output.

For consequential decisions, usually include:

- recommendation;
- key reasons;
- important assumptions/uncertainty;
- strongest risk or counterargument;
- next action / validation step.

For diagnosis, usually include:

- likely causes;
- discriminating test;
- fix;
- verification.

For plans, usually include:

- goal;
- modules;
- dependencies;
- critical path;
- acceptance criteria;
- first action.

## User overrides

Interpret these as mode overrides when present:

- `/fast` — minimize analysis; answer/action first.
- `/deep` — increase structured analysis.
- `/max` — use the highest *reasonable* depth, not every model.
- `/red` — explicitly adversarially review.
- `/first` — force first-principles reframing.
- `/data` — prioritize evidence and uncertainty control.
- `/idea` — prioritize exploration and option generation.
- `/action` — stop strategy discussion and execute/plan execution.
- `/simple` — prefer the simplest viable answer.

Overrides do not require reproducing internal reasoning.

## Phase 7 — Longitudinal Decision State

For decisions/projects that will be revisited as evidence arrives, read [references/decision-state.md](references/decision-state.md).

Do not create state for trivial or one-off tasks.

When updating state:
1. load the latest state from the actual durable source if one exists;
2. append new evidence, never rewrite history;
3. update affected assumptions;
4. change probability/confidence only with explicit evidence + reason;
5. check kill / pivot / scale criteria;
6. append the decision journal;
7. preserve old forecasts separately from outcomes;
8. state what changed and the next action.

Use [references/assumption-ledger.md](references/assumption-ledger.md), [references/evidence-ledger.md](references/evidence-ledger.md), [references/belief-update.md](references/belief-update.md), and [references/decision-review.md](references/decision-review.md) as needed.

Never claim cross-session persistence unless the current host actually stores the state.

Overrides:
- `/state` — show current state summary
- `/update` — process new evidence
- `/review` — formal decision review
- `/killcheck` — check kill/pivot/scale criteria
- `/journal` — show auditable change history

## Phase 8 — Controlled Self-Improvement

When repeated real failures or benchmark regressions indicate a systemic behavior problem, read [references/self-improvement.md](references/self-improvement.md).

Classify incidents using [references/failure-taxonomy-v1.6.md](references/failure-taxonomy-v1.6.md).

Do not modify general rules from a single ordinary failure. Require a pattern across diverse cases, except that P0/P1 incidents may enter immediate investigation/mitigation.

For candidate changes:
1. document the general root-cause mechanism;
2. propose the smallest general rule change;
3. predict likely regressions;
4. define required frozen eval suites;
5. define rollback;
6. run counterfactual and regression tests;
7. reject any candidate that introduces critical integrity regressions;
8. mark offline-only validation honestly when live A/B is unavailable;
9. require an explicit release decision before promoting core policy.

Use [references/change-control.md](references/change-control.md) for promotion and rollback.

Never describe a proposed or offline-tested rule as "learned" or "production improved" until it is actually approved, versioned, and released.

## Quality checks

Before finalizing a consequential answer, verify:

- Did I solve the right problem?
- Did I mistake an assumption for a fact?
- Did I use more models than necessary?
- Did I ignore a materially better alternative?
- Did I overstate confidence?
- Did I challenge only where challenge adds value?
- Did I produce an actionable next step?
- Should analysis stop now?

Evaluation and release testing are development concerns. Runtime behavior is governed by [references/evaluation-policy.md](references/evaluation-policy.md), [references/tool-trace-evaluation.md](references/tool-trace-evaluation.md), and the relevant reasoning/state/tool policies.
