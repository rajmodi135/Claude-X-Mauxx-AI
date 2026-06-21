#!/usr/bin/env bash
# Claude x Mauxx AI — Quick Setup for a New Project
# Usage: cd <new-project> && bash /path/to/Claude-x-Mauxx-AI/scripts/setup-new-project.sh

set -e

MAUXX_HOME="$(cd "$(dirname "$0")/.." && pwd)"
PROJECT_DIR="$(pwd)"

echo "═══ Claude x Mauxx AI — Project Setup ═══"
echo ""

# Create symlink to .claude config
echo "Creating .claude symlink..."
ln -sf "$MAUXX_HOME/.claude" "$PROJECT_DIR/.claude"

# Copy CLAUDE.md
echo "Copying CLAUDE.md..."
cp "$MAUXX_HOME/CLAUDE.md" "$PROJECT_DIR/CLAUDE.md"

# Initialize memory
echo "Initializing memory..."
mkdir -p "$PROJECT_DIR/memory"
cat > "$PROJECT_DIR/memory/MEMORY.md" << 'EOF'
# Memory Index — <project-name>

> Last Updated: $(date +%Y-%m-%d)
> Active Plans: 0 | Archives: 0

## Active Plans
*(none yet)*

## State Files
- [[state-session-snapshot]]
- [[state-priority-queue]]
EOF

# Detect project type
echo ""
echo "Detecting project type..."
if [ -f "package.json" ]; then
    echo "  ✓ Node.js project detected"
fi
if [ -f "pyproject.toml" ] || [ -f "requirements.txt" ]; then
    echo "  ✓ Python project detected"
fi
if [ -f "Cargo.toml" ]; then
    echo "  ✓ Rust project detected"
fi
if [ -f "Dockerfile" ]; then
    echo "  ✓ Docker project detected"
fi
if [ -f "docusaurus.config.js" ]; then
    echo "  ✓ Documentation project detected"
fi

echo ""
echo "═══ Setup complete ═══"
echo ""
echo "Run: claude --config .claude/settings.json"
echo "Or:  claude-mauxx"
echo ""
