#!/usr/bin/env node
// Claude x Mauxx AI — Post-Install Setup
// Runs after npm install -g claude-x-mauxx-ai

import { existsSync, mkdirSync, writeFileSync, copyFileSync } from 'fs';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';
import { execSync } from 'child_process';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const MAUXX_HOME = resolve(__dirname, '..');

function log(msg, type = 'OK') {
  process.stdout.write(`  ${type === 'OK' ? '\x1b[32mOK\x1b[0m' : '\x1b[33m--\x1b[0m'} ${msg}\n`);
}

// Ensure memory directory
const memDir = resolve(MAUXX_HOME, 'memory');
if (!existsSync(memDir)) {
  mkdirSync(memDir, { recursive: true });
}

// Create MEMORY.md if missing
const idxFile = resolve(memDir, 'MEMORY.md');
if (!existsSync(idxFile)) {
  const idx = `# Claude x Mauxx AI — Memory Index

> Last Updated: ${new Date().toISOString().split('T')[0]}

## Active Plans
*(none yet — run "claude x mauxx ai" in your project)*

## Rules
- [[rule-memory-plan-system]]

## State Files
- [[state-session-snapshot]]
- [[state-priority-queue]]
- [[state-resource-budget]]
`;
  writeFileSync(idxFile, idx);
}

// Welcome message
console.log('');
console.log('╔══════════════════════════════════════════════╗');
console.log('║       Claude x Mauxx AI installed!          ║');
console.log('╚══════════════════════════════════════════════╝');
console.log('');
console.log('  Run from any project:');
console.log('');
console.log('    npx claude-x-mauxx-ai');
console.log('    # or');
console.log('    claude-x-mauxx-ai');
console.log('');
console.log('  Or point Claude Code directly:');
console.log('');
console.log('    claude --config "' + resolve(MAUXX_HOME, '.claude/settings.json') + '"');
console.log('');
console.log('  First run auto-detects your project structure.');
console.log('  No permission prompts. Full autonomy.');
console.log('');
