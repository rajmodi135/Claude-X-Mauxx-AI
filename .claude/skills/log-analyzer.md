---
name: log-analyzer
description: "Analyzes logs for errors, patterns, anomalies. Aggregates, summarizes, alerts."
metadata:
  type: skill
  category: observability
  version: 1
---

# Log Analyzer

Smart log analysis.

## What It Does

1. **Aggregates** logs from multiple sources (file, journald, CloudWatch, Datadog)
2. **Detects** error patterns using AI
3. **Groups** similar errors
4. **Suggests** fixes based on past resolutions
5. **Alerts** on anomalies (error spike, latency spike)

## Commands

- `log-analyzer tail` — recent logs
- `log-analyzer errors` — just errors
- `log-analyzer group <pattern>` — group similar
- `log-analyzer alert <threshold>` — set alert
- `log-analyzer export <format>` — CSV/JSON

## Output

```
ERRORS (last 1h): 47

Grouped:
  - DBConnectionError (32)
    src/db.py:42 — connection refused
    First seen: 14:32
    Suggested fix: check DB_HOST env var
  - AuthTimeout (15)
    src/auth/middleware.py:18

Top error sites:
  1. src/api/users.py:42 (24)
  2. src/auth/middleware.py:18 (15)
  3. src/api/login.py:8 (8)
```