---
name: webapp-fullstack
description: "Preset for fullstack web app development (React/Vue/Svelte + FastAPI/Express + Postgres/SQLite)"
metadata:
  type: agent-preset
  version: 1
  stack:
    frontend: ["react", "vue", "svelte", "next"]
    backend: ["fastapi", "express", "django", "flask"]
    database: ["postgres", "sqlite", "mysql"]
  modelTier: "sonnet"
---

# Webapp Fullstack Preset

**Auto-configures the AI company for fullstack web app projects.**

## Detected Stack

Triggers when project has:
- `package.json` with React/Vue/Svelte/Next
- Backend in `web_app/`, `backend/`, `server/`, `api/`
- Database: SQLite/Postgres/MySQL

## Auto-Configured Agents

| Agent | Role | Tools |
|-------|------|-------|
| **Frontend Dev** | React/Vue components, state, routing | Sonnet + frontend-design skill |
| **Backend Dev** | API endpoints, auth, business logic | Sonnet |
| **DB Admin** | Schema, migrations, queries | Sonnet |
| **Auth Specialist** | JWT, sessions, OAuth | Sonnet + security-review |
| **UI Tester** | Playwright E2E | Sonnet + verify skill |
| **API Tester** | pytest, jest, supertest | Sonnet + verify skill |
| **Designer** | UI/UX, accessibility | Sonnet + frontend-design skill |

## Default Workflow

```
User Request → CTO (architecture) → parallel:
  - Frontend Dev (UI)
  - Backend Dev (API)
  - DB Admin (schema)
→ Designer (polish)
→ UI Tester (E2E)
→ API Tester (integration)
→ Security (audit)
→ Memory (update)
```

## Conventions

- **Frontend:** TypeScript, function components, Tailwind
- **Backend:** Type hints (Python) / TS, async-first
- **DB:** Migrations via Alembic / Prisma
- **Auth:** JWT with refresh tokens
- **Tests:** 80%+ coverage target
- **API:** REST with OpenAPI spec

## Pre-loaded Skills

- `frontend-design` (for UI)
- `code-review` (PR review)
- `verify` (run + screenshot)
- `simplify` (cleanup)
- `security-review` (audit)

## Pre-loaded Hooks

- PostToolUse (tool accuracy)
- Pre-commit (lint + format)
- Pre-push (test + type-check)

## Quick Start

```bash
# In a new project, set this preset:
echo "preset: webapp-fullstack" >> CLAUDE.md
claude --config .claude/settings.json
```

The system will auto-detect the stack and configure all agents.

## Example Plan

```markdown
# Plan: Add user authentication

Priority: P0 | Steps: 6 | Est. cost: $0.08

## Steps
1. CTO: Design auth system (JWT + refresh)
2. Backend Dev: Implement /auth/login, /auth/register, /auth/refresh
3. DB Admin: Add users, refresh_tokens tables + migration
4. Frontend Dev: Build login/register forms
5. UI Tester: E2E test for auth flow
6. Security: Audit for OWASP top 10

## Agents
- Auth Specialist (lead)
- Backend Dev
- Frontend Dev
- DB Admin
- Security
```
