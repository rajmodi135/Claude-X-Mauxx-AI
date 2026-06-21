# 📦 Claude × Mauxx AI — Installation Guide

> Multiple ways to install. Pick the one that fits your workflow.

---

## Prerequisites

- **Claude Code** installed (`claude --version` should work)
- **Node.js ≥ 18** (only for npm method)
- **Git** (only for clone method)

---

## Option 1: npm Global Install (Recommended)

```bash
npm install -g claude-x-mauxx-ai
```

Then from any project:
```bash
cd your-project
claude --config ~/.claude-x-mauxx-ai/.claude/settings.json
```

Or just `npx claude-x-mauxx-ai` for one-off use.

---

## Option 2: Clone the Repo

```bash
git clone https://github.com/rajmodi135/Claude-X-Mauxx-AI.git
cd Claude-X-Mauxx-AI
```

Then point any project to it:
```bash
cd your-project
claude --config /absolute/path/to/Claude-X-Mauxx-AI/.claude/settings.json
```

---

## Option 3: Windows One-Click Install

```powershell
powershell -ExecutionPolicy Bypass -File install.ps1
```

This will:
1. Clone the repo to `%USERPROFILE%\Claude x Mauxx AI`
2. Add a global `claude x mauxx ai` command
3. Verify the installation

---

## Option 4: Mac/Linux One-Click Install

```bash
curl -fsSL https://raw.githubusercontent.com/rajmodi135/Claude-X-Mauxx-AI/main/install.sh | bash
```

This will:
1. Clone the repo to `~/.claude-x-mauxx-ai`
2. Add `claude-mauxx` shell alias
3. Verify the installation

After install, **restart your terminal** or `source ~/.zshrc` / `source ~/.bashrc`.

---

## Option 5: Per-Project Symlink

```bash
cd your-project
ln -s /path/to/Claude-X-Mauxx-AI/.claude .claude-mauxx
claude --config .claude-mauxx/settings.json
```

---

## ✅ Verify Installation

```bash
claude --version
# Should show: claude-code v0.4.x or higher

claude --config /path/to/Claude-X-Mauxx-AI/.claude/settings.json --version
# Should start without errors
```

You should see the banner:
```
===================================================
  Claude x Mauxx AI v1.0
  Project: /your/project
===================================================
```

---

## 🔄 Upgrading

```bash
# npm:
npm update -g claude-x-mauxx-ai

# Clone:
cd Claude-X-Mauxx-AI && git pull origin main

# Re-run installer.
```

---

## 🗑️ Uninstalling

```bash
# npm:
npm uninstall -g claude-x-mauxx-ai

# Manual:
rm -rf ~/.claude-x-mauxx-ai
# Remove alias from ~/.zshrc / ~/.bashrc if you added one
```

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| `claude: command not found` | `npm install -g @anthropic-ai/claude-code` |
| `Permissions prompts appearing` | Check `skipDangerousModePermissionPrompt: true` in settings.json |
| `Memory not persisting` | Ensure `memory/` exists and is writable |
| `Plugin not loading` | Run `/plugins install claude-x-mauxx-ai` inside Claude |
| `Accuracy not tracking` | `logs/` dir is created automatically on first run |
| `Context too large` | System auto-summarizes at 70%. Check `state-resource-budget.md` |

---

## 💡 First-Run Tips

On the first run, the system will:

1. Scan all `.md` files in your project root
2. Detect your tech stack
3. Create a `fact-command-personal-memory.md` — this is your project's permanent memory
4. Create a `plan-project-onboarding.md` — first autonomous plan

The first run takes 1-2 minutes to read your project. Subsequent runs are instant.

**Tip:** Drop a `CLAUDE.md` in your project root with project-specific notes — the system will read it every session.

---

🚀 **Questions?** Open an issue at https://github.com/rajmodi135/Claude-X-Mauxx-AI/issues
