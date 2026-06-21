#!/usr/bin/env bash
# Claude x Mauxx AI — Diagnostic Script
# Checks system health and reports issues

set -e

MAUXX_HOME="$(cd "$(dirname "$0")/.." && pwd)"
ISSUES=0

echo "═══ Claude x Mauxx AI — Doctor ═══"
echo ""

# Check Claude CLI
if command -v claude &>/dev/null; then
    echo "✓ Claude Code: $(claude --version 2>&1 | head -1)"
else
    echo "✗ Claude Code not found. Install: npm install -g @anthropic-ai/claude-code"
    ISSUES=$((ISSUES+1))
fi

# Check Node.js
if command -v node &>/dev/null; then
    echo "✓ Node.js: $(node --version)"
else
    echo "✗ Node.js not found. Install from https://nodejs.org"
    ISSUES=$((ISSUES+1))
fi

# Check settings.json
if [ -f "$MAUXX_HOME/.claude/settings.json" ]; then
    echo "✓ settings.json exists"
else
    echo "✗ settings.json not found"
    ISSUES=$((ISSUES+1))
fi

# Check CLAUDE.md
if [ -f "$MAUXX_HOME/CLAUDE.md" ]; then
    echo "✓ CLAUDE.md exists"
else
    echo "✗ CLAUDE.md not found"
    ISSUES=$((ISSUES+1))
fi

# Check memory
if [ -d "$MAUXX_HOME/memory" ]; then
    echo "✓ memory directory exists"
else
    echo "⚠ memory directory missing (created on first run)"
fi

# Count skills
SKILLS=$(find "$MAUXX_HOME/.claude/skills" -name "*.md" 2>/dev/null | wc -l)
echo "✓ $SKILLS skills loaded"

# Count agents
AGENTS=$(find "$MAUXX_HOME/.claude/agents" -name "*.md" 2>/dev/null | wc -l)
echo "✓ $AGENTS preset agents"

# Count hooks
HOOKS=$(find "$MAUXX_HOME/.claude/hooks" -name "*.mjs" 2>/dev/null | wc -l)
echo "✓ $HOOKS hooks active"

# Git status
if [ -d "$MAUXX_HOME/.git" ]; then
    if git -C "$MAUXX_HOME" diff --quiet 2>/dev/null; then
        echo "✓ No uncommitted changes"
    else
        echo "⚠ Uncommitted changes exist"
    fi
else
    echo "⚠ Not a git repository"
fi

echo ""
if [ $ISSUES -eq 0 ]; then
    echo "═══ All checks passed. 🚀 Mauxx AI is healthy. ═══"
else
    echo "═══ $ISSUES issue(s) found. Run the suggested fixes. ═══"
fi
