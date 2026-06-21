# Claude x Mauxx AI — Windows Installer
# One-click setup for the autonomous AI company

$RepoUrl = "https://github.com/rajmodi135/Claude-X-Mauxx-AI.git"
$InstallDir = "$env:USERPROFILE\Claude x Mauxx AI"

Write-Host ""
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "  Claude x Mauxx AI - Windows Installer" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""

# Check prerequisites
Write-Host "[1/4] Checking prerequisites..." -ForegroundColor Yellow

try {
    $nodeVersion = node --version
    Write-Host "  OK Node.js: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "  FAIL Node.js not found. Please install from https://nodejs.org" -ForegroundColor Red
    exit 1
}

try {
    $claudeVersion = claude --version 2>$null
    Write-Host "  OK Claude Code: $claudeVersion" -ForegroundColor Green
} catch {
    Write-Host "  Claude Code not found. Installing..." -ForegroundColor Yellow
    npm install -g @anthropic-ai/claude-code
}

# Clone or update
Write-Host ""
Write-Host "[2/4] Setting up Claude x Mauxx AI..." -ForegroundColor Yellow

if (Test-Path $InstallDir) {
    Write-Host "  Updating existing installation..." -ForegroundColor White
    Set-Location $InstallDir
    git pull origin main
} else {
    Write-Host "  Cloning from GitHub..." -ForegroundColor White
    git clone $RepoUrl $InstallDir
}

# Create global command
Write-Host ""
Write-Host "[3/4] Registering global command..." -ForegroundColor Yellow

$BatchDir = "$env:USERPROFILE\AppData\Local\Microsoft\WindowsApps"
$BatchPath = "$BatchDir\claude-x-mauxx-ai.cmd"
$BatchContent = "@echo off`r`nsetlocal`r`nset MAUXX_HOME=$($InstallDir -replace '\\', '\\')`r`nset PROJECT_DIR=%CD%`r`ncd /d `"%PROJECT_DIR%`"`r`nclaude --config `"%MAUXX_HOME%\.claude\settings.json`" %*`r`nendlocal`r`n"

if (-not (Test-Path $BatchDir)) { New-Item -ItemType Directory -Path $BatchDir -Force | Out-Null }
$BatchContent | Out-File -FilePath $BatchPath -Encoding ascii -Force
Write-Host "  OK Global command: claude-x-mauxx-ai" -ForegroundColor Green

# Verify
Write-Host ""
Write-Host "[4/4] Verifying installation..." -ForegroundColor Yellow

if (Test-Path "$InstallDir\.claude\settings.json") {
    Write-Host "  OK settings.json found" -ForegroundColor Green
} else {
    Write-Host "  FAIL settings.json missing!" -ForegroundColor Red
    exit 1
}

if (Test-Path "$InstallDir\CLAUDE.md") {
    Write-Host "  OK CLAUDE.md found" -ForegroundColor Green
} else {
    Write-Host "  FAIL CLAUDE.md missing!" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "==================================================" -ForegroundColor Green
Write-Host "  Installation Complete!" -ForegroundColor Green
Write-Host "==================================================" -ForegroundColor Green
Write-Host ""
Write-Host "Run from any project directory:" -ForegroundColor White
Write-Host "  claude-x-mauxx-ai" -ForegroundColor Cyan
Write-Host ""
Write-Host "Or manually:" -ForegroundColor White
Write-Host "  claude --config `"$InstallDir\.claude\settings.json`"" -ForegroundColor Cyan
Write-Host ""
Write-Host "First run will auto-detect your project structure." -ForegroundColor Yellow
Write-Host ""
