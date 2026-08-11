# Failure Taxonomy v1.6

Use the narrowest class that explains the **mechanism**, not merely the symptom.

## Routing / depth

- `WRONG_INTENT` — primary task type was misclassified.
- `DOMAIN_MISROUTE` — wrong domain pack or domain assumptions.
- `OVERTHINKING` — analysis depth/structure exceeded decision value.
- `UNDERTHINKING` — insufficient depth for consequence/uncertainty.
- `STOP_FAILURE` — continued analysis/tooling after additional work had low value.
- `NO_CLEAR_RECOMMENDATION` — decision task ended without a usable choice/rule.
- `NO_NEXT_ACTION` — action was expected but not made concrete.

## Evidence / calibration

- `EVIDENCE_MISS` — decision-critical evidence was not sought/used.
- `WRONG_SOURCE` — evidence came from a lower/wrong source of truth.
- `FALSE_CERTAINTY` — confidence exceeded evidence.
- `DUPLICATE_EVIDENCE` — dependent/repeated evidence was over-counted.

## Challenge

- `RED_TEAM_FALSE_POSITIVE` — adversarial review added no meaningful value.
- `RED_TEAM_FALSE_NEGATIVE` — meaningful failure path was not challenged.
- `STRAWMAN_CHALLENGE` — attacked a weaker version of the plan.

## Tools / actions

- `TOOL_OVERUSE` — unnecessary calls or fan-out.
- `TOOL_UNDERUSE` — required tool/source was not used.
- `TOOL_WRONG_FIRST_CALL` — first call ignored the nearest source of truth.
- `TOOL_REPEAT` — redundant equivalent calls.
- `READ_BEFORE_WRITE` — mutated before resolving required current state.
- `ACTION_SCOPE` — external action exceeded or missed requested scope.
- `ACTION_NOT_VERIFIED` — write/action completed without available verification when material.

## Decision state

- `STATE_DRIFT` — current state diverged from auditable history without a valid transition.
- `HINDSIGHT_REWRITE` — old forecast/assumption was rewritten after outcome.
- `OVER_UPDATE` — belief changed too much for evidence quality/independence.
- `UNDER_UPDATE` — material evidence failed to change belief.
- `CRITERION_DRIFT` — kill/scale threshold moved after result without explicit supersession.
- `STALE_STATE` — decision used state/evidence known to be outdated when refresh mattered.

## Evaluation / infrastructure

- `EVAL_BUG` — benchmark/judge/test expectation is wrong.
- `PARSER_BUG` — trace/state/result parsing produced an incorrect evaluation.
- `CAPABILITY_LIMIT` — failure is primarily a model/tool capability limitation rather than a policy defect.
- `AMBIGUOUS_INPUT` — task cannot be reliably resolved without missing user/source information.

## Rule

Do not force every bad outcome into a Thinking OS policy failure.

A bad outcome can occur after a good process.
