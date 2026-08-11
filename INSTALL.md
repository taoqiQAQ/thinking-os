# Installation

Thinking OS follows the Agent Skills folder pattern.

## Production package

Unzip `thinking-os-skill-v2.0.0.zip`.

Keep the root folder name:

```text
thinking-os/
  SKILL.md
  references/
  state/
  scripts/
```

Install or copy that `thinking-os` folder into the Skills location supported by your Agent-Skills-compatible host.

## Source/development package

Use `thinking-os-source-v2.0.0.zip` when you want to:
- run regression suites;
- inspect benchmark cases;
- change Router/domain/tool/state policies;
- prepare a future release.

## Sanity check

A valid runtime package must have:
- `thinking-os/SKILL.md`
- YAML frontmatter `name: thinking-os`
- version `2.0.0`
- no broken local links from `SKILL.md`
- no secrets
- no `evals/` or benchmark run data in the production build

## State persistence

Thinking OS does not create durable memory by itself.

Decision State persists only when the host actually stores it in a file, repository, database, document, or supported memory mechanism.
