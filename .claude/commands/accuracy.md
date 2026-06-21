# Claude x Mauxx AI — Tool Accuracy Stats
# Invoke: /accuracy

Show tool accuracy statistics and unlock status.

## What It Does
1. Reads memory/state-tool-accuracy.md
2. Reads logs/accuracy.log
3. Computes rolling accuracy per tool per agent (last 100 uses)
4. Shows which tools are at unlock thresholds
5. Shows recently unlocked tools

## Usage
```
/accuracy                    — show all tool accuracies
/accuracy <tool>             — show specific tool history
/accuracy thresholds         — show unlock thresholds and progress
/accuracy unlock             — manually trigger unlock check
```

## Output Format
| Tool | Agent | Success | Total | Accuracy | Tier | Next Threshold |
|------|-------|---------|-------|----------|------|----------------|
| Edit | dev-team | 94 | 100 | 94.0% | 2 | 95% → Tier 3 |
| Bash | qa | 87 | 100 | 87.0% | 1 | 85% → Tier 2 ✓ |
