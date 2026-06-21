#!/usr/bin/env bash
# Claude x Mauxx AI — Update Script
# Updates to the latest version from GitHub

set -e

echo "═══ Claude x Mauxx AI — Update ═══"
echo ""

MAUXX_HOME="$(cd "$(dirname "$0")/.." && pwd)"

cd "$MAUXX_HOME"

# Check if git repo
if [ -d ".git" ]; then
    echo "Pulling latest from GitHub..."
    git pull origin main
    echo "✓ Updated to latest version"
else
    echo "Not a git clone. Re-downloading..."
    cd /tmp
    rm -rf claude-x-mauxx-ai-temp
    git clone https://github.com/rajmodi135/Claude-X-Mauxx-AI.git claude-x-mauxx-ai-temp
    cp -r claude-x-mauxx-ai-temp/* "$MAUXX_HOME/"
    rm -rf claude-x-mauxx-ai-temp
    echo "✓ Updated to latest version"
fi

# Update version tag
echo ""
echo "Current version:"
git describe --tags --abbrev=0 2>/dev/null || echo "(no tags)"
echo ""

echo "Done. Restart Mauxx AI to apply changes."
