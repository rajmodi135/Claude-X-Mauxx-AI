#!/usr/bin/env node
// PreCompact hook — save state before context compaction
// Ensures nothing is lost when context is compressed

import { existsSync, writeFileSync, readFileSync } from 'fs';
import { resolve, dirname, join } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const MAUXX_HOME = process.env.MAUXX_HOME || resolve(__dirname, '../..');

async function main() {
  const snapshotPath = join(MAUXX_HOME, 'memory', 'state', 'session-snapshot.md');
  const ts = new Date().toISOString();

  let content = `# Session Snapshot (PreCompact)\n\nTimestamp: ${ts}\n\n`;
  if (existsSync(snapshotPath)) {
    content += readFileSync(snapshotPath, 'utf8');
  }
  content += `\n\n---\n\n## Compaction Notice\n\nContext was compacted at ${ts}. Resume from next plan step.\n`;

  writeFileSync(snapshotPath, content, 'utf8');

  const output = {
    additionalContext: [
      `💾 Pre-compact snapshot saved at ${ts}`,
      'Next session will resume from this snapshot.',
    ],
  };

  console.log(JSON.stringify(output));
}

main().catch(() => {
  console.log('{}');
});
