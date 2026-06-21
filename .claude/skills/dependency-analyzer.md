---
name: dependency-analyzer
description: "Analyzes project dependencies, checks for outdated/vulnerable packages, suggests updates"
metadata:
  type: skill
  category: quality
  version: 1
---

# Dependency Analyzer

Checks project dependencies.

## What It Does

1. **Reads** package.json, requirements.txt, Cargo.toml, go.mod
2. **Checks** for outdated packages
3. **Scans** for known vulnerabilities (CVE database)
4. **Suggests** safe update paths
5. **Reports** license compatibility

## Output Format

```
📦 Dependencies Report

Outdated (12):
  react 17.0.0 → 18.3.0 (recommended)
  axios 0.27.0 → 1.7.0 (security fix)
  ...

Vulnerable (1):
  lodash@4.17.15 — CVE-2021-23337 (HIGH)
  Fix: upgrade to 4.17.21

License Issues (0):
  All compatible (MIT, Apache-2.0, BSD-3)
```

## Commands

- `/deps check` — full scan
- `/deps outdated` — just outdated
- `/deps vulnerable` — just security
- `/deps update <package>` — update one package

## Integration

Works with `code-review` and `security-review` skills.
