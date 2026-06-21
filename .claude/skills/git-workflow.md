---
name: git-workflow
description: "Git workflow automation — conventional commits, branch management, PR templates, changelog generation"
metadata:
  type: skill
  category: development
  version: 1
---

# Git Workflow Skill

Automates git workflows with conventional commits, branching, and changelogs.

## Features

- Enforces conventional commit format (feat, fix, docs, refactor, etc.)
- Auto-generates CHANGELOG from commit history
- Branch naming conventions
- PR template generation

## Commit Format

```
<type>(<scope>): <description>

[optional body]
[optional footer]
```

Types: feat, fix, docs, style, refactor, perf, test, chore, ci, feat

## Commands

- `conventional-commit` — Format your last commit properly
- `generate-changelog` — Create CHANGELOG.md from git log
- `branch <type>/<description>` — Create a properly named branch
- `pr-body` — Generate PR description from commits
