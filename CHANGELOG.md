# Changelog

All notable changes to Claude × Mauxx AI are documented here.

Format: [Semantic Versioning](https://semver.org/)

## [Unreleased]

### Added
- v2 architecture: skill-first, model tiering, free-tier stack
- Neon TUI with profession onboarding
- 7 new skills (emoji-reactions, dependency-analyzer, test-runner, etc.)
- 9 preset agents (webapp, api, security, perf, mobile, data, cli, docs, ml, blockchain)
- 8 new slash commands (/config, /profile, /theme, /deploy, etc.)
- 4 lifecycle hooks (PostToolUse, UserPromptSubmit, SessionStart, PreCompact)
- GitHub Actions CI/CD
- Cloudflare Worker for support tickets
- Ollama setup for local LLMs
- Cost tracking + auto-throttle
- Tool accuracy tracking with auto-unlock at 85%/90%/95%/98%

## [1.0.0] - 2026-06-22

### Added
- Initial release
- Memory & Plan system (file-based markdown)
- CLAUDE.md operating instructions
- Auto-mode permissions
- Basic skill stubs (/plan, /memory, /support, /feedback, /accuracy, /heartbeat)
- npm package: `claude-x-mauxx-ai`
- README, LICENSE, INSTALL, package.json

### Notes
This is the foundation. v2 adds intelligence, TUI, and integrations.

---

## Roadmap

- **v1** (DONE): Foundation
- **v2** (CURRENT): Smart + TUI + Routing + Memory
- **v3** (PLANNED): Plugin marketplace, community presets
- **v4** (PLANNED): Web dashboard, multi-user
- **v5** (PLANNED): Mobile, real-time collaboration
- **v6** (PLANNED): Auto-improvement engine
- **v7** (PLANNED): Enterprise + compliance
- **v8** (PLANNED): Multi-LLM support
- **v9** (PLANNED): Full autonomy, predictive AI
- **v10** (PLANNED): Self-evolving AI IDE

See [VERSION_ROADMAP.md](VERSION_ROADMAP.md) for full plan.
