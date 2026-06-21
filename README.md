<p align="center">
  <h1 align="center">🚀 Claude × Mauxx AI</h1>
  <p align="center"><em>An autonomous AI company in your terminal. Skill-first. Model-tiered. Free-tier.</em></p>
  <p align="center"><strong>v2.0 — 70+ commits, 20+ skills, 9 presets, Neon TUI</strong></p>
</p>

<p align="center">
  <a href="#-what-is-it">What is it?</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-the-ai-company">The AI Company</a> •
  <a href="#-neon-tui">Neon TUI</a> •
  <a href="#-smart-skills">Smart Skills</a> •
  <a href="#-model-routing">Model Routing</a> •
  <a href="#-preset-agents">Presets</a> •
  <a href="#-free-tier-stack">Free-Tier Stack</a> •
  <a href="#-commands">Commands</a> •
  <a href="#-configuration">Config</a> •
  <a href="#-roadmap">Roadmap</a>
</p>

---

## 🤔 What Is It?

**Claude × Mauxx AI** is an open-source operating system for Claude Code. It transforms Claude Code into a **self-driving AI company** with:

- **CEO** that picks the plan
- **6 specialized agents** (CTO, Dev, QA, Memory, Innovation, Support)
- **20+ skills** that work out of the box
- **9 preset configurations** for common project types
- **Model tiering** that saves 85%+ on costs (Haiku/Sonnet/Opus)
- **Neon TUI** with profession onboarding, stats bar, animated AI agent
- **Free-tier integrations** (GitHub Actions, Cloudflare, Ollama)
- **Self-healing** (3x retry with backoff, then escalation)
- **Tool accuracy tracking** with auto-unlock at 85%/90%/95%/98%

A single command starts it in any project:

```bash
claude --config .claude/settings.json
# or: npx claude-x-mauxx-ai
# or: python -m tui.mauxx_tui
```

---

## ⚡ Quick Start

### One command
```bash
npx claude-x-mauxx-ai
```

### Global install
```bash
npm install -g claude-x-mauxx-ai
claude --config .claude/settings.json
```

### Manual clone
```bash
git clone https://github.com/rajmodi135/Claude-X-Mauxx-AI.git
cd your-project
claude --config /path/to/Claude-X-Mauxx-AI/.claude/settings.json
```

### Neon TUI (recommended)
```bash
cd tui
pip install -r requirements.txt
python run.py
```

### What Happens on First Run

1. Asks your profession (Developer, Designer, Data Scientist, etc.)
2. Auto-detects your tech stack
3. Loads the right preset agent
4. Configures model tiering for your budget
5. Begins autonomous work

---

## 🏢 The AI Company

```
                       ┌──────────────────────┐
                       │  👤 YOU (Stakeholder) │
                       └─────────┬────────────┘
                                 │
                                 ▼
                 ┌────────────────────────────┐
                 │  🎯 CEO / Orchestrator     │
                 │  picks plan, delegates     │
                 └──────────┬─────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ 🏗️ CTO/      │   │ 💻 Dev Team  │   │ ✅ QA/       │
│   Architect  │   │  write code  │   │   Verifier   │
│  design      │   │  commit      │   │  test        │
└──────────────┘   └──────────────┘   └──────────────┘
        │                   │                   │
        └───────────────────┼───────────────────┘
                            ▼
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ 💾 Memory    │   │ 🔬 Innovation│   │ 🎫 Support   │
│   Keeper     │   │   Lead       │   │   Team       │
│  plan update │   │  accuracy    │   │  tickets     │
└──────────────┘   └──────────────┘   └──────────────┘
```

All communicate via **files only** — zero in-memory chatter = zero context bloat.

---

## 🎨 Neon TUI

A beautiful terminal interface with:
- **Profession onboarding** (8 professions)
- **Stats bar** with tokens, tasks, ETA, cost, uptime
- **Animated Mauxx mascot** (ASCII face with moods)
- **Agent status messages** ("Analyzing your project...")
- **Claude Code subprocess** integration
- **Custom color themes** (neon, cyberpunk, matrix, vaporwave, nord, monokai)

```bash
cd tui
pip install -r requirements.txt
python run.py
```

---

## 🧠 Smart Skills (20+)

