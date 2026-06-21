---
name: db-migration
description: "Database migration generator and runner. Supports Prisma, Alembic, Flyway, Knex, Drizzle."
metadata:
  type: skill
  category: database
  version: 1
---

# Database Migration

Migration generator and runner.

## Supported

| Stack | Tool |
|-------|------|
| Prisma | prisma migrate |
| Alembic (Python) | alembic revision |
| Drizzle | drizzle-kit |
| Knex | knex migrate |
| Flyway (Java) | flyway migrate |
| golang-migrate | migrate up |

## What It Does

1. Detects schema changes (Prisma schema, SQLAlchemy models, etc.)
2. Generates migration file
3. Reviews for safety (destructive changes warning)
4. Runs migration (dev/staging)
5. Generates rollback
6. Logs to `state/migrations.md`

## Commands

- `db-migration generate` — make new migration
- `db-migration up` — run pending
- `db-migration down` — rollback
- `db-migration status` — show pending
- `db-migration seed` — load test data

## Safety

- Always asks before destructive (DROP TABLE, etc.)
- Backs up DB before migration
- Tests on staging first
- Never runs on production without approval