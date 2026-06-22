---
name: error-tracking
description: "Sentry-style error tracking and aggregation. Group, prioritize, suggest fixes."
metadata:
  type: skill
  category: monitoring
  version: 1
---

# Error Tracking

Aggregates errors, groups similar ones, prioritizes, suggests fixes.

## What It Does

1. Captures errors (Sentry SDK, custom, stdout parsing)
2. Groups by stack trace fingerprint
3. Prioritizes (frequency × user impact)
4. Suggests fixes from past resolutions
5. Auto-creates PRs for known fixes

## Output

```
ERRORS (last 1h): 47

Top 5:
  1. DBConnectionError (32x) — src/db.py:42
  2. AuthTimeout (15x) — src/auth/middleware.py:18
  3. RateLimitHit (8x) — src/api/login.py:8
```

## Integration

- Sentry SDK (preferred)
- stdout/stderr parsing (fallback)
- Files in `logs/`
- Past resolutions in `fact-bug-*.md`
