# Claude x Mauxx AI — System Heartbeat
# Invoke: /heartbeat

Show system health and runtime state.

## What It Does
1. Reads memory/state-session-snapshot.md
2. Reads memory/state-resource-budget.md
3. Reads memory/state-heartbeat.md (if exists)
4. Shows: active plan, current step, resource usage, last heartbeat

## Usage
```
/heartbeat                   — show system health
/heartbeat --full            — show all state files
/heartbeat --resources       — show only resource usage
/heartbeat --active-plan     — show only active plan
```

## Output Format
```
═══════════════════════════════════════════════
  Claude x Mauxx AI — System Heartbeat
═══════════════════════════════════════════════

  Active Plan:   plan-agent-skills
  Current Step:  Step 3 of 5 (API Endpoints)
  Worker PID:    14920
  Last Update:   2026-06-22T14:30:00Z

  Resources:
    Context:     312 KB / 1 MB    (31%) ✓
    CPU:         22%             ✓
    RAM:         4.2 GB / 16 GB   (26%) ✓
    Disk I/O:    12 MB/s          ✓
    Active Agents: 3 / 8         ✓

  Cron Jobs:
    Heartbeat:       every 30 min ✓ active
    Accuracy Audit:  every 4h    ✓ active
    Daily Review:    9am daily   ✓ active

  Status: HEALTHY
═══════════════════════════════════════════════
```
