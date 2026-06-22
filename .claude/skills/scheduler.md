---
name: scheduler
description: "Smart scheduler — runs tasks at optimal times. Considers rate limits, costs, system load."
metadata:
  type: skill
  category: orchestration
  version: 1
---

# Smart Scheduler

Schedules tasks at the best time.

## What It Considers

- API rate limits
- Cost windows (off-peak cheaper)
- System load (don't run heavy tasks at peak)
- User presence (no background work during work hours)
- Task dependencies
- Deadline urgency

## Commands

- `scheduler add <task> <time>` — schedule
- `scheduler list` — show queue
- `scheduler optimize` — auto-optimize
- `scheduler run <id>` — force run now

## Time Windows

- Off-peak: 2am-7am (cheapest API)
- Peak: 9am-5pm (avoid heavy work)
- Quiet: 7pm-2am (medium)
