# Recipes v0.1

Recipes are defaults, not mandatory chains. Drop any step that does not add value.

## RCP01 — Direct / Simple

Use when: C0–C1, R0–R1.

Flow:
1. Answer directly.
2. Add one caveat only if material.
3. No red team.

Model budget: 0–1.

## RCP02 — Diagnosis

Use when: something is failing or a metric changed.

Flow:
1. M05 Issue Tree
2. M03 Five Whys on the highest-signal branch
3. M07 TOC if the problem is throughput/capacity related
4. Define discriminating test
5. Fix → verify

Model budget: 1–3.

## RCP03 — Important Decision

Use when: meaningful resources or trade-offs are involved.

Flow:
1. M01 Reframe if needed
2. M09 Base Rate
3. M10 Probability
4. M11 Expected Value
5. M12 Opportunity Cost
6. M14 Reversibility
7. M15 Red Team only if risk/irreversibility warrants it
8. M19 MVA if a test can reduce uncertainty

Model budget: 3–6.

## RCP04 — Build a Project

Use when: planning a multi-stage project.

Flow:
1. Define outcome + acceptance criteria
2. M04 MECE decomposition
3. Dependencies / critical path
4. M07 TOC
5. M08 80/20
6. First executable milestone
7. Feedback checkpoint

Model budget: 2–5.

## RCP05 — Evaluate an Existing Plan

Use when: user already has a plan and wants review.

Flow:
1. M18 Key Assumption Check
2. M15 Red Team
3. M16 Premortem if consequential
4. M17 Falsification
5. Keep / modify / reject
6. Mitigation + next validation

Model budget: 2–5.

## RCP06 — Explore a New Direction

Use when: direction is uncertain.

Flow:
1. M01 Problem Reframing
2. M02 First Principles when conventions constrain options
3. Generate 3–5 distinct options
4. M08 80/20 to select promising tests
5. M19 MVA
6. Move into OODA after first real evidence

Model budget: 2–4.

## Combination rules

- Reversibility can **reduce** the need for analysis.
- High risk + low reversibility can **increase** the evidence and challenge bar.
- Base rate should usually precede inside-view storytelling in forecasts.
- Red Team should usually follow a coherent proposal, not replace proposal generation.
- MVA should target the uncertainty most likely to change the decision.
