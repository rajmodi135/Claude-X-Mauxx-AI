#!/usr/bin/env node
// Claude x Mauxx AI — npm entry point
// Usage: npx claude-x-mauxx-ai [project-dir]

import { spawn } from 'child_process';
import { existsSync, readFileSync, writeFileSync, mkdirSync } from 'fs';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const MAUXX_HOME = resolve(__dirname, '..');
const PROJECT_DIR = process.argv[2] || process.cwd();

function log(msg) {
  process.stdout.write(`  ${msg}\n`);
}

function welcome() {
  console.log('');
  console.log('==================================================');
  console.log('  Claude x Mauxx AI v1.0');
  console.log(`  Project: ${PROJECT_DIR}`);
  console.log('==================================================');
  console.log('');
}

function ensureMemoryDir() {
  const memDir = resolve(MAUXX_HOME, 'memory');
  if (!existsSync(memDir)) {
    mkdirSync(memDir, { recursive: true });
    log('Created memory/ directory');
  }

  // Create MEMORY.md if missing
  const idxFile = resolve(memDir, 'MEMORY.md');
  if (!existsSync(idxFile)) {
    const idx = `# Claude x Mauxx AI — Memory Index

> Last Updated: ${new Date().toISOString().split('T')[0]}
> Mode: 24/7 Autonomous

## Active Plans
*(none yet — first run)*

## Active Rules
- [[rule-memory-plan-system]]

## State Files
- [[state-session-snapshot]]
- [[state-priority-queue]]
- [[state-resource-budget]]
`;
    writeFileSync(idxFile, idx);
    log('Created memory/MEMORY.md');
  }
}

function run() {
  welcome();
  ensureMemoryDir();

  const configPath = resolve(MAUXX_HOME, '.claude', 'settings.json');

  if (!existsSync(configPath)) {
    console.error('ERROR: .claude/settings.json not found at', configPath);
    process.exit(1);
  }

  log(`Config: ${configPath}`);

  const claude = spawn('claude', [
    `--config`, configPath,
    ...process.argv.slice(2)
  ], {
    cwd: PROJECT_DIR,
    stdio: 'inherit',
    shell: true,
    env: {
      ...process.env,
      CLAUDE_AUTONOMOUS_MODE: 'true',
      CLAUDE_EFFORT_LEVEL: 'ultracode',
      CLAUDE_SKILLS_ALL: 'true',
      CLAUDE_TOOLS_ALL: 'true',
      CLAUDE_LOOP_MODE: '24x7',
      CLAUDE_CONFIG_DIR: resolve(MAUXX_HOME, '.claude'),
      CLAUDE_MEMORY_DIR: resolve(MAUXX_HOME, 'memory'),
    }
  });

  claude.on('exit', (code) => {
    process.exit(code);
  });
}

run();
