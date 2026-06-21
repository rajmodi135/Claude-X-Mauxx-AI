# Claude x Mauxx AI — Memory System

This directory is created on first run with the system. It stores the persistent memory of your AI company.

## Files Created on First Run

| File | Purpose |
|------|---------|
| `MEMORY.md` | Main index — always read first |
| `rule-*.md` | Behavioral rules (auto-loaded every session) |
| `fact-*.md` | Architecture decisions, project facts, bug records |
| `plan-*.md` | Active multi-step plans |
| `archive-<date>-*.md` | Completed plans with outcomes |
| `state-*.md` | Runtime state (queue, budget, heartbeat, snapshot) |
| `session-*.md` | Session snapshots for crash recovery |

## How It Works

The system reads `MEMORY.md` (the index, ~2 KB) on every session start. It then loads relevant files based on the active plan and [[wiki-links]].

This keeps conversation context small while the project state lives on disk.

## Template Files

This `README.md` is a template. On first run, the system creates the actual `MEMORY.md` index and other state files.

## Personal Command Memory

The file `fact-command-personal-memory.md` is **never lost**. It records every project worked on, every preference, every learning. The system reads it on every session start to remember context from prior runs.

## Backup Recommendation

```bash
# Backup the memory directory
tar -czf claude-x-mauxx-ai-memory-$(date +%Y%m%d).tar.gz memory/
```
