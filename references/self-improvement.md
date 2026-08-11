# Self-Improvement Engine v1.6

Thinking OS does not "learn" by rewriting itself after every bad answer.

It improves through **controlled, evidence-backed change management**:

`Incident → Triage → Pattern → Root Cause → Candidate Change → Counterfactual Test → Regression → Promotion Review → Release → Monitor / Rollback`

The goal is to improve general behavior while minimizing benchmark gaming, overfitting, and regressions.

## Constitution

1. **One bad answer is not automatically a rule problem.**
2. **Do not patch prompt wording. Fix the general failure mechanism.**
3. **A change must predict both benefits and possible regressions.**
4. **Frozen regression suites outrank anecdotal improvement.**
5. **Quality gains do not justify critical safety, action, state-integrity, or source-of-truth regressions.**
6. **The system may propose a change; it does not silently promote its own core rules.**
7. **Every promoted change must be reversible and versioned.**
8. **If evidence is insufficient, collect more incidents instead of changing policy.**

## Stage 1 — Capture incident

Create an Improvement Incident only when something materially failed or nearly failed.

Record:
- incident ID;
- task fingerprint / prompt summary;
- failure class;
- severity;
- affected layer;
- expected behavior;
- observed behavior;
- evidence;
- whether the final outcome is known;
- candidate pattern key.

Do not store private raw content when a concise redacted summary is enough.

Schema: [../state/improvement-record.schema.json](../state/improvement-record.schema.json)

## Stage 2 — Triage

Classify the failure using [failure-taxonomy-v1.6.md](failure-taxonomy-v1.6.md).

Severity:

- `P0` — critical: safety, destructive action, severe privacy/security, irreversible material harm.
- `P1` — major: wrong consequential recommendation/action/source, material state corruption.
- `P2` — moderate: task failure, significant over/underthinking, wrong routing, avoidable tool waste.
- `P3` — minor: style/format/verbosity issues that do not materially change outcome.

## Stage 3 — Pattern gate

Before modifying a general rule, require one of:

### Normal pattern
- at least **3 incidents**;
- at least **2 distinct prompt forms**;
- same plausible root mechanism;
- failure is reproducible or supported by evals.

### Critical escalation
A single `P0` or strong `P1` may immediately enter investigation and mitigation.

Critical escalation does **not** mean automatic promotion. It means faster investigation, temporary guardrails, and targeted regression.

## Stage 4 — Root cause

Do not stop at the visible symptom.

Separate:
- task-specific accident;
- ambiguous input;
- missing evidence/tool;
- model capability limit;
- bad Router trigger;
- bad de-escalation rule;
- bad domain rule;
- bad tool/source rule;
- bad stop rule;
- bad state/update rule;
- evaluator/benchmark bug.

If the benchmark is wrong, fix the benchmark and preserve that change in the changelog.

## Stage 5 — Candidate change

A change proposal must contain:

- `proposal_id`
- `pattern_key`
- `target_layer`
- `target_files`
- `current_rule`
- `proposed_rule`
- `general_rationale`
- `supporting_incident_ids`
- `expected_improvements`
- `predicted_regression_risks`
- `required_eval_suites`
- `rollback_plan`

Reject:
- exact prompt patches;
- changes with no general mechanism;
- changes that cannot be evaluated;
- changes with no rollback path.

See [change-control.md](change-control.md).

## Stage 6 — Counterfactual test

Before changing the production Skill, ask:

> If this candidate rule had existed, would it likely have prevented the incidents without damaging nearby cases?

Test at least:
- the failing cases;
- semantically similar non-failing cases;
- the opposite behavior (negative controls).

## Stage 7 — Regression gate

Run all affected frozen suites.

Minimum core suites when a core Router/policy changes:

- v1.1 Router regression
- v1.3 Tool routing regression
- v1.5 Decision State regression

Add:
- v1.2 answer-quality A/B when live credentials are available and answer quality is affected;
- v1.4 Tool Trace when tool behavior is affected;
- domain-specific suites when domain policy changes.

A candidate cannot be promoted if a required deterministic integrity suite fails.

## Stage 8 — Promotion gate

A candidate becomes `ready_for_review` only when:

- pattern gate passed;
- root cause is plausible and documented;
- required offline suites pass;
- no critical regression is introduced;
- target failure metric improves or a critical failure is eliminated;
- rollback is defined.

Live quality promotion should also satisfy the corresponding v1.2/v1.4 metrics when those runs are available.

The engine does **not** silently mark core-policy changes as production-promoted. Final promotion is an explicit release decision.

## Stage 9 — Release

When approved:
- increment version;
- update CHANGELOG;
- preserve prior package;
- freeze benchmark configuration;
- record proposal ID in release notes.

## Stage 10 — Monitor and rollback

After release:
- collect new incidents;
- compare failure rates;
- watch for predicted regressions;
- rollback if a critical regression appears or the expected improvement does not survive real tasks.

## Anti-overfitting rules

- Do not add a keyword rule for one exact sentence.
- Require semantic diversity in supporting incidents.
- Include negative controls.
- Keep a frozen benchmark and a separate holdout set where practical.
- Prefer the smallest general rule change.
- A benchmark score increase is not enough if real failure rate worsens.
- Do not tune evaluator criteria after seeing candidate scores unless the evaluator itself is demonstrably wrong.

## Output

For a detected pattern:

- Pattern
- Evidence count
- Root-cause hypothesis
- Candidate change
- Expected gain
- Regression risk
- Required tests
- Promotion status

Avoid saying "the system learned this" until the rule is actually approved and released.
