---
name: doc-generator
description: "Generates documentation from source code. Auto-creates JSDoc, docstrings, README, API docs."
metadata:
  type: skill
  category: documentation
  version: 1
---

# Documentation Generator

Auto-generates documentation from source.

## What It Generates

| Source | Output |
|--------|--------|
| Python functions | Google-style docstrings |
| TypeScript functions | JSDoc comments |
| OpenAPI spec | Interactive docs (Swagger UI) |
| Markdown files | Consistent formatting |
| Code comments | API reference |

## Commands

- `/doc generate` — generate all missing docs
- `/doc <file>` — doc a specific file
- `/doc api` — generate OpenAPI from FastAPI/Express
- `/doc readme` — generate README from code
- `/doc changelog` — from git log

## Integration

- Pre-commit hook (auto-format)
- Pre-PR hook (generate diff)
- Daily cron (full scan)
