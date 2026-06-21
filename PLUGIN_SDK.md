# Claude x Mauxx AI — Plugin SDK

> Build custom presets, skills, and commands.

## Quick Start

Create a file in the right directory:

| Type | Directory | Example |
|------|-----------|---------|
| Skill | `.claude/skills/my-skill.md` | [Example](#skill-example) |
| Command | `.claude/commands/my-cmd.md` | [Example](#command-example) |
| Preset | `.claude/agents/my-preset.md` | [Example](#preset-example) |
| Hook | `.claude/hooks/my-hook.mjs` | [Example](#hook-example) |

---

## Skill Example

```yaml
---
name: my-skill
description: "What this skill does"
metadata:
  type: skill
  category: development
  version: 1
---

# My Skill

## What It Does

Describe the skill's purpose.

## Usage

- `/my-skill <arg>` — do something
- `/my-skill help` — show help

## Integration

Describe how it integrates with other skills.
```

## Command Example

```yaml
# /my-command — Brief description

## Usage

```
/my-command <arg>   — does something
/my-command help     — show help
```

## What It Does

Full description.
```

## Preset Example

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

# My Preset

## Detected Stack

Describe what auto-triggers this preset.

## Auto-Configured Agents

| Agent | Role | Tools |
|-------|------|-------|

## Quick Start

```bash
echo "preset: my-preset" >> CLAUDE.md
claude --config .claude/settings.json
```
```

## Hook Example

```javascript
#!/usr/bin/env node
// .claude/hooks/my-hook.mjs

async function main() {
  const input = await readStdin();
  const event = JSON.parse(input);
  // Handle the event
  const output = { additionalContext: [] };
  console.log(JSON.stringify(output));
}

main().catch(() => console.log('{}'));
```

## Publishing

1. Create your plugin in the right directory
2. Test locally
3. Share via GitHub Discussions or PR
4. We'll add it to the community registry

## Registry

Coming in v3 — a plugin marketplace where community presets and skills are indexed.
