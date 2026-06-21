---
name: git-hooks
description: "Manages git hooks for the project — pre-commit, pre-push, post-merge. Auto-installs standard hooks."
metadata:
  type: skill
  category: git
  version: 1
---

# Git Hooks Manager

Manages git hooks for projects.

## Standard Hooks

- **pre-commit** — lint, format, test fast
- **pre-push** — full test, type-check
- **post-merge** — install deps, regenerate
- **commit-msg** — conventional commit format

## Usage

- `git-hooks install` — install all standard hooks
- `git-hooks uninstall` — remove all
- `git-hooks status` — show installed hooks
- `git-hooks add <name>` — add custom hook

## What They Do

```
pre-commit:
  ✓ Prettier/Black formatting
  ✓ ESLint/Flake8 linting
  ✓ Type check (tsc/mypy --strict)
  ✓ Fast unit tests (<30s)
  ✓ Conventional commit message check

pre-push:
  ✓ Full test suite
  ✓ Build
  ✓ Security scan (Snyk/Trivy)
  ✓ License check

post-merge:
  ✓ npm/pip install
  ✓ Migrations
  ✓ Generate types
```