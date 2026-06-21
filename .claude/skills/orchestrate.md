---
name: orchestrate
description: "Multi-agent workflow coordinator. Routes tasks to specialized agents (CTO, Dev, QA, etc.) with smart delegation and parallel execution."
metadata:
  type: skill
  category: orchestration
  version: 1
---

# Orchestrate Skill

**Coordinator for multi-agent workflows.** Delegates work to specialized agents.

## When to Use

- Task requires multiple roles (design + implement + test)
- Complex multi-step work
- Parallel agent execution

## Agent Roster

| Role | subagent_type | Specialty |
|------|---------------|-----------|
| CEO/Orchestrator | (this session) | Plans, delegates |
| CTO/Architect | `Plan` | Tech design, system choice |
| Dev Team | `general-purpose` | Code, edit, commit |
| QA/Verifier | `code-review` or `general-purpose` | Tests, review |
| Memory Keeper | `general-purpose` | Plan updates |
| Innovation Lead | `general-purpose` | Accuracy analysis |
| Support Team | `general-purpose` | Ticket triage |
| Security | `security-review` | Security audit |
| Designer | `general-purpose` + `frontend-design` | UI/UX |
| Researcher | `general-purpose` + `deep-research` | Research |
| Verifier | `general-purpose` + `verify` | Run + verify |

## Workflow Patterns

### Pattern 1: Sequential
```
CEO → CTO (design) → Dev (implement) → QA (test) → Memory (update)
```

### Pattern 2: Parallel
```
CEO → (Dev in parallel) + (Designer in parallel) → QA → Memory
```

### Pattern 3: Iterative
```
CEO → Dev → QA → if fail: Dev → QA → repeat → if pass: Memory
```

## Invocation

```python
# Sequential
result = orchestrate([
    ("Plan", "Design the auth system"),
    ("general-purpose", "Implement auth based on this design: {result_1}"),
    ("code-review", "Review the implementation: {result_2}"),
])

# Parallel
results = parallel([
    ("general-purpose", "Build the API endpoints"),
    ("general-purpose", "Build the frontend"),
    ("general-purpose", "Write the tests"),
])
# Then: ("code-review", "Review all of these: {results}")
```

## Auto-Choose Workflow

```python
def choose_workflow(task):
    if task.complexity == "low":
        return "single-agent"
    if task.requires_design_and_implementation:
        return "sequential-cto-dev-qa"
    if task.has_independent_components:
        return "parallel-dev-then-qa"
    if task.has_retry_loop:
        return "iterative-with-retry"
    return "sequential-default"
```

## State Management

Each agent receives:
- Plan context (which plan, which step)
- Previous agent's output (chained)
- Relevant memory files (via `[[wiki-links]]`)
- Tool tier available (based on accuracy)

Each agent produces:
- Output for next agent
- Update to `state/agent-output.md`
- Logging of actions to `logs/agents.log`

## Cost Control

- Use Haiku for triage agents (e.g., "is this a bug?")
- Use Sonnet for dev/QA (default)
- Use Opus only for CTO/architecture
- Cache outputs for re-use

## Example

```python
# User: "Add user authentication to the app"
workflow = orchestrate([
    Plan("Design auth system — JWT vs session, libraries, tradeoffs"),
    parallel([
        general-purpose("Implement backend auth endpoints"),
        general-purpose("Implement frontend login UI"),
    ]),
    code-review("Review the full auth implementation"),
    general-purpose("Update memory with auth architecture decision"),
])
# Cost: ~$0.05 (mostly Sonnet) vs $0.50 always-Opus
```

---

🎯 **Result: Right agent for the right job, in parallel when possible.**
