---
name: sentry-monitor
description: "Monitors Sentry errors, groups similar ones, suggests fixes, creates PRs"
metadata:
  type: skill
  category: monitoring
  version: 1
---

# Sentry Monitor

Proactive error monitoring and remediation.

## What It Does

1. **Polls** Sentry for new errors
2. **Groups** similar errors by stack trace fingerprint
3. **Prioritizes** by frequency + user impact
4. **Suggests** fixes using AI
5. **Creates** PR with the fix (with your approval)

## Commands

- `sentry-monitor poll` — check now
- `sentry-monitor watch` — continuous
- `sentry-monitor fix <issue-id>` — auto-fix
- `sentry-monitor stats` — show error trends

## Auto-Triage

- Top 1% errors → P0 (auto-create ticket)
- Top 5% errors → P1
- New errors → P2
- Recurring → P1
- Resurfaced → P0

## Integration

- Reads `fact-bug-*.md` for known fixes
- Suggests fixes based on past resolutions
- Never auto-merges PRs (requires human approval)