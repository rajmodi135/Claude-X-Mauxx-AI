---
name: github-monitor
description: "Monitor GitHub repos for issues, PRs, releases. Auto-triage and respond."
metadata:
  type: skill
  category: integration
  version: 1
---

# GitHub Monitor

Monitors your GitHub repos and auto-responds.

## What It Does

1. **Polls** GitHub for new issues, PRs, releases
2. **Triages** new issues using AI (labels, priority)
3. **Responds** to common questions automatically
4. **Notifies** you on P0 issues via Telegram/Slack
5. **Generates** weekly digests

## Commands

- `gh-monitor watch <repo>` — start monitoring
- `gh-monitor stop <repo>` — stop
- `gh-monitor triage <issue>` — manually triage
- `gh-monitor digest` — show weekly digest

## Triage Categories

- bug (P0/P1 based on impact)
- feature-request
- question
- documentation
- duplicate
- needs-info

## Auto-Response Templates

- "How to install" → installation steps
- "How to use X" → doc link
- "Build error" → common fixes
- "Already fixed in v2.x" → upgrade instructions