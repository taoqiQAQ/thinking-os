# Thinking OS v2.0 Architecture

Thinking OS is a **cognitive control layer**, not one giant prompt.

## Runtime layers

1. **Intent / Depth Router**
   - intent
   - complexity
   - risk
   - uncertainty
   - reversibility
   - evidence need

2. **Reasoning Selection**
   - 20 core reasoning models
   - recipes
   - minimal-model budget
   - anti-overthinking policy

3. **Domain Adaptation**
   - Business
   - Investment
   - Product
   - Code
   - Content
   - Research

4. **Evidence & Tool Orchestration**
   - NO_TOOL
   - fresh public
   - private source
   - local artifact
   - code source
   - action tool
   - multi-source

5. **Challenge**
   - assumption check
   - Red Team
   - Premortem
   - Falsification
   - tail-risk review

6. **Action & Stop**
   - bottleneck
   - 80/20
   - Minimum Validation Action
   - OODA
   - kill / scale criteria
   - analysis stop rules

7. **Decision State**
   - Assumption Ledger
   - Evidence Ledger
   - probability/confidence updates
   - Decision Journal
   - reviews and outcomes

8. **Controlled Self-Improvement**
   - incident capture
   - failure taxonomy
   - pattern gate
   - candidate rule change
   - regression gate
   - explicit promotion / rollback

## Design principle

The runtime should expose the **answer, decision, evidence, risk, and action**—not a parade of framework names.

Use the minimum reasoning/tool/state machinery that materially improves the user outcome.

## Production vs source package

The v2.0 production package contains only runtime material:
- `SKILL.md`
- `references/`
- runtime state schemas
- runtime helper engines
- release/use documentation

The source package additionally contains:
- frozen eval suites
- benchmark fixtures
- regression scripts
- smoke results
- development configuration
- release/audit tooling
