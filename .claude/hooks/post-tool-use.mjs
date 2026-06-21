#!/usr/bin/env node
// PostToolUse hook — tracks tool accuracy and cost
// Runs after EVERY tool call. Auto-logs to logs/accuracy.log
// and updates state/tool-accuracy.md

import { appendFileSync, existsSync, mkdirSync, readFileSync, writeFileSync } from 'fs';
import { resolve, dirname, join } from 'path';
import { fileURLToPath } from 'url';
import { homedir } from 'os';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const MAUXX_HOME = process.env.MAUXX_HOME || resolve(__dirname, '../..');

function log(msg) {
  process.stderr.write(`[post-tool-use] ${msg}\n`);
}

function ensureDir(p) {
  if (!existsSync(p)) mkdirSync(p, { recursive: true });
}

function getLogPath() {
  return join(MAUXX_HOME, 'logs', 'accuracy.log');
}

function getStatePath() {
  return join(MAUXX_HOME, 'memory', 'state', 'tool-accuracy.md');
}

function getCostPath() {
  return join(MAUXX_HOME, 'memory', 'state', 'cost-tracker.md');
}

function readStdin() {
  return new Promise((resolve) => {
    let data = '';
    process.stdin.on('data', (chunk) => data += chunk);
    process.stdin.on('end', () => resolve(data));
  });
}

async function main() {
  const input = await readStdin();
  if (!input) return;

  let event;
  try {
    event = JSON.parse(input);
  } catch {
    return; // not JSON, ignore
  }

  // Extract tool info
  const tool = event.tool_name || 'unknown';
  const result = event.error ? 'failure' : 'success';
  const context = event.tool_input?.file_path || event.tool_input?.command?.slice(0, 80) || '';
  const duration = event.duration_ms || 0;
  const timestamp = new Date().toISOString();

  // Ensure dirs
  ensureDir(join(MAUXX_HOME, 'logs'));
  ensureDir(join(MAUXX_HOME, 'memory', 'state'));

  // Append to accuracy log
  const logLine = `[${timestamp}] tool=${tool} result=${result} context="${context}" duration_ms=${duration}\n`;
  appendFileSync(getLogPath(), logLine, 'utf8');

  // Every 10 calls, update state/tool-accuracy.md
  // (we don't do this synchronously — would be too slow)
  // Instead, log intent: a separate script aggregates
  log(`logged ${tool}=${result}`);

  // If failure, check if needs escalation
  if (result === 'failure') {
    log(`⚠ tool failure: ${tool} (context: ${context})`);
    // Auto-heal will pick this up on next iteration
  }
}

main().catch((e) => {
  log(`error: ${e.message}`);
  process.exit(0); // don't fail the tool call
});
