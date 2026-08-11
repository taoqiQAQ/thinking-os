# Thinking OS Skill v2.0

[English](README.md) | [中文](README.zh-CN.md)

Thinking OS is a portable [Agent Skill](https://agentskills.io/) that routes complex work to the minimum useful reasoning, evidence, challenge, decision-state, and action machinery. It is a reasoning router—not a single giant prompt.

## What it does

Thinking OS helps an agent decide:

1. whether structured reasoning is needed;
2. how deep to go;
3. which minimum set of models to use;
4. whether fresh, private, local, or repository evidence is required;
5. whether adversarial review adds value;
6. when to stop thinking and take the next action.

It intentionally avoids heavy frameworks for simple tasks and does not expose private chain-of-thought.

## Repository contents

This repository is the **v2.0.0 production runtime package**. It contains the files needed to use the skill:

```text
SKILL.md                 # Skill entry point and router
references/              # Detailed policies, models, domains, and protocols
scripts/                 # Runtime helper engines
state/                   # Decision-state JSON schemas
ARCHITECTURE.md          # System architecture
INSTALL.md               # Installation guidance
SECURITY.md              # Data and security boundaries
RELEASE.md               # Release status and offline gates
CHANGELOG.md             # Version history
MANIFEST.json            # File inventory and hashes
```

The production package intentionally excludes development-only evaluation suites, benchmark fixtures, generated runs, and release tooling. Those assets are not required at runtime.

## Installation

Clone the repository and keep the directory name `thinking-os`:

```bash
git clone https://github.com/taoqiQAQ/thinking-os.git
```

Copy the `thinking-os` folder into the Skills location supported by your Agent-Skills-compatible host. The folder must contain `SKILL.md` at its top level.

The release archive `thinking-os-skill-v2.0.0.zip` uses the same folder layout with a `thinking-os/` wrapper directory.

## Invocation

Normally let the host activate the skill automatically. You can also say:

- `Use thinking-os for this decision.`
- `Use thinking-os /red on this plan.`
- `Use thinking-os /action; stop analyzing and give me the execution path.`

Supported mode overrides include `/fast`, `/deep`, `/max`, `/red`, `/first`, `/data`, `/idea`, `/action`, and `/simple`.

## Validation

The runtime helpers use only Python's standard library. From the repository root:

```bash
python3 -m py_compile scripts/decision_state.py scripts/improvement_engine.py
```

The v2.0.0 release is offline-regression validated. Live A/B quality or tool-use proof requires a separately authorized run and is not claimed by this package.

## Design principles

- Think only when thinking improves the decision.
- Research only when information can change the decision.
- Challenge only when challenge can reduce meaningful risk.
- Act when reality can teach more than further analysis.
- Never claim persistence unless the host provides durable storage.
- Never silently promote self-improvement changes into production rules.

See [`SKILL.md`](SKILL.md) for the runtime entry point and [`ARCHITECTURE.md`](ARCHITECTURE.md) for the full design.

## License

Released under the [MIT License](LICENSE).
