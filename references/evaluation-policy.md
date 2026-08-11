# Live Evaluation Policy v1.2

Thinking OS v1.2 evaluates **answer quality**, not whether the model visibly names mental models.

## Goal

Measure whether enabling Thinking OS produces a meaningful improvement over a fair baseline on representative reasoning tasks.

The benchmark must detect both:

- **under-reasoning** — missing assumptions, risks, evidence needs, or action logic;
- **over-reasoning** — unnecessary frameworks, verbosity, strategic reopening, or adversarial theater.

## A/B principle

For every case:

- use the **same target model**;
- use the same reasoning effort;
- use the same verbosity setting;
- use the same user prompt;
- change only the Thinking OS instruction condition;
- blind the judge to which answer used Thinking OS;
- randomize A/B presentation order;
- keep the benchmark case set fixed while tuning a version.

Do not compare different models and call the difference a Thinking OS gain.

## Benchmark layers

### Layer 1 — Reasoning benchmark

Primary v1.2 benchmark.

Use self-contained tasks that do not require external tools to answer well.

Purpose:
- isolate reasoning quality;
- measure overthinking restraint;
- measure decision quality;
- measure challenge calibration;
- measure actionability.

### Layer 2 — Evidence-awareness cases

A smaller subset may intentionally lack current/private evidence.

The correct behavior is not to fabricate certainty. The answer should identify the missing source of truth and say what information would change the recommendation.

No live web/private tools are enabled in the v1.2 core benchmark.

### Layer 3 — Tool orchestration

Deferred to a later version.

Once reasoning quality is stable, separately benchmark:
- web-search decisions;
- private-source selection;
- tool-call efficiency;
- citation/evidence quality.

Do not mix this into the v1.2 headline score.

## Judge dimensions

Score each answer 0–4.

### 1. Task success — 30%

Did it actually satisfy the user's request?

### 2. Correctness & logic — 20%

Are the claims, causal logic, comparisons, and recommendations coherent and defensible?

### 3. Calibration & evidence judgment — 15%

Does it distinguish facts from assumptions, avoid false certainty, and request/check evidence only when decision-relevant?

### 4. Actionability — 15%

When action is appropriate, does it end with a concrete next step, test, decision rule, or execution path?

### 5. Appropriate depth — 10%

Is the response neither shallow nor bloated for the consequence and reversibility of the task?

### 6. Reasoning judgment — 10%

Does it challenge framing/assumptions when useful and refrain from needless red-teaming or framework theater when not useful?

Weighted total is 0–100.

## Pairwise winner

In addition to absolute scores, the judge selects:

- `A`
- `B`
- `tie`

The judge must state only a concise decision rationale, not hidden chain-of-thought.

## Headline metrics

Report:

- Thinking OS win rate;
- baseline win rate;
- tie rate;
- mean weighted score delta;
- median score delta;
- per-domain score delta;
- overthinking-control win rate;
- high-stakes/adversarial win rate;
- average output length delta;
- token delta;
- latency delta;
- estimated cost delta.

Quality gain must be considered together with token/latency/cost.

## Promotion gate

A new Thinking OS version should not be promoted solely because average score rises.

Recommended v1.2 promotion criteria:

1. mean quality delta >= +3.0 points;
2. Thinking OS pairwise wins >= 55%;
3. baseline wins <= 25%;
4. control/trivial cases show no material overthinking regression;
5. high-stakes cases do not lose calibration or risk coverage;
6. no single major domain regresses by >3 points without an explained trade-off.

These are engineering defaults, not universal truths.

## Anti-overfitting rule

Do not rewrite the Router to satisfy one benchmark wording.

Before changing policy:
- identify the failure class;
- check at least 3 semantically similar cases;
- change a general rule;
- rerun the full benchmark;
- inspect new regressions.

## Benchmark freeze

For a version comparison, freeze:
- benchmark prompts;
- judge rubric;
- target model;
- target reasoning effort;
- grader model;
- grader reasoning effort.

If any changes, start a new benchmark run ID and record the change.
