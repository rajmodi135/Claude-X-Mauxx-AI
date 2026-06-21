---
name: task-queue
description: "Persistent task queue. Add, list, prioritize, and track tasks across sessions."
metadata:
  type: skill
  category: orchestration
  version: 1
---

# Task Queue Skill

Persistent task management.

## Storage

`memory/state-task-queue.md` — markdown file with task list.

## Task Format

```yaml
- id: T001
  title: Implement rate limiting
  status: pending | in_progress | done | blocked
  priority: P0 | P1 | P2 | P3
  createdAt: 2026-06-22
  assignee: dev-team
  depends_on: [T000]
  estimated_hours: 4
  tags: [backend, security]
```

## Commands

- `/task add <title>` — add a task
- `/task list` — show all
- `/task <id>` — show details
- `/task done <id>` — mark done
- `/task <id> start` — start work
- `/task <id> block` — mark blocked
