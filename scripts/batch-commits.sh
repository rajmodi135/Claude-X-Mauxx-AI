#!/usr/bin/env bash
# Claude x Mauxx AI — Batch Commit Script
# Makes atomic commits for each component
set -e

cd "$(dirname "$0")/.."

echo "═══ Claude x Mauxx AI — Batch Commits ═══"
echo ""

# Function to commit if there are staged changes
commit() {
    local msg="$1"
    shift
    if [ $# -gt 0 ]; then
        git add "$@"
    fi

    # Check if anything staged
    if git diff --cached --quiet; then
        echo "  ⏭ No changes: $msg"
        return 0
    fi

    git commit -m "$msg"
    echo "  ✅ $msg"
}

# ── v2 Core System ──
echo "[v2] Core System..."

commit "feat(core): CLAUDE.md v2 — skill-first, model tiering" CLAUDE.md

# ── v2 Smart Skills ──
echo ""
echo "[v2] Smart Skills..."

commit "feat(skill): model-router — auto-pick cheapest model per task" .claude/skills/model-router.md
commit "feat(skill): smart-memory — vector search over past plans" .claude/skills/smart-memory.md
commit "feat(skill): cost-optimizer — real-time spend tracking + auto-throttle" .claude/skills/cost-optimizer.md
commit "feat(skill): predictive-loader — pre-fetch context, reduce tool calls 40%" .claude/skills/predictive-loader.md
commit "feat(skill): orchestrate — multi-agent coordinator" .claude/skills/orchestrate.md
commit "feat(skill): accuracy-monitor — tool accuracy dashboard + auto-unlock" .claude/skills/accuracy-monitor.md
commit "feat(skill): auto-heal — 3x retry with backoff, self-healing" .claude/skills/auto-heal.md

# ── v2 Hooks ──
echo ""
echo "[v2] Lifecycle Hooks..."

commit "feat(hook): PostToolUse — auto-track tool accuracy + cost" .claude/hooks/post-tool-use.mjs
commit "feat(hook): UserPromptSubmit — predictive context pre-loading" .claude/hooks/predictive-loader.mjs
commit "feat(hook): SessionStart — memory bootstrap + heartbeat" .claude/hooks/session-start.mjs
commit "feat(hook): PreCompact — save state before context summary" .claude/hooks/pre-compact.mjs
commit "feat(hook): hooks.json — wire all lifecycle hooks" .claude/hooks/hooks.json

# ── v2 Preset Agents ──
echo ""
echo "[v2] Preset Agents..."

commit "feat(preset): webapp-fullstack — React/Vue + FastAPI + DB agents" .claude/agents/webapp-fullstack.md
commit "feat(preset): api-microservice — API + Docker + K8s agents" .claude/agents/api-microservice.md
commit "feat(preset): security-audit — SAST + DAST + compliance agents" .claude/agents/security-audit.md
commit "feat(preset): perf-tuning — profiler + load test + cache agents" .claude/agents/perf-tuning.md
commit "feat(preset): agents README — usage guide + auto-detection" .claude/agents/README.md

# ── v2 Settings ──
echo ""
echo "[v2] Configuration..."

commit "feat(config): update settings.json with hooks + smart features" .claude/settings.json

# ── v2 Free-Tier Integrations ──
echo ""
echo "[v2] Free-Tier Integrations..."

commit "feat(ci): GitHub Actions — CI with lint, test, verify" .github/workflows/ci.yml
commit "feat(ci): GitHub Actions — auto-release to npm" .github/workflows/release.yml
commit "feat(ci): GitHub Actions — first-run auto-reply" .github/workflows/first-run.yml
commit "feat(cf): Cloudflare Worker — ticket API + support edge" cloudflare-worker/src/index.js cloudflare-worker/wrangler.toml
commit "feat(ollama): setup script — local LLM for $0 routing" scripts/ollama-setup.sh
commit "feat(cost): tracker script — parse logs, report spend" scripts/cost-tracker.mjs

# ── v2 Smart Features Roadmap ──
echo ""
echo "[v2] Documentation..."

commit "docs: SMART_FEATURES_ROADMAP — v2 architecture blueprint" SMART_FEATURES_ROADMAP.md

# ── v2 Neon TUI ──
echo ""
echo "[v2] Neon TUI..."

commit "feat(tui): agent-animation — Mauxx mascot with ASCII faces + moods" tui/agent_animation.py
commit "feat(tui): profession-onboarding — 8 professions with suggestions" tui/profession_onboarding.py
commit "feat(tui): claude-wrapper — async Claude Code subprocess + stats parser" tui/claude_wrapper.py
commit "feat(tui): main app — full TUI with stats bar, input, agent panel" tui/mauxx_tui.py
commit "feat(tui): neon theme — dark + neon CSS theme" tui/neon.tcss
commit "feat(tui): requirements + entry point" tui/requirements.txt tui/__init__.py tui/run.py
commit "feat(tui): bin/mauxx — TUI entry point" bin/mauxx

# ── v2 Version Roadmap ──
echo ""
echo "[v2] Version Roadmap..."

commit "docs: VERSION_ROADMAP — v1 to v10, 1000+ commits plan" VERSION_ROADMAP.md

# ── Summary ──
echo ""
echo "═══ Summary ═══"
git log --oneline --count
echo "commits total"
echo "═══ DONE ═══"
