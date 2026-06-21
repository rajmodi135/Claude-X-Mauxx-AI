---
name: model-router
description: "Auto-pick the cheapest Claude model that can handle the task. Saves 85%+ on API costs vs always-Opus."
metadata:
  type: skill
  category: cost-optimization
  version: 1
  costImpact: high
---

# Model Router Skill

**Auto-loaded on session start.** Picks the cheapest model that can do the job.

## Routing Table

| Task Type | Model | Cost (1M tok in/out) | Triggers |
|-----------|-------|---------------------|----------|
| Classify, sort, format, search | **Haiku 4.5** | $0.25 / $1.25 | Intent detection, file routing, sort/filter |
| Cache hit (repeated pattern) | **Cache** | 10% of base | Same prompt rephrased |
| Local trivial (no API needed) | **Ollama:llama3.1** | **$0** | Simple edits, formatting, JSON transforms |
| Code edit, test, review | **Sonnet 4.6** | $3 / $15 | Default for any code work |
| Architecture, design, critical | **Opus 4.8** | $15 / $75 | Multi-system design, only when truly needed |

## Decision Logic

```python
def pick_model(task, prompt):
    # 1. Cache first (cheapest)
    if cache_hit_available(prompt_hash):
        return "cache"
    
    # 2. Local if trivial
    if task.complexity == "trivial" and ollama_available():
        return "ollama:llama3.1"
    
    # 3. Haiku for simple decisions
    if task.type in CLASSIFY_TYPES:
        return "haiku"
    
    # 4. Sonnet for code
    if task.type in CODE_TYPES:
        return "sonnet"
    
    # 5. Opus only for architecture
    if task.requires_architecture:
        return "opus"
    
    # 6. Default: Sonnet (best balance)
    return "sonnet"
```

## Classify Types (use Haiku)

- File routing: "which directory should this go in?"
- Intent detection: "is this a bug, feature, or question?"
- Triage: "prioritize these 10 tasks"
- Sort/filter: "find all auth-related files"
- Format conversion: "convert this to JSON"
- Simple lookup: "what's the API for X?"

## Code Types (use Sonnet)

- Edit a function
- Write a test
- Refactor a module
- Run code review
- Generate boilerplate
- Bug investigation (single file)
- Documentation

## Architecture Types (use Opus — sparingly)

- Multi-system design
- Choose between competing approaches
- Critical security decisions
- Performance-critical algorithms
- Database schema design (complex)

## Tracking

Log every model choice to `state/cost-tracker.md`:
```markdown
| Time | Task | Model | Tokens in/out | Cost |
|------|------|-------|---------------|------|
| 14:30 | classify intent | haiku | 200/50 | $0.0001 |
| 14:31 | edit auth.py | sonnet | 1500/800 | $0.017 |
| 14:32 | design system | opus | 3000/2000 | $0.195 |
```

## Usage

This skill is **automatic** — you don't need to invoke it manually. The CLAUDE.md operating instructions include the routing logic.

## Monthly Budget

- Default: $50/month per project
- Warning at: $40
- Hard stop at: $50 (queue non-critical work)
- Configurable in `.claude/settings.json` → `claudeMauxxAI.budget`

## Cost Comparison

| Scenario | Always-Opus | With Router | Savings |
|----------|-------------|-------------|---------|
| Classify 100 intents | $15.00 | $0.025 | **99.8%** |
| Edit 50 files | $75.00 | $1.50 | **98%** |
| Mix: 70% haiku + 25% sonnet + 5% opus | $150.00 | $8.00 | **95%** |

---

💰 **Result: Same work, 85%+ cheaper.**
