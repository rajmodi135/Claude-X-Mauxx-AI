#!/usr/bin/env bash
# Claude x Mauxx AI — Mac/Linux Installer
# One-click setup for the autonomous AI company

set -e

REPO_URL="https://github.com/rajmodi135/Claude-X-Mauxx-AI.git"
INSTALL_DIR="${HOME}/.claude-x-mauxx-ai"

echo ""
echo "=================================================="
echo "  Claude x Mauxx AI - Installer"
echo "=================================================="
echo ""

# Check prerequisites
echo "[1/4] Checking prerequisites..."

if command -v node &>/dev/null; then
    echo "  OK Node.js: $(node --version)"
else
    echo "  FAIL Node.js not found. Install from https://nodejs.org"
    exit 1
fi

if command -v claude &>/dev/null; then
    echo "  OK Claude Code: $(claude --version 2>/dev/null)"
else
    echo "  Claude Code not found. Installing..."
    npm install -g @anthropic-ai/claude-code
fi

# Clone or update
echo ""
echo "[2/4] Setting up Claude x Mauxx AI..."

if [ -d "$INSTALL_DIR" ]; then
    echo "  Updating existing installation..."
    cd "$INSTALL_DIR" && git pull origin main
else
    echo "  Cloning from GitHub..."
    git clone "$REPO_URL" "$INSTALL_DIR"
fi

# Add shell alias
echo ""
echo "[3/4] Registering shell alias..."

ALIAS_LINE="alias claude-mauxx='claude --config ${INSTALL_DIR}/.claude/settings.json'"

for rc_file in "${HOME}/.zshrc" "${HOME}/.bashrc" "${HOME}/.bash_profile"; do
    if [ -f "$rc_file" ]; then
        if ! grep -q "claude-mauxx" "$rc_file" 2>/dev/null; then
            echo "" >> "$rc_file"
            echo "# Claude x Mauxx AI" >> "$rc_file"
            echo "$ALIAS_LINE" >> "$rc_file"
            echo "  OK Added alias to $rc_file"
        else
            echo "  OK Alias already in $rc_file"
        fi
    fi
done

# Verify
echo ""
echo "[4/4] Verifying installation..."

if [ -f "${INSTALL_DIR}/.claude/settings.json" ]; then
    echo "  OK settings.json found"
else
    echo "  FAIL settings.json missing!"
    exit 1
fi

if [ -f "${INSTALL_DIR}/CLAUDE.md" ]; then
    echo "  OK CLAUDE.md found"
else
    echo "  FAIL CLAUDE.md missing!"
    exit 1
fi

echo ""
echo "=================================================="
echo "  Installation Complete!"
echo "=================================================="
echo ""
echo "Run from any project directory:"
echo "  claude-mauxx"
echo ""
echo "Or manually:"
echo "  claude --config ${INSTALL_DIR}/.claude/settings.json"
echo ""
echo "Restart your terminal or run:"
echo "  source ~/.zshrc   # or ~/.bashrc"
echo ""
echo "First run will auto-detect your project structure."
echo ""
