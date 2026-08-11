# Tool Trace Evaluation Policy v1.4

v1.4 evaluates the **agent's tool-use trajectory**, not only the final prose.

A plausible final answer can still be a bad agent run if it used the wrong source of truth, called irrelevant tools, repeated calls, wrote before required reads, ignored tool output, or kept calling tools after the task was resolved.

## Metrics

1. **Route success** — correct source/tool class; `NO_TOOL` means zero calls.
2. **First-call precision** — the first call is a valid source-of-truth tool.
3. **Required-source recall** — all required sources are actually used.
4. **Forbidden-call avoidance** — no irrelevant/incorrect source is called.
5. **Redundant-call avoidance** — no equivalent completed call is repeated without decision value.
6. **Call-budget compliance** — tool calls remain inside the case budget.
7. **Read-before-write** — existing state is resolved before mutation when required.
8. **Action correctness** — correct synthetic mutation, target, and scope.
9. **Stop efficiency** — stop once the answer/action is sufficiently grounded.
10. **Final grounding** — final answer reflects returned tool data rather than invented facts.

## Trace pass gate

A case passes only when:
- route succeeds;
- all required sources are used;
- no forbidden tool is used;
- call budget passes;
- read-before-write passes when applicable;
- synthetic action correctness passes when applicable;
- final grounding passes.

First-call precision, redundancy, turns, tokens, latency, and cost remain optimization metrics.

## Fair A/B comparison

Baseline and Thinking OS must use the same:
- target model;
- reasoning effort;
- user prompt;
- exposed tools and descriptions;
- fixture data;
- max turns.

Change only the Thinking OS instruction condition.

## Synthetic environment

Core v1.4 uses deterministic synthetic tools, not the user's real accounts.

Benefits:
- reproducible hidden gold answers;
- zero real-world side effects;
- no private-data exposure;
- controlled decoy tools;
- exact mutation checking.

Real connected-tool acceptance tests should be a later layer.

## Promotion gates

Recommended:
- trace pass >= 90%;
- NO_TOOL false-positive rate <= 5%;
- first-call precision >= 90%;
- forbidden-call rate <= 2%;
- required read-before-write = 100%;
- synthetic action correctness = 100%;
- no material route-class regression;
- lower call count only counts as better when correctness/grounding still pass.

## Anti-gaming

Do not hardcode benchmark prompts. Fix general source-of-truth, action-scope, and stopping rules, then rerun the full frozen benchmark.
