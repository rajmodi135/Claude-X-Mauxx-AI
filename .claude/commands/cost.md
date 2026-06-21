# /cost — Show Spending Report
# Invoke: /cost

Shows API spending breakdown.

## Usage

```
/cost                — current session
/cost today          — today's breakdown
/cost week           — this week
/cost month          — this month
/cost set $50        — set monthly budget
/cost alert $40      — set alert threshold
```

## Data Source

Reads from `memory/state-cost-tracker.md`. Uses `scripts/cost-tracker.mjs` for analysis.
