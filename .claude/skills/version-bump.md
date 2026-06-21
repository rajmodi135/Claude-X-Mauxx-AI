---
name: version-bump
description: "Auto-bumps version using semver. Updates package.json, CHANGELOG.md, creates git tag, pushes release."
metadata:
  type: skill
  category: release
  version: 1
---

# Version Bump

Automates semver version bumps.

## Bump Types

- `patch` (1.0.0 → 1.0.1) — bug fixes
- `minor` (1.0.0 → 1.1.0) — new features
- `major` (1.0.0 → 2.0.0) — breaking changes

## What It Does

1. Reads current version from package.json
2. Bumps per type
3. Updates package.json + CHANGELOG.md
4. Creates git commit + tag
5. Pushes to GitHub (triggers release workflow)
6. Optionally publishes to npm

## Usage

- `version-bump patch` — bump patch version
- `version-bump minor` — bump minor version
- `version-bump major` — bump major version
- `version-bump --dry-run` — preview changes

## Integration

Works with `git-workflow` (conventional commits) to auto-detect bump type from commit messages.