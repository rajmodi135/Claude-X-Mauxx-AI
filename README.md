<p align="center">
  <h1 align="center">🚀 Claude × Mauxx AI</h1>
  <p align="center"><em>Turn Claude Code into a 24/7 autonomous AI company for your project.</em></p>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-how-it-works">How It Works</a> •
  <a href="#-the-ai-company">The AI Company</a> •
  <a href="#-tool-accuracy-system">Tool Accuracy</a> •
  <a href="#-resource-governor">Resource Governor</a> •
  <a href="#-memory--plan-system">Memory & Plans</a> •
  <a href="#-feedback--support">Feedback</a> •
  <a href="#-configuration">Configuration</a>
</p>

---

## 🤔 What Is This?

**Claude × Mauxx AI** is an *operating system for Claude Code* that transforms it from a single AI assistant into a **self-driving AI company** with specialized roles:

> **CEO** → **CTO** → **Dev Team** → **QA** → **Memory Keeper** → **Innovation Lead** → **Support Team**

Each role is a specialized Claude agent. They work together 24/7 — planning, coding, testing, tracking their own accuracy, unlocking better tools as they improve, and recovering from failures — all **without permission prompts**.

A single command starts it in any project:

```bash
claude --config .claude/settings.json   # or: npx claude-x-mauxx-ai
```

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **🧠 Persistent Memory** | File-based markdown memory. Survives restarts. Never re-learns your project. |
| **📋 Plan System** | Auto-creates plans from tasks. Tracks steps. Archives completed work with lessons. |
| **🏢 AI Company** | CEO orchestrates 6 specialized agents. They communicate via files, not chat. |
| **📊 Tool Accuracy** | Every tool use logged. At 85% → Tier 2 tools. 90% → Tier 3. 95% → Tier 4. 98% → Tier 5. |
| **🛡️ Resource Governor** | Monitors context, RAM, CPU, tokens. Auto-summarizes at 70%, hard-stops at 85%. |
| **🔁 24/7 Loop** | Keeps working autonomously. Resumes from last step on restart. |
| **🧪 Self-Healing** | Retries 3x with exponential backoff. Creates bug facts. Escalates automatically. |
| **🎫 Feedback System** | Tickets, complaints, reviews, quick reactions — CLI now, UI coming. |
| **🔐 Zero Prompts** | No "are you sure?" No permission popups. Just work. |

---

## ⚡ Quick Start

### Install globally (one command)

```bash
npm install -g claude-x-mauxx-ai
```

### Or run instantly

```bash
npx claude-x-mauxx-ai
```

### Or manual setup

```bash
git clone https://github.com/rajmodi135/Claude-X-Mauxx-AI.git
cd your-project
claude --config /path/to/Claude-X-Mauxx-AI/.claude/settings.json
```

### Windows one-click

```powershell
powershell -ExecutionPolicy Bypass -File install.ps1
```

### Mac/Linux one-click

```bash
curl -fsSL https://raw.githubusercontent.com/rajmodi135/Claude-X-Mauxx-AI/main/install.sh | bash
```

---

## 🎯 What Happens On First Run

When you run `claude --config .claude/settings.json` for the **first time** in a project:

1. 🔎 **Scans** all `.md` files in your project
2. 🧪 **Detects** your tech stack (package.json, pyproject.toml, Cargo.toml, etc.)
3. 🧠 **Saves** `fact-command-personal-memory.md` — remembers this project forever
4. 📋 **Creates** `plan-project-onboarding.md` — a plan to understand your codebase
5. 🚀 **Begins** autonomous work — no prompts needed

Every subsequent run just continues from where you left off.

---

## 🏢 How It Works: The AI Company

### The Org Chart

```
                       ┌──────────────────────┐
                       │  👤 YOU (Stakeholder) │
                       │  commands · reviews   │
                       └─────────┬────────────┘
                                 │
                                 ▼
                 ┌────────────────────────────┐
                 │  🎯 CEO / Orchestrator     │
                 │  • selects plans           │
                 │  • delegates to agents     │
                 │  • reports progress        │
                 └──────────┬─────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ 🏗️ CTO/Archi-│   │ 💻 Dev Team  │   │ ✅ QA/Verifier│
│   tect       │   │  • writes    │   │  • runs tests │
│  • designs   │   │    code      │   │  • catches    │
│  • picks     │   │  • commits   │   │    bugs       │
│    tools     │   │  • self-tests│   │  • benchmarks │
└──────────────┘   └──────────────┘   └──────────────┘
        │                   │                   │
        └───────────────────┼───────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ 💾 Memory   │   │ 🔬 Innovation│   │ 🎫 Support   │
│   Keeper    │   │   Lead       │   │   Team       │
│  • updates  │   │  • tracks    │   │  • triages   │
│    plans    │   │    accuracy  │   │    tickets   │
│  • snapshots│   │  • unlocks   │   │  • replies   │
│    state    │   │    tools     │   │  • escalates │
└──────────────┘   └──────────────┘   └──────────────┘
```

