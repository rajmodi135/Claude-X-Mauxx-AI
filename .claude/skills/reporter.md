---
name: reporter
description: "Generates daily/weekly progress reports from memory, plan status, and cost logs"
metadata:
  type: skill
  category: reporting
  version: 1
---

# Reporter Skill

Periodic progress reports.

## Report Types

| Type | Frequency | Content |
|------|-----------|---------|
| Daily | Every day | Plans completed, issues, accuracy, cost |
| Weekly | Every Monday | Weekly progress, trends, insights |
| Monthly | 1st of month | Monthly summary, budget, velocity |
| On-demand | /report | Custom report |

## Data Sources

- memory/state-tool-accuracy.md
- memory/state-cost-tracker.md
- memory/archive-*.md
- memory/plan-*.md
- logs/accuracy.log

## Commands

- `/report daily` — Show daily report
- `/report weekly` — Show weekly report
- `/report monthly` — Show monthly report
- `/report custom <start> <end>` — Custom date range
