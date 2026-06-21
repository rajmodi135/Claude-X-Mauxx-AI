---
name: cost-optimizer
description: "Track API spend in real-time. Auto-switch to cheaper models when budget tight. Daily/monthly limits with auto-throttle."
metadata:
  type: skill
  category: cost-optimization
  version: 1
  costImpact: high
---

# Cost Optimizer Skill

**Auto-loaded on session start.** Real-time spend tracking and auto-throttling.

## Tracks

- Tokens in/out per turn
- Model used per turn
- Cost per turn (calculated from model pricing)
- Cumulative cost (session, day, month)
- Cost per task (group of turns)

## Files

- `state/cost-tracker.md` — current session cost
- `state/cost-daily.md` — daily breakdown
- `state/cost-monthly.md` — monthly total

## Pricing (per 1M tokens, in/out)

```yaml
haiku:   { in: 0.25, out: 1.25 }
sonnet:  { in: 3.00, out: 15.00 }
opus:    { in: 15.00, out: 75.00 }
ollama:  { in: 0, out: 0 }
cache:   { factor: 0.10 }  # 90% off
```

## Budget Tiers

| Tier | Monthly Limit | Action |
|------|---------------|--------|
| Free | $5 | All non-critical on Haiku/Ollama |
| Standard | $50 | Default mix |
| Pro | $200 | Allow more Opus |
| Unlimited | — | Use Opus freely |

## Auto-Throttle

When monthly spend hits:

- **50% ($25)**: Log warning, suggest switching non-critical to Haiku
- **80% ($40)**: Auto-switch non-critical to Haiku, defer Opus tasks
- **95% ($47.5)**: Hard-cap Opus, use Sonnet for everything
- **100% ($50)**: Hard stop non-critical, queue for next month

## Cost Output

Every cost-bearing action displays:
```
💰 Sonnet · 1.5K in / 800 out · $0.020 · today: $0.45
```

## Tracking Format

`state/cost-tracker.md`:
```markdown
---
name: state-cost-tracker
description: Real-time API spend tracking
metadata:
  type: state
  version: 47
---

# Cost Tracker

## Session: $0.234

| Time | Task | Model | In/Out | Cost |
|------|------|-------|--------|------|
| 14:30 | classify intent | haiku | 200/50 | $0.0001 |
| 14:31 | edit auth.py | sonnet | 1500/800 | $0.017 |
| 14:32 | design system | opus | 3000/2000 | $0.195 |

## Today: $1.45 / $5.00 (29%)

## This Month: $12.34 / $50.00 (25%)

## Model Mix

- Haiku:  60% (target: 70%)  ✓
- Sonnet: 30% (target: 25%)  ✓
- Opus:   10% (target: 5%)   ⚠ slightly high
```

## Integration

- `model-router` skill: provides the cost per choice
- `PostToolUse` hook: logs cost per turn
- `state-resource-budget.md`: shows cost alongside context/RAM

## Commands

- `/cost` — show current spend
- `/cost today` — show today's breakdown
- `/cost month` — show monthly
- `/cost set $X` — set custom monthly limit

---

💰 **Result: Spend under control, with full visibility.**
