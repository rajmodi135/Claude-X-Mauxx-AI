---
name: accuracy-monitor
description: "Real-time tool accuracy tracking with auto-unlock at 85%/90%/95%/98%. Monitors per-tool, per-agent success rates."
metadata:
  type: skill
  category: monitoring
  version: 1
---

# Accuracy Monitor Skill

**Auto-loaded on session start.** Tracks tool accuracy and auto-unlocks new tools.

## How It Tracks

Every tool call is logged via `PostToolUse` hook:
```json
{
  "timestamp": "2026-06-22T14:30:00Z",
  "tool": "Edit",
  "agent": "dev-team",
  "result": "success|failure",
  "context": "src/auth/login.py:L42",
  "duration_ms": 234,
  "error": null
}
```

Aggregated in `state/tool-accuracy.md` (rolling 100 uses per tool).

## Unlock Thresholds

| Tier | Threshold | New Tools Unlocked |
|------|-----------|-------------------|
| 1 (Basics) | Always | Read, Write, Edit, Glob, Grep, Bash basics |
| 2 (85%) | 85% sustained 30 uses | MultiEdit, code-review, deep-research |
| 3 (90%) | 90% sustained 30 uses | WebFetch, WebSearch, Workflow, advanced Bash |
| 4 (95%) | 95% sustained 30 uses | security-review, perf, multi-agent at scale |
| 5 (98%) | 98% sustained 30 uses | Self-modifying, custom tool creation |

## Sustained Check

A tool only unlocks if the last 30 uses are ALL ≥ threshold (no recent failures).

## Auto-Unlock Flow

1. Accuracy monitor sees tool crossed threshold
2. Verifies last 30 uses all ≥ threshold
3. Logs to `state/tool-accuracy.md` → "Recently Unlocked"
4. Creates `fact-tool-unlocked-<tool>.md`
5. Notifies CEO in next turn
6. Adds tool to allow-list (auto-enables it)

## Dashboard

`/accuracy` shows:

```
═══════════════════════════════════════════════════════
  Tool Accuracy Dashboard
═══════════════════════════════════════════════════════

  Per-Tool (last 100 uses)
  
  Tool          Agent       Acc   Tier   Next Unlock
  ──────────────────────────────────────────────────
  Edit          dev-team   94%   2→3   95% → Tier 3 ⚠
  Write         dev-team   99%   2→3   95% → Tier 3 ✓ UNLOCK
  Bash          qa         87%   1→2   85% → Tier 2 ✓ UNLOCK
  Read          dev-team   99%   1     (no unlock)
  Grep          dev-team   96%   1→2   85% → Tier 2 ✓ UNLOCK
  
  Recently Unlocked
  ──────────────────────────────────────────────────
  🎉 Write unlocked (T2→T3) — 2026-06-22 14:30
  🎉 Bash unlocked (T1→T2) — 2026-06-22 13:15
  
  Currently Active Tiers
  ──────────────────────────────────────────────────
  Tier 1: ✅ Read, Write, Edit, Glob, Grep, Bash
  Tier 2: ✅ code-review, deep-research
  Tier 3: ⏳ 2 tools at 90% threshold
  Tier 4: 🔒 need 95% on Tier 3 first
═══════════════════════════════════════════════════════
```

## Trending

- `↗ rising` — accuracy improving last 20 uses
- `↘ falling` — accuracy dropping (auto-pause + review)
- `→ stable` — no change

## Alerts

- If accuracy drops below 70% for any tool → auto-pause + alert
- If accuracy drops below 50% → emergency: create bug fact, escalate

## Integration

- `PostToolUse` hook writes to `logs/accuracy.log`
- Aggregator updates `state/tool-accuracy.md` every 10 uses
- `Innovation Lead` agent reviews and unlocks

---

📊 **Result: Self-improving system that earns new tools as it proves itself.**