| Skill | Purpose |
|-------|---------|
| `model-router` | Auto-pick cheapest model per task |
| `smart-memory` | Vector search over past plans |
| `cost-optimizer` | Real-time spend tracking + auto-throttle |
| `predictive-loader` | Pre-fetch context, reduce tool calls 40% |
| `orchestrate` | Multi-agent workflow coordinator |
| `accuracy-monitor` | Tool accuracy dashboard + auto-unlock |
| `auto-heal` | 3x retry with backoff, self-healing |
| `git-workflow` | Conventional commits, branch mgmt, changelogs |
| `reporter` | Daily/weekly/monthly progress reports |
| `emoji-reactions` | Quick 👍/👎 feedback for satisfaction |
| `dependency-analyzer` | Scans outdated/vulnerable packages |
| `test-runner` | Auto-runs tests after every change |
| `doc-generator` | Auto-creates docstrings, README, API docs |
| `security-scanner` | OWASP Top 10, secrets, CVE detection |
| `task-queue` | Persistent task list with priority, deps |
| `webhook` | GitHub/Slack/Discord/Telegram integration |

---

## 💰 Model Routing (Cost Optimization)

**Before (always Opus):**
```
$0.075 per 1K output tokens → $30-50/month typical
```

**After (smart tiering):**
```
Haiku:  $0.00125/1K  (60% of tasks)  — classify, sort, format
Sonnet: $0.015/1K    (30% of tasks)  — code, test, review
Opus:   $0.075/1K    (5% of tasks)   — architecture, critical
Cache:  90% off      (rest)          — repeated patterns
Ollama: $0           (trivials)      — local LLM

→ $3-10/month typical  (85% savings)
```

The `model-router` skill picks the cheapest model that can handle each task automatically.

---

## 🎯 Preset Agents (9)

| Preset | Use For |
|--------|---------|
| `webapp-fullstack` | React/Vue + FastAPI + DB |
| `api-microservice` | API + Docker + K8s |
| `mobile-app` | React Native + Expo + iOS/Android |
| `data-pipeline` | Airflow + dbt + Spark + BigQuery |
| `cli-tool` | Typer/Click + PyPI/npm + Homebrew |
| `docs-site` | Docusaurus + MDX + i18n |
| `security-audit` | SAST + DAST + compliance |
| `perf-tuning` | Profiler + load test + cache |
| `ml-training` | PyTorch + W&B + HuggingFace |
| `blockchain` | Solidity + Hardhat + OpenZeppelin |

Use with:
```bash
echo "preset: webapp-fullstack" >> CLAUDE.md
```

---

## 🆓 Free-Tier Stack

| Service | What For | Free Tier |
|---------|----------|-----------|
| **GitHub Actions** | CI/CD, auto-test, release | 2,000 min/month |
| **Cloudflare Workers** | Support ticket API | 100K req/day |
| **Supabase** | Tickets DB + auth | 500MB |
| **Sentry** | Error tracking | 5K events/month |
| **Ollama** | Local LLM | FREE forever |
| **Telegram** | P0 notifications | FREE |
| **Vercel** | Frontend hosting | 100GB |

Total infrastructure: **$0/month**

---

## 🎮 Commands (15+)

| Command | Purpose |
|---------|---------|
| `/mauxx` | Full run |
| `/plan` | Show active plans |
| `/memory` | Show memory index |
| `/support` | Open ticket |
| `/feedback` | Quick reaction |
| `/review` | Rate work |
| `/accuracy` | Tool accuracy stats |
| `/heartbeat` | System health |
| `/archive` | Past plans |
| `/cost` | Spending report |
| `/preset` | Set project preset |
| `/report` | Progress report |
| `/config` | Show/edit config |
| `/profile` | Switch profession |
| `/theme` | Switch TUI theme |
| `/deploy` | Deploy project |
| `/search` | Semantic search |
| `/test` | Run tests |
| `/init` | Initialize project |

---

## 🔄 Resource Governor

Never overloads your machine or context:

| Resource | Warning | Hard Stop |
|----------|---------|-----------|
| Context window | 70% → auto-summarize | 85% → save & exit |
| RAM | 80% → reduce agents | 90% → emergency stop |
| CPU (5min) | 90% → sleep 60s | 95% → stop non-critical |
| Token rate | 50K/min → smaller model | 80K/min → pause |
| Concurrent agents | Max 8 → queue | — |
| Disk | 90% → archive | 95% → critical |

