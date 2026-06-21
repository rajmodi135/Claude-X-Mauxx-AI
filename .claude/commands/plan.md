# Claude x Mauxx AI — Show Active Plans
# Invoke: /plan

Shows all active plans from memory.

## What It Does
1. Reads memory/MEMORY.md Active Plans table
2. Reads memory/state-priority-queue.md for queue order
3. For each plan, reads the plan-*.md file's first section (title, status, priority, ETA)
4. Displays a summary table

## Format
| # | Plan | Status | Priority | Steps Done | ETA |
|---|---|--------|----------|------------|-----|
| 1 | [[plan-agent-skills]] | Step 3/5 | P0 | ⬜⬜✅✅⬜ | 2026-06-23 |

## Usage
```
/plan                 — list all active plans
/plan <name>          — show full plan detail
/plan archive <name>  — archive a completed plan
```
