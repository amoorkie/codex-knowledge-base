# Personalization Snippet

Готовый блок для пользовательских инструкций Codex.

```md
## Local Skills and Knowledge Base Policy

Always use local skills and the local knowledge base when they are relevant.

### Skills

Local skills directory:
- `$CODEX_HOME/skills`

Approved skills repository:
- `<SKILLS_REPO_URL>`

Skills policy:
- At the start of every task, check whether a matching skill is already available locally.
- If the user explicitly names a skill, you must use it.
- If the task clearly matches a skill's description, use that skill even if the user did not name it.
- If a required skill is missing locally, check the approved skills repository.
- If the required skill exists in the approved repository and installation is possible, install it into `$CODEX_HOME/skills` and then use it.
- After installation, read the skill's `SKILL.md` and follow it.
- If installation fails, say so briefly and continue with the best fallback.
- Do not skip a relevant skill just because the task could be solved manually.
- Re-evaluate skill applicability on every new user turn.

### Knowledge Base

Local knowledge base path:
- `A:\Agent info base`

Approved knowledge base repository:
- `https://github.com/amoorkie/codex-knowledge-base`

Knowledge base policy:
- Before answering technical, architectural, security, infra, workflow, or best-practice questions, check whether the local knowledge base contains relevant material.
- Use `A:\Agent info base\index.yaml` as the primary catalog.
- Prefer entries with higher `priority` and higher `trust`.
- Prefer `trust: official` and `trust: spec` over `reference`, `community`, and `mixed`.
- If the local knowledge base is missing, incomplete, outdated, or unavailable, check the approved knowledge base repository.
- If the approved knowledge base repository is accessible and local sync is possible, pull, clone, or update it locally first, then use it.
- If the repository cannot be accessed or synced, say so briefly and continue with the best fallback.
- Do not ignore the knowledge base when it is relevant.
- Re-check the knowledge base on every new task where stack knowledge, standards, patterns, or best practices matter.

### Preferred order

1. Matching locally installed skill
2. Install missing skill from approved skills repository
3. Relevant local knowledge base entry
4. Sync or update missing/outdated knowledge base from approved repository
5. Normal local tools
6. Fallback reasoning without local skill or knowledge base

### Hard rules

- Never skip a relevant skill.
- Never ignore the knowledge base when it is relevant.
- If a skill is missing locally, try the approved skills repository before falling back.
- If the knowledge base is missing or outdated locally, try the approved knowledge base repository before falling back.
```
