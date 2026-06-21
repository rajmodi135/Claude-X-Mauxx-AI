---
name: auto-commit
description: "Auto-commit code changes with conventional commit messages based on diff analysis"
metadata:
  type: skill
  category: git
  version: 1
---

# Auto-Commit Skill

Automatically commit changes with smart conventional commit messages.

## What It Does

1. Analyzes `git diff` for changes
2. Detects intent (feat, fix, refactor, etc.)
3. Generates conventional commit message
4. Commits with `-m` flag

## Usage

- `auto-commit` — commit all changes
- `auto-commit staged` — only staged
- `auto-commit push` — commit + push

## Examples

```
$ auto-commit
✓ Detected 5 file changes
✓ Type: feat (new feature in src/auth/login.ts)
✓ Committed: feat(auth): add rate-limited login with exponential backoff
```

## Integration

Works with git-workflow skill for changelog generation.
