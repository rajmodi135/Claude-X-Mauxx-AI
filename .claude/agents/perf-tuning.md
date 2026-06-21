---
name: perf-tuning
description: "Preset for performance tuning (profiling + benchmarking + optimization + monitoring)"
metadata:
  type: agent-preset
  version: 1
  stack:
    profilers: ["py-spy", "cProfile", "perf", "flamegraph"]
    benchmarkers: ["k6", "locust", "wrk", "hyperfine"]
  modelTier: "sonnet"
---

# Performance Tuning Preset

**Auto-configures the AI company for performance optimization projects.**

## Detected Stack

Triggers when project mentions:
- "performance", "slow", "optimize", "scale", "load test"
- Already has monitoring (Prometheus, Datadog, Sentry)
- High-traffic production system

## Auto-Configured Agents

| Agent | Role | Tools |
|-------|------|-------|
| **Perf Architect** | Profiling strategy, bottleneck ID | Opus |
| **CPU Profiler** | py-spy, perf, flamegraph | Sonnet |
| **Memory Profiler** | memray, heaptrack | Sonnet |
| **DB Tuner** | Query plans, indexes, N+1 | Sonnet |
| **Network Analyzer** | curl, tcpdump, mitmproxy | Sonnet |
| **Load Tester** | k6, locust, wrk | Sonnet |
| **Cache Specialist** | Redis, Memcached, CDN | Sonnet |
| **Frontend Perf** | Lighthouse, WebPageTest | Sonnet + frontend-design |

## Default Workflow

```
Perf Issue → Perf Architect (strategy) → parallel:
  - CPU Profiler (where's time spent)
  - Memory Profiler (leaks, bloat)
  - DB Tuner (slow queries)
  - Network Analyzer (latency)
→ Load Tester (before/after)
→ Cache Specialist (if applicable)
→ Frontend Perf (if UI)
→ Report (% improvement)
```

## Profiling Strategy

```python
# 1. CPU profile
py-spy record -o profile.svg -- python main.py

# 2. Memory profile
memray run -o memory.bin python main.py
memray flamegraph memory.bin

# 3. DB queries
EXPLAIN ANALYZE SELECT * FROM users WHERE email = ?

# 4. Network
curl -w "@curl-format.txt" -o /dev/null -s https://api.example.com
```

## Common Wins (cheapest first)

| Win | Effort | Impact |
|-----|--------|--------|
| Add DB index | 5 min | 10-100x faster queries |
| Enable gzip/brotli | 1 min | 70% smaller responses |
| Cache in Redis | 30 min | 100x faster reads |
| Use CDN | 1 hr | 5x faster for global users |
| Connection pool | 1 hr | 3x throughput |
| Async I/O | 1 day | 5-10x throughput |
| Replace ORM with raw SQL | 1 day | 2-5x faster queries |
| Switch to Rust/Go | 1 week | 10-50x faster |

## Pre-loaded Skills

- `code-review` (review optimizations)
- `verify` (run + measure)
- `simplify` (cleanup after optimization)

## Quick Start

```bash
echo "preset: perf-tuning" >> CLAUDE.md
claude --config .claude/settings.json --task "Profile the slow /api/search endpoint"
```

## Example Output

```markdown
# Perf Report: /api/search

## Before
- p50: 800ms
- p95: 2.4s
- p99: 5.1s
- CPU: 95%
- DB queries: 47 per request

## After Optimization
- p50: 45ms (18x faster)
- p95: 120ms (20x faster)
- p99: 280ms (18x faster)
- CPU: 35%
- DB queries: 1 per request (47x reduction)

## Changes Made
1. Added index on `users.email` (eliminated full table scan)
2. Replaced ORM with prepared statements (eliminated N+1)
3. Added Redis cache for top 1000 searches (5min TTL)
4. Switched to async/await throughout
5. Added connection pooling (10 → 50 connections)
```
