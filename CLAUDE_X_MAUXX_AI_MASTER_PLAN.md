# Claude x Mauxx AI — Master Plan & Architecture Blueprint

> Version: 1.0 | Created: 2026-06-22 | Status: ACTIVE

---

## Overview

Claude x Mauxx AI transforms Claude Code into a 24/7 autonomous AI organization. It runs with:

- **Auto mode** — no permission prompts
- **Effort: ultracode** — xhigh + dynamic workflow orchestration
- **All skills & tools** — every available capability enabled
- **Company structure** — CEO + 6 specialized agent roles
- **Memory & Plan system** — file-based, persistent, crash-recoverable
- **Tool accuracy tracking** — auto-unlocks new tools at 85%/90%/95%/98%
- **Resource governor** — context, RAM, CPU, tokens all monitored and throttled
- **Self-healing** — 3x retry with backoff, then escalation via tickets

---

## Company Structure

| Role | Responsibility |
|------|----------------|
| CEO / Orchestrator | Reads memory, picks plans, delegates, reports |
| CTO / Architect | Tech design, tool selection, risk analysis |
| Dev Team | Code, commit, PRs |
| QA / Verifier | Tests, verification, benchmarks |
| Memory Keeper | Plan updates, MEMORY.md index, snapshots |
| Innovation Lead | Tool accuracy tracking, auto-unlock |
| Support Team | Ticket triage, replies, escalation |

---

## Tool Accuracy Tiers

| Tier | Unlock | Tools Added |
|------|--------|-------------|
| 1 (Basics) | Always | Read, Write, Edit, Glob, Grep, Bash |
| 2 (85%) | 85%+ | MultiEdit, code-review, deep-research |
| 3 (90%) | 90%+ | WebFetch, WebSearch, Workflow, advanced Bash |
| 4 (95%) | 95%+ | Multi-agent orchestration, security audit |
| 5 (98%) | 98%+ | Self-modifying, custom tool creation |

---

## Plan Lifecycle

```
DRAFT → ACTIVE → COMPLETED → ARCHIVED
               ↳ BLOCKED → ACTIVE (when unblocked)
               ↳ FAILED → ARCHIVED
```

---

## Resource Limits

| Resource | Warning | Hard Stop |
|----------|---------|-----------|
| Context | 70% → summarize | 85% → save & exit |
| RAM | 80% → reduce agents | 90% → emergency stop |
| CPU (5min) | 90% → sleep 60s | 95% → stop non-critical |
| Token rate | 50K/min → smaller model | 80K/min → pause |

---

## First Run Behavior

1. Scan all `.md` files in project root
2. Detect tech stack
3. Save to `fact-command-personal-memory.md`
4. Create `plan-project-onboarding.md`
5. Begin autonomous work
