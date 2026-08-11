# Security & Data Boundaries

## Secrets

Do not store API keys, access tokens, cookies, private keys, or passwords inside the Skill package.

Evaluation runners read credentials from the process environment when a live benchmark is explicitly run.

## Private data

Use the closest source of truth for user-specific data, but do not copy private source contents into permanent Decision State unless they are necessary.

Prefer:
- concise summaries;
- source references;
- decision-relevant facts.

## External actions

For mutations:
- preserve user scope;
- read before write when current state matters;
- avoid unnecessary destructive actions;
- verify completion when possible.

## Self-improvement

The Skill never silently promotes a candidate policy change.

Core behavior changes require:
- evidence;
- regression tests;
- rollback plan;
- explicit release decision.

## Persistence honesty

Never claim cross-session persistence unless the host provides actual durable storage.
