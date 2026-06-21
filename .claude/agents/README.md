# Claude x Mauxx AI — Preset Agent Library

Drop-in agent configurations for common project types. Use by setting `preset: <name>` in your project's `CLAUDE.md`.

## Available Presets

| Preset | Use For | Stack |
|--------|---------|-------|
| [`webapp-fullstack`](./webapp-fullstack.md) | React/Vue + FastAPI/Express + DB | Frontend + Backend + DB + Auth |
| [`api-microservice`](./api-microservice.md) | REST/GraphQL API + Docker + K8s | API + Containers + Observability |
| [`security-audit`](./security-audit.md) | Security audit / pentest | SAST + DAST + Compliance |
| [`perf-tuning`](./perf-tuning.md) | Performance optimization | Profiling + Load + Cache |

## Coming Soon

- `mobile-app` (React Native + Expo)
- `data-pipeline` (Python + Airflow)
- `cli-tool` (Python + Typer + PyPI)
- `docs-site` (Docusaurus + MDX)
- `ml-training` (PyTorch + W&B)
- `blockchain` (Solidity + Hardhat)

## Usage

### Method 1: Project CLAUDE.md
```bash
echo "preset: webapp-fullstack" >> CLAUDE.md
claude --config ~/.claude-x-mauxx-ai/.claude/settings.json
```

### Method 2: Command line
```bash
claude --config ~/.claude-x-mauxx-ai/.claude/settings.json --preset webapp-fullstack
```

### Method 3: Settings.json override
```json
{
  "claudeMauxxAI": {
    "preset": "webapp-fullstack"
  }
}
```

## Creating a Custom Preset

Create a new file in this directory with YAML frontmatter:

```yaml
---
name: my-preset
description: "What this preset does"
metadata:
  type: agent-preset
  version: 1
  modelTier: sonnet
  stack:
    language: [python]
    framework: [fastapi]
---
```

Then define:
- Detected stack triggers
- Auto-configured agents
- Default workflow
- Conventions
- Pre-loaded skills

## Auto-Detection

If no preset is specified, the system auto-detects based on:
1. Files in project root (package.json, pyproject.toml, etc.)
2. Directory structure (web_app/, src-tauri/, k8s/)
3. Dependencies (React, FastAPI, Docker)
4. Existing tooling (.github/workflows/, .claude/)

Best match wins. If ambiguous, user is prompted.
