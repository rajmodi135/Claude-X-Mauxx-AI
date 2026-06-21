# Claude x Mauxx AI — Slash Command
# Invoke: /mauxx

Loads the full Claude x Mauxx AI autonomous system.

## What It Does
1. Reads memory/MEMORY.md for active plans
2. Reads all rule-*.md files for behavioral guidelines
3. Checks state-session-snapshot.md for resume state
4. Picks the highest-priority plan from state-priority-queue.md
5. Delegates execution to the appropriate agent (CTO, Dev, QA, etc.)
6. Updates plan files and memory index in real-time
7. Logs tool accuracy to state-tool-accuracy.md

## Usage
```
/mauxx              — start/resume autonomous work
/mauxx plan <desc>  — create a new plan from description
/mauxx resume       — resume last active plan
/mauxx status       — show system status
```

## First-Run (project not yet onboarded)
On first run in a new project, the system:
1. Scans all .md files in the project
2. Detects tech stack (package.json, pyproject.toml, etc.)
3. Saves project structure to memory/fact-command-personal-memory.md
4. Creates plan-project-onboarding.md
5. Begins autonomous work