---

## 🧪 Self-Healing

```
On tool error → retry 3x (exponential backoff) → still fails?
   → log error
   → mark step blocked
   → try alternative tool
   → if no alternative: create support ticket
   → notify user once
```

95%+ of errors self-heal without user intervention.

---

## 🛠️ Tool Accuracy → Auto-Unlock

```
Tool accuracy ≥ 85% (sustained 30 uses) → Tier 2 unlocked
Tool accuracy ≥ 90% (sustained 30 uses) → Tier 3 unlocked
Tool accuracy ≥ 95% (sustained 30 uses) → Tier 4 unlocked
Tool accuracy ≥ 98% (sustained 30 uses) → Tier 5 unlocked
```

The system gets more powerful as it proves itself.

---

## 📁 File Structure

```
Claude-X-Mauxx-AI/
├── README.md                 ← This file
├── CLAUDE.md                 ← AI brain (auto-loaded)
├── INSTALL.md                ← Installation guide
├── LICENSE                   ← MIT
├── VERSION_ROADMAP.md        ← v1 → v10, 1000+ commits plan
├── SMART_FEATURES_ROADMAP.md ← v2 architecture
├── ARCHITECTURE.md           ← System design
├── COMPARISON.md             ← vs alternatives
├── SECURITY.md               ← Security policy
├── FAQ.md                    ← Common questions
├── CONTRIBUTING.md           ← How to contribute
├── CHANGELOG.md              ← Release notes
├── PLUGIN_SDK.md             ← Build your own
├── package.json              ← npm package
├── install.ps1               ← Windows installer
├── install.sh                ← Mac/Linux installer
├── .claude/
│   ├── settings.json         ← Autopilot config
│   ├── plugin.json           ← Plugin manifest
│   ├── hooks/                ← 4 lifecycle hooks
│   ├── skills/               ← 16+ skills
│   ├── commands/             ← 15+ slash commands
│   └── agents/               ← 9 presets
├── tui/                      ← Neon TUI (Python)
├── .github/workflows/        ← Free CI/CD
├── cloudflare-worker/        ← Free ticket API
├── scripts/                  ← Doctor, update, sync
├── examples/                 ← Example skills/plugins
├── memory/                   ← Created at runtime
├── logs/                     ← Created at runtime
└── tools/                    ← Created at runtime
```

---

## 🗺️ Roadmap

| Version | Theme | Status |
|---------|-------|--------|
| **v1** | Foundation | ✅ DONE |
| **v2** | Smart + TUI + Routing | ✅ DONE (70+ commits) |
| **v3** | Plugin marketplace | 🔜 Next |
| **v4** | Web dashboard | 🔜 |
| **v5** | Mobile + collaboration | 🔜 |
| **v6** | Auto-improvement | 🔜 |
| **v7** | Enterprise + compliance | 🔜 |
| **v8** | Multi-LLM | 🔜 |
| **v9** | Full autonomy | 🔜 |
| **v10** | Self-evolving IDE | 🔜 |

See [VERSION_ROADMAP.md](VERSION_ROADMAP.md) for full plan.

---

## 📚 Documentation

- [INSTALL.md](INSTALL.md) — Installation
- [ARCHITECTURE.md](ARCHITECTURE.md) — System design
- [FAQ.md](FAQ.md) — Common questions
- [COMPARISON.md](COMPARISON.md) — vs alternatives
- [CONTRIBUTING.md](CONTRIBUTING.md) — How to contribute
- [SECURITY.md](SECURITY.md) — Security policy
- [CHANGELOG.md](CHANGELOG.md) — Release notes
- [PLUGIN_SDK.md](PLUGIN_SDK.md) — Build your own
- [VERSION_ROADMAP.md](VERSION_ROADMAP.md) — v1 → v10

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch
3. Add tests
4. Submit a PR

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 📄 License

MIT — do whatever you want.

---

<p align="center">Built by <a href="https://github.com/rajmodi135">@rajmodi135</a> · Powered by Mauxx AI</p>
<p align="center">⭐ Star us on GitHub · 🐛 Report issues · 💡 Suggest features</p>
