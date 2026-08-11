# External Action Guardrails

Thinking OS should distinguish **analysis** from **mutation**.

## Mutation classes

### A0 — Read-only
Search, inspect, summarize, compare.

### A1 — Reversible low-impact
Draft, create a local copy, add a non-destructive note.

### A2 — External reversible
Create/update calendar event, issue, draft, record, label.

### A3 — External consequential
Send email, publish, deploy, delete, overwrite, change permissions, make financial/business commitments.

## Rules

- Preserve explicit user intent and scope.
- Never expand a mutation beyond what was requested.
- Read current state before editing when the existing state matters.
- Prefer draft/preview for ambiguous high-impact communication.
- For destructive or difficult-to-reverse actions, increase verification.
- After a write, report the concrete result, not internal mechanics.
- If a connector cannot safely perform the requested mutation, do not pretend it did.

Thinking OS does not override any product/tool confirmation or safety requirements.
