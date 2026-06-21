# Claude x Mauxx AI — Diagnostic Script
# Checks system health and reports issues

Write-Host "═══ Claude x Mauxx AI — Doctor ═══" -ForegroundColor Cyan
Write-Host ""

$issues = 0

# Check Claude CLI
try {
    $v = claude --version 2>$null
    Write-Host "✓ Claude Code: $v" -ForegroundColor Green
} catch {
    Write-Host "✗ Claude Code not found. Install: npm install -g @anthropic-ai/claude-code" -ForegroundColor Red
    $issues++
}

# Check Node.js
try {
    $v = node --version
    Write-Host "✓ Node.js: $v" -ForegroundColor Green
} catch {
    Write-Host "✗ Node.js not found. Install from https://nodejs.org" -ForegroundColor Red
    $issues++
}

# Check Python
try {
    $v = python --version
    Write-Host "✓ Python: $v" -ForegroundColor Green
} catch {
    Write-Host "⚠ Python not found (only needed for TUI)" -ForegroundColor Yellow
}

# Check settings.json
$settingsPath = "$PSScriptRoot\..\.claude\settings.json"
if (Test-Path $settingsPath) {
    Write-Host "✓ settings.json exists" -ForegroundColor Green
} else {
    Write-Host "✗ settings.json not found" -ForegroundColor Red
    $issues++
}

# Check CLAUDE.md
$claudePath = "$PSScriptRoot\..\CLAUDE.md"
if (Test-Path $claudePath) {
    Write-Host "✓ CLAUDE.md exists" -ForegroundColor Green
} else {
    Write-Host "✗ CLAUDE.md not found" -ForegroundColor Red
    $issues++
}

# Check memory directory
if (Test-Path "$PSScriptRoot\..\memory") {
    Write-Host "✓ memory directory exists" -ForegroundColor Green
} else {
    Write-Host "⚠ memory directory missing (will be created on first run)" -ForegroundColor Yellow
}

# Check skills
$skillsCount = (Get-ChildItem "$PSScriptRoot\..\.claude\skills\*.md" -ErrorAction SilentlyContinue).Count
Write-Host "✓ $skillsCount skills loaded" -ForegroundColor Green

# Check agents
$agentsCount = (Get-ChildItem "$PSScriptRoot\..\.claude\agents\*.md" -ErrorAction SilentlyContinue).Count
Write-Host "✓ $agentsCount preset agents" -ForegroundColor Green

# Check hooks
$hooksCount = (Get-ChildItem "$PSScriptRoot\..\.claude\hooks\*.mjs" -ErrorAction SilentlyContinue).Count
Write-Host "✓ $hooksCount hooks active" -ForegroundColor Green

# Git status
try {
    $status = git -C "$PSScriptRoot\.." status --short
    if ($status) {
        Write-Host "⚠ Uncommitted changes:" -ForegroundColor Yellow
        $status | ForEach-Object { Write-Host "   $_" -ForegroundColor Gray }
    } else {
        Write-Host "✓ No uncommitted changes" -ForegroundColor Green
    }
} catch {
    Write-Host "⚠ Not a git repository" -ForegroundColor Yellow
}

Write-Host ""
if ($issues -eq 0) {
    Write-Host "═══ All checks passed. 🚀 Mauxx AI is healthy. ═══" -ForegroundColor Green
} else {
    Write-Host "═══ $issues issue(s) found. Run the suggested fixes. ═══" -ForegroundColor Yellow
}
