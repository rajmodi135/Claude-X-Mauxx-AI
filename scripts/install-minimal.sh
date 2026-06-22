#!/usr/bin/env bash
# Mauxx AI — Quick Install for Claude x Mauxx AI
set -e
git clone https://github.com/rajmodi135/Claude-X-Mauxx-AI.git /tmp/Claude-x-Mauxx-AI 2>/dev/null || true
cd /tmp/Claude-x-Mauxx-AI && git pull 2>/dev/null || true
echo "Claude x Mauxx AI installed. Run: claude --config /tmp/Claude-x-Mauxx-AI/.claude/settings.json"
