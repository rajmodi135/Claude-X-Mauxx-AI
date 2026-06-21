# Claude × Mauxx AI — Architecture

## High-Level

```
User Command → CLI/TUI → Claude Code + Skills + Memory + Agents → Result
```

## Components

### 1. Memory System (`memory/`)
- `MEMORY.md` — index, always read first
- `plan-*.md` — active plans
- `archive-*.md` — completed plans
- `fact-*.md` — decisions, bugs, project state
- `rule-*.md` — behavioral rules
- `state-*.md` — runtime state (queue, heartbeat, cost, accuracy)

### 2. Skill System (`.claude/skills/`)
- 13+ auto-loaded skills
- Each skill: YAML frontmatter + markdown body
- Skills are pure markdown (no code required)
- Auto-activated when relevant

### 3. Preset Agents (`.claude/agents/`)
- 9 project-specific configurations
- Auto-detected from project files
- Each defines: agents, workflow, conventions, skills

### 4. Lifecycle Hooks (`.claude/hooks/`)
- `PostToolUse` — track tool accuracy
- `UserPromptSubmit` — predictive context loading
- `SessionStart` — memory bootstrap + heartbeat
- `PreCompact` — save state before compaction

### 5. Neon TUI (`tui/`)
- Python Textual app
- Profession onboarding
- Stats bar (tokens, tasks, ETA)
- Animated Mauxx mascot
- Claude Code subprocess wrapper

### 6. Free-Tier Stack
- GitHub Actions (CI/CD)
- Cloudflare Workers (support API)
- Ollama (local LLM)
- Supabase (optional, for tickets)
- Sentry (optional, for errors)

## Data Flow

```
┌─────────────┐
│ User Input  │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│ SessionStart hook   │ → Read MEMORY.md
│                     │ → Load state files
│                     │ → Bootstrap if needed
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ UserPromptSubmit    │ → Analyze intent
│ (predictive-loader) │ → Pick model (Haiku/Sonnet/Opus)
│                     │ → Pre-fetch context
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Orchestrator (CEO)  │ → Read priority queue
│                     │ → Pick plan
│                     │ → Delegate to agent
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Skill/Agent         │ → Execute task
│                     │ → Use cheapest model
│                     │ → Log accuracy
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ PostToolUse hook    │ → Track tool result
│                     │ → Update accuracy stats
│                     │ → Update cost tracker
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Memory Keeper       │ → Update plan file
│                     │ → Update MEMORY.md
│                     │ → Save snapshot
└─────────────────────┘
```

## Cost Optimization

| Layer | Optimization |
|-------|--------------|
| Input | Smart-memory (cache) + Prompt caching |
| Model | Haiku for triage, Sonnet for code, Opus for architecture |
| Local | Ollama for trivial tasks |
| Output | Token-efficient responses |
| Routing | Auto-route by cost threshold |

## Accuracy → Unlock

```
Tool accuracy ≥ 85% for 30 uses → Tier 2 tools unlocked
Tool accuracy ≥ 90% for 30 uses → Tier 3 tools unlocked
Tool accuracy ≥ 95% for 30 uses → Tier 4 tools unlocked
Tool accuracy ≥ 98% for 30 uses → Tier 5 tools unlocked
```
