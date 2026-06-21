---
name: perf-monitor
description: "Real-time performance monitoring with flame graphs, memory profiling, CPU sampling"
metadata:
  type: skill
  category: performance
  version: 1
---

# Performance Monitor

Real-time performance monitoring.

## What It Captures

- CPU usage per function (py-spy, perf)
- Memory allocation (memray, heaptrack)
- I/O patterns
- Network latency
- Database query timing

## Output

- Live flame graph
- Memory timeline
- Hotspot report
- N+1 query detection

## Commands

- `perf-monitor start` — begin monitoring
- `perf-monitor stop` — stop + generate report
- `perf-monitor report` — view latest
- `perf-monitor compare <before> <after>` — diff

## Integration

Works with `perf-tuning` preset and `code-review` skill.
