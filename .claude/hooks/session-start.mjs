#!/usr/bin/env node
// SessionStart hook — bootstrap on every session
// Loads memory, checks state, outputs resume context

import { existsSync, readFileSync, writeFileSync, mkdirSync } from 'fs';
import { resolve, dirname, join } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const MAUXX_HOME = process.env.MAUXX_HOME || resolve(__dirname, '../..');

function readStdin() {
  return new Promise((resolve) => {
    let data = '';
    process.stdin.on('data', (chunk) => data += chunk);
    process.stdin.on('end', () => resolve(data));
  });
}

function ensureDir(p) {
  if (!existsSync(p)) mkdirSync(p, { recursive: true });
}

async function main() {
  const input = await readStdin();

  // Ensure memory directory exists
  ensureDir(join(MAUXX_HOME, 'memory', 'state'));
  ensureDir(join(MAUXX_HOME, 'logs'));

  // Create initial MEMORY.md if missing
  const memoryIdx = join(MAUXX_HOME, 'memory', 'MEMORY.md');
  if (!existsSync(memoryIdx)) {
    writeFileSync(memoryIdx, `# Claude x Mauxx AI — Memory Index

> Auto-created by SessionStart hook
> Last Updated: ${new Date().toISOString()}

## Active Plans
*(none yet — first run)*

## Rules
- See CLAUDE.md for behavioral rules

## State Files
- [[state-session-snapshot]]
- [[state-priority-queue]]
- [[state-resource-budget]]
- [[state-tool-accuracy]]
- [[state-cost-tracker]]
`, 'utf8');
  }

  // Update heartbeat
  const heartbeat = join(MAUXX_HOME, 'memory', 'state', 'heartbeat.md');
  const ts = new Date().toISOString();
  let content = `# Heartbeat\n\nLast alive: ${ts}\n`;
  if (existsSync(heartbeat)) {
    content = readFileSync(heartbeat, 'utf8') + `\n${ts} - session start`;
    // Keep only last 50 lines
    const lines = content.split('\n');
    if (lines.length > 50) {
      content = lines.slice(-50).join('\n');
    }
  }
  writeFileSync(heartbeat, content, 'utf8');

  // Output session context
  const output = {
    additionalContext: [
      '🎯 Claude x Mauxx AI v2 — skill-first, model-tiered, free-tier integrated',
      '💰 Cost optimization active (Haiku for triage, Sonnet for code, Opus for architecture)',
      '🧠 Smart memory active (vector search over past work)',
      '📊 Tool accuracy tracking enabled (auto-unlock at 85%/90%/95%/98%)',
      '🛡️ Auto-heal active (3x retry with backoff, then escalation)',
      '⚡ Predictive loader active (pre-fetch likely context)',
    ],
  };

  console.log(JSON.stringify(output));
}

main().catch(() => {
  console.log('{}');
});
