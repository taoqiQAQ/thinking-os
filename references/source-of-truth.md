# Source-of-Truth Map

This reference helps route information before selecting a specific connector/tool.

| User need | Preferred source class | Avoid |
|---|---|---|
| Current public fact | FRESH_PUBLIC | model memory if freshness matters |
| User's meetings | PRIVATE_SOURCE / calendar | web |
| User's email | PRIVATE_SOURCE / email | web, memory |
| User's document content | PRIVATE_SOURCE or LOCAL_ARTIFACT | generic web |
| Attached PDF/image/file | LOCAL_ARTIFACT | guessing from filename |
| Repository/CI/PR state | CODE_SOURCE | generic tutorials first |
| Current package/API docs | FRESH_PUBLIC, official docs | stale memory |
| User asks to send/change/create | ACTION_TOOL | only giving manual steps if safe tool is available |
| Conceptual reasoning | NO_TOOL | unnecessary search |
| Creative writing/design brief | NO_TOOL unless current references are requested | evidence gathering by default |
| Multi-source meeting prep | MULTI_SOURCE: calendar + docs/email | broad web unless external context is needed |
| Current travel plan | FRESH_PUBLIC, sometimes MULTI_SOURCE | stale general knowledge |

## Authority ladder

Prefer, when relevant:

1. direct source of truth;
2. official/primary source;
3. authoritative specialist;
4. reputable secondary synthesis;
5. community experience;
6. general memory/heuristic.

The ladder is not absolute. Community sources may be primary for subjective experience, and private user data is primary for the user's own state.
