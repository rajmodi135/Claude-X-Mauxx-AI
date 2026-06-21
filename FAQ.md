# Frequently Asked Questions

## General

### What is Claude × Mauxx AI?
A self-driving AI company that runs inside Claude Code. It works 24/7, plans, codes, tests, tracks accuracy, and self-improves — without permission prompts.

### Is this free?
Yes. The system itself is open-source (MIT). You only pay for Claude API usage (~$5-10/month typical project).

### Do I need Claude Code installed?
Yes. Install with `npm install -g @anthropic-ai/claude-code`.

### Does it work on Windows / Mac / Linux?
Yes, all three.

## Installation

### How do I install?
```bash
# Easiest:
npm install -g claude-x-mauxx-ai

# Or from source:
git clone https://github.com/rajmodi135/Claude-X-Mauxx-AI.git
claude --config Claude-X-Mauxx-AI/.claude/settings.json
```

### Does it work with any model?
Yes. Supports Anthropic Claude (Opus/Sonnet/Haiku), OpenAI, Google Gemini, Ollama (local), or any compatible API.

### Does it work offline?
Partially. With Ollama running locally, simple tasks (classify, format, edit) work offline. Complex tasks need API access.

## Usage

### What does "ultracode" mean?
The highest effort level: xhigh + dynamic workflow orchestration. Every task uses multi-agent pipelines when appropriate.

### Can I customize the AI company?
Yes. Edit `CLAUDE.md` or use `/config`. Change model, budget, skills, presets, profession.

### How does the memory system work?
File-based markdown. Each plan/fact/decision is a file. `MEMORY.md` is the index (always loaded first). System uses vector search to find relevant context.

### What happens if I run out of tokens?
System auto-summarizes at 70% context. Hard-saves and exits at 85%. On next run, resumes from snapshot.

## Cost

### How much does it cost?
Depends on usage:
- Light (occasional help): $1-2/month
- Medium (daily coding): $5-10/month
- Heavy (24/7 autonomous): $30-50/month

The system auto-routes to cheapest model. Default budget: $50/month.

### Can I use a free model?
Yes. Install Ollama locally and set:
```bash
/config model ollama:llama3.1
```
Then all tasks route to local LLM (free, but slower).

### How do I track costs?
Run `/cost` anytime. The system logs every model call.

## Privacy & Security

### Where is my data stored?
- Memory files: locally in your project
- Logs: locally in `.claude/`
- Tickets (if using Cloudflare Worker): Cloudflare edge
- Nothing on Mauxx AI servers (we don't have any)

### Can I self-host everything?
Yes. Skip the Cloudflare Worker, use Ollama for local LLM, store tickets in a local SQLite. Fully air-gapped mode coming in v7.

### Is the code audited?
Not yet. The system is open-source so you can audit it yourself. SOC2/HIPAA compliance planned for v7.

## Troubleshooting

### "Permission denied" errors
Run `claude --dangerously-skip-permissions` or set `skipDangerousModePermissionPrompt: true` in settings.

### Memory system not loading
Check that `memory/MEMORY.md` exists. Run `/init` to recreate.

### TUI not displaying correctly
Try a different terminal (Windows Terminal, iTerm2, Alacritty). Some terminals don't support true color.

### Ollama not detected
Ensure Ollama is running: `ollama serve` in another terminal.

### "Out of context" errors
System should auto-summarize. If not, run `/simplify` or increase `autoCompactThreshold`.

## Contributing

### How can I contribute?
- Add a preset agent (`.claude/agents/<name>.md`)
- Add a skill (`.claude/skills/<name>.md`)
- Improve documentation
- Report bugs
- Share your preset in Discussions

### What's the licensing?
MIT. Do whatever you want.

### Where can I get help?
- GitHub Issues
- GitHub Discussions
- Discord (link in README)