### How They Communicate

**Via files only.** Zero in-memory chatter = zero context bloat.

- **Plans** → `memory/plan-*.md` (CEO writes, others read)
- **Decisions** → `memory/fact-*.md` (anyone writes, CEO reads)
- **State** → `memory/state-*.md` (Memory Keeper writes, all read)
- **Tickets** → `feedback/tickets/*.json` (Support reads/writes)

### Workflow Pipeline

```
User Request → CEO triages → creates plan-*.md
    → CTO designs approach (fact-*.md)
    → Dev Team executes steps, commits
    → QA runs tests, verifies
    → Memory Keeper updates plan + MEMORY.md
    → Innovation Lead logs accuracy
    → Support triages any new tickets
    → CEO picks next plan or waits
```

---

## 📊 Tool Accuracy System

### The Tier Ladder

| Tier | Threshold | Tools Unlocked |
|------|-----------|----------------|
| 🟢 **Tier 1: Basics** | Always on | Read, Write, Edit, Glob, Grep, Bash basics |
| 🔵 **Tier 2: Intermediate** | 85%+ accuracy | MultiEdit, code-review, deep-research, safe Bash |
| 🟣 **Tier 3: Advanced** | 90%+ accuracy | WebFetch, WebSearch, advanced Bash, Workflow |
| 🟠 **Tier 4: Expert** | 95%+ accuracy | Multi-agent orchestration, security audit, profiling |
| 🔴 **Tier 5: Frontier** | 98%+ accuracy | Self-modifying tools, custom tool creation |

### How It Works

Every tool use is logged to `logs/accuracy.log`:

```
2026-06-22T14:30:00 tool=Edit result=success agent=dev context="main.py:L42" duration_ms=234
```

An aggregated `state-tool-accuracy.md` tracks rolling accuracy (last 100 uses). When a tool sustains ≥ threshold for 30+ uses:

1. ✅ Innovation Lead **verifies** sustained performance
2. 🎉 **Unlocks** the next-tier tool
3. 📝 **Creates** `fact-tool-unlocked-<tool>.md`
4. 📣 **Notifies** CEO: "🎉 MultiEdit unlocked for dev-team"

---

## 🛡️ Resource Governor

### Never overloads your machine

| Resource | Limit | Action |
|----------|-------|--------|
| **Context window** | < 70% → summarize · < 85% → hard stop | Auto-saves state, resumes on restart |
| **RAM** | < 80% | Reduces concurrent agents by half |
| **CPU** | < 90% (5 min sustained) | Sleeps 60s, resumes slower |
| **Token rate** | < 50K/min | Smaller model for non-critical tasks |
| **Concurrent agents** | Max 8 | Queues excess, runs as slots free |
| **Disk** | < 90% | Archives old plans, compresses logs |

Every action checks `memory/state-resource-budget.md` first. If limits are hit, it throttles — never crashes.

---

## 🧠 Memory & Plan System

### File-based, persistent, portable

```
Claude-X-Mauxx-AI/memory/
├── MEMORY.md                        ← Main index (always read first, ~2 KB)
├── rule-*.md                        ← Behavioral rules (always loaded, ~5 KB)
├── fact-*.md                        ← Decisions, bugs, project facts
├── plan-*.md                        ← Active plans (max 5)
├── archive-<date>-*.md              ← Completed plans (unlimited)
├── state-*.md                       ← Runtime state (queue, budget, heartbeats)
└── session-*.md                     ← Session snapshots
```

### Plan Lifecycle

```
DRAFT → ACTIVE → COMPLETED → ARCHIVED
               ↳ BLOCKED → ACTIVE (when unblocked)
               ↳ FAILED → ARCHIVED
```

### Wiki-Link Navigation

Plans reference each other with `[[plan-name]]` — no need to load all files:

```markdown
This depends on [[plan-auth-hardening]] being complete first.
See [[fact-decision-architecture]] for constraints.
```

---

## 🎫 Feedback & Support

### Ticket System (CLI)

| Command | Description |
|---------|-------------|
| `/support` | Open a support ticket |
| `/feedback` | Send quick 👍/👎 feedback |
| `/review` | Review completed work (1-5 stars) |
| `/plan` | Show active plans |
| `/accuracy` | Show tool accuracy stats |
| `/heartbeat` | Show system health |
| `/archive` | Show past plans |

### Coming Soon: UI Buttons

