# /init — Initialize Project
# Invoke: /init

Initialize Mauxx AI for the current project.

## What It Does

1. **Scans** project structure (package.json, src/, etc.)
2. **Detects** tech stack
3. **Reads** all .md files
4. **Creates** `memory/` directory + initial state files
5. **Saves** `fact-command-personal-memory.md` (project context)
6. **Suggests** profession-based preset
7. **Starts** with the first onboarding plan

## Usage

```
/init           — full initialization
/init --quick   — skip onboarding, use defaults
/init --preset  — specify preset upfront
```

## First-Run Behavior

The system reads all `.md` files in the project root and subfolders (max depth 3). It builds a context file and remembers the project forever in `fact-command-personal-memory.md`.
