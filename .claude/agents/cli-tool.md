---
name: cli-tool
description: "Preset for CLI tool development (Python + Typer + PyPI OR Node + Commander + npm)"
metadata:
  type: agent-preset
  version: 1
  stack:
    python: ["typer", "click", "argparse", "rich"]
    node: ["commander", "yargs", "oclif"]
    rust: ["clap", "structopt"]
  modelTier: "haiku"
---

# CLI Tool Preset

**Auto-configures the AI company for CLI tool development.**

## Detected Stack

Triggers when project has:
- `pyproject.toml` with [typer, click, rich]
- `package.json` with [commander, yargs, oclif]
- `Cargo.toml` with clap

## Auto-Configured Agents

| Agent | Role | Tools |
|-------|------|-------|
| **CLI Architect** | Argument parsing, command structure | Sonnet |
| **CLI Dev** | Commands, flags, subcommands | Sonnet |
| **UX Dev** | Rich output, progress bars, colors | Sonnet + frontend-design |
| **Distribution** | PyPI/npm/Homebrew packaging | Sonnet |
| **Tester** | E2E, snapshot tests | Sonnet + verify |
| **Documenter** | README, --help, man pages | Sonnet + deep-research |

## Workflow

```
New Command → CLI Architect (design) → parallel:
  - CLI Dev (implementation)
  - UX Dev (rich output)
→ Tester (snapshot tests)
→ Documenter (--help, README, man)
→ Distribution (publish)
```

## Conventions

- **Python:** Typer + Rich for output
- **Node:** Commander + chalk + ora
- **Errors:** Exit codes, structured JSON error output
- **Help:** Auto-generated from docstrings
- **Versioning:** SemVer
- **Distribution:** PyPI/npm + GitHub Releases + Homebrew tap

## Pre-loaded Skills

- frontend-design (rich output)
- code-review
- verify (run commands)
- simplify

## Quick Start

```bash
echo "preset: cli-tool" >> CLAUDE.md
claude --config .claude/settings.json --task "Add a 'db migrate' subcommand"
```
