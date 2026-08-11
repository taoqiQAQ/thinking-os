# Changelog

## 2.0.0 — Production Stable

- Froze the eight-layer Thinking OS architecture.
- Removed runtime links to development-only eval artifacts.
- Added production/source package separation.
- Added architecture, installation, security, and stable-release documentation.
- Added release audit, production-package validation, dead-reference/model checks, secret scan, and compile gate.
- Preserved v1.x frozen evaluation suites in the source package.
- Declared live A/B evidence boundary explicitly: offline validation is not presented as live proof.

## 1.6.0 — Controlled Self-Improvement Engine

- Added incident → pattern → candidate → regression → promotion lifecycle.
- Added expanded failure taxonomy and severity triage.
- Added recurrence + semantic-diversity pattern gate.
- Added anti-overfitting and exact-prompt-patch rejection.
- Added candidate change, rollback, and promotion policy.
- Added offline-vs-live validation distinction.
- Added deterministic integrity blocking and v1.2/v1.4 live promotion hooks.
- Added 48-case self-improvement lifecycle regression suite.
- Core rules are never silently self-promoted.

## 1.5.0 — Decision State / Memory Engine

- Added longitudinal Decision State protocol.
- Added Assumption and Evidence ledgers.
- Added calibrated/Bayesian belief-update safeguards.
- Added append-only Decision Journal and outcome records.
- Added kill/pivot/scale gates and review protocol.
- Added JSON state format + CLI engine.
- Added 40-case deterministic transition regression.
- Added explicit persistence boundary.

## 1.4.0 — Tool Trace Evaluation

- Added 42-case balanced synthetic tool-use benchmark.
- Added deterministic fake tool environment with decoys.
- Added Responses API function-calling live runner.
- Added trace evaluator for source choice, order, budget, redundancy, grounding, and stopping.
- Added read-before-write and synthetic action correctness checks.
- Added oracle smoke-test; no real user accounts are touched.

## 1.3.0 — Tool Orchestration Layer

- Added seven-route source-of-truth tool router.
- Added no-tool gate to prevent unnecessary retrieval.
- Added fresh-public, private-source, local-artifact, code-source, action-tool, and multi-source policies.
- Added source authority ladder and staleness protocol.
- Added read-before-write and external action guardrails.
- Added tool budget and tool stop rules.
- Added 60-case deterministic tool-routing regression suite.
- Added source-class shadow router and regression reporting.
- Added implicit code-source detection for requests such as “根据实际代码判断…”.

## 1.2.0 — Live A/B Evaluation

- Added frozen 30-case answer-quality benchmark.
- Added fair baseline and compiled Thinking OS evaluation profiles.
- Added blind randomized pairwise LLM grader.
- Added six-dimension weighted quality rubric.
- Added failure-label classification and promotion gates.
- Added token, latency, and estimated cost accounting.
- Added OpenAI Responses API live runner with environment-only API key handling.
- Added mock provider for zero-cost pipeline smoke tests.
- Added anti-overfitting and benchmark-freeze policy.
- Kept tool orchestration out of the headline benchmark to isolate reasoning quality.

## 1.1.0 — Router Regression & Anti-Overthinking

- Added router priority/de-escalation policy.
- Added explicit negative triggers for Red Team, First Principles, Premortem, Base Rate, and decomposition.
- Added deterministic shadow-router simulator.
- Added automated 100-case regression runner.
- Added routing failure taxonomy.
- Tuned critical gates to 100/100 on intent, evidence, red-team, action, and forbidden-model checks.
- Preserved soft-band scores as advisory to avoid test overfitting.

## 1.0.0 — Integrated Thinking OS

- Integrated router, challenge, evidence, domain, action, and evaluation layers.
- Added six domain packs: Business, Investment, Product, Code, Content, Research.
- Expanded evaluation suite to 100 cases.
- Finalized portable Agent Skills package structure.

## 0.8.0 — Evaluation Layer

- Expanded routing and adversarial regression suite.
- Added domain coverage and overthinking tests.
- Added eval schema/coverage validation.

## 0.5.0 — Action Engine

- Added bottleneck-first execution.
- Added Impact × Confidence ÷ Effort priority heuristic.
- Added Minimum Validation Action.
- Added feedback architecture, OODA, kill and scale criteria.

## 0.4.0 — Domain Packs

- Added Business, Investment, Product, Code, Content, and Research packs.
- Added two-domain maximum default to control context growth.

## 0.3.0 — Evidence Engine

- Added reasoning-vs-information gate.
- Added current/private evidence triggers.
- Added evidence labels, confidence, value-of-information, research stop rule.

## 0.2.0 — Red Team Engine

- Added strongest-plan steelman stage.
- Added ranked assumption map.
- Added premortem, falsification, tail-risk, and mitigation protocol.

## 0.1.0 — Router MVP

- Added Agent Skills-compatible `SKILL.md`.
- Added six-axis router.
- Added 20 core reasoning models and 6 recipes.
- Added stop rules and output protocols.