Floating support button (bottom-right) with:
- 🎫 **Ticket** — Bug, complaint, feature request, question
- ⭐ **Review** — Rate accuracy, speed, communication
- 💬 **Feedback** — Quick 👍/👎 + comment

---

## 📁 File Structure

```
Claude-X-Mauxx-AI/
├── README.md                         ← This file
├── INSTALL.md                        ← Installation guide
├── LICENSE                           ← MIT
├── CLAUDE_X_MAUXX_AI_MASTER_PLAN.md  ← Full architecture blueprint
├── CLAUDE.md                         ← AI brain (loaded by Claude)
├── package.json                      ← npm package
├── .gitignore
├── install.ps1                       ← Windows one-click installer
├── install.sh                        ← Mac/Linux one-click installer
├── bin/
│   ├── claude-x-mauxx-ai.mjs         ← npm entry point
│   └── postinstall.js                ← Post-install welcome
├── .claude/
│   ├── settings.json                 ← Autopilot config
│   ├── plugin.json                   ← Claude Code plugin manifest
│   ├── commands/                     ← Slash commands
│   │   ├── mauxx.md                  ← /mauxx (full run)
│   │   ├── plan.md                   ← /plan (show plans)
│   │   ├── memory.md                 ← /memory (show index)
│   │   ├── support.md                ← /support (tickets)
│   │   ├── feedback.md               ← /feedback
│   │   ├── accuracy.md               ← /accuracy (stats)
│   │   ├── heartbeat.md              ← /heartbeat (health)
│   │   └── archive.md                ← /archive (past plans)
│   └── skills/                       ← Auto-loaded skill extensions
├── memory/                           ← Created on first run
│   ├── MEMORY.md                     ← Main index
│   ├── rule-*.md                     ← Rules
│   ├── fact-*.md                     ← Facts
│   ├── state-*.md                    ← Runtime state
│   ├── plan-*.md                     ← Active plans
│   ├── archive-*.md                  ← Archived plans
│   └── session-*.md                  ← Session snapshots
├── logs/                             ← Created on first run
│   ├── accuracy.log                  ← Tool tracking
│   ├── heartbeat.log                 ← Health logs
│   └── session.log                   ← Activity log
├── tools/                            ← Tool registry (auto-extends)
├── feedback/                         ← Feedback data
└── .claude/settings.json             ← Config
```

---

## 🔧 Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `CLAUDE_AUTONOMOUS_MODE` | `true` | Enables autonomous operation |
| `CLAUDE_EFFORT_LEVEL` | `ultracode` | Claude effort (ultracode = xhigh + workflow) |
| `CLAUDE_SKILLS_ALL` | `true` | Loads all skills |
| `CLAUDE_TOOLS_ALL` | `true` | Enables all tools |
| `CLAUDE_LOOP_MODE` | `24x7` | Loop mode |
| `CLAUDE_CONFIG_DIR` | auto | Config directory |
| `CLAUDE_MEMORY_DIR` | auto | Memory directory |

### Resource Limits (in settings.json)

```json
"resourceLimits": {
  "maxContextKB": 500,
  "maxAgents": 8,
  "maxTokensPerTurn": 32000,
  "maxCpuPercent": 90,
  "maxRamPercent": 80
}
```

---

## 🗺️ Roadmap

**Phase 1: Foundation** ✅ Done
- [x] Memory & Plan system
- [x] CLAUDE.md operating instructions
- [x] Auto-mode permissions
- [x] Tool accuracy tracking design

**Phase 2: Core** 🔜 In Progress
- [ ] Tool accuracy tracker (skill + log parser)
- [ ] Resource Governor (state-resource-budget.md)
- [ ] Context Guard (auto-summarize at 70%)
- [ ] Self-healing retry (3x with backoff)
- [ ] Heartbeat cron job (durable, every 30 min)

**Phase 3: Advanced**
- [ ] Innovation Lead agent (track >90% threshold)
- [ ] Support Team agent (triage tickets)
- [ ] Frontend support panel (ticket/review/feedback buttons)
- [ ] Tier-3 tool auto-unlock

**Phase 4: Self-Improvement**
- [ ] Weekly accuracy reports
- [ ] Auto-tool-creation at >95%
- [ ] Cross-project learning

---

## 🤝 Contributing

1. Fork this repo
2. Create a feature branch
3. Test your changes
4. Submit a PR with before/after accuracy data

---

## 📄 License

MIT — do whatever you want.

---

<p align="center">Built by <a href="https://github.com/rajmodi135">@rajmodi135</a> · Powered by Mauxx AI</p>
<p align="center">⭐ Star us on GitHub · 🐛 Report issues · 💡 Suggest features</p>
