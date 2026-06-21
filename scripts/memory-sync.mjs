#!/usr/bin/env node
// Memory Sync — syncs memory files between projects
// Usage: node scripts/memory-sync.mjs [source-dir] [target-dir]

import { readFileSync, writeFileSync, existsSync, mkdirSync, readdirSync } from 'fs';
import { join } from 'path';

const [source, target] = process.argv.slice(2);

if (!source || !target) {
  console.log('Usage: node scripts/memory-sync.mjs <source-dir> <target-dir>');
  process.exit(1);
}

const sourceDir = join(source, 'memory');
const targetDir = join(target, 'memory');

function ensureDir(dir) {
  if (!existsSync(dir)) mkdirSync(dir, { recursive: true });
}

function syncFiles(type) {
  const srcDir = join(sourceDir, type);
  const tgtDir = join(targetDir, type);

  if (!existsSync(srcDir)) return 0;

  ensureDir(tgtDir);

  const files = readdirSync(srcDir).filter(f => f.endsWith('.md'));
  let count = 0;

  for (const file of files) {
    const content = readFileSync(join(srcDir, file), 'utf8');
    writeFileSync(join(tgtDir, file), content, 'utf8');
    count++;
  }

  return count;
}

console.log(`Syncing memory from ${sourceDir} to ${targetDir}`);

ensureDir(targetDir);

// Sync plans
let count = syncFiles('plans');
console.log(`  Synced ${count} plans`);

// Sync facts
count = syncFiles('facts');
console.log(`  Synced ${count} facts`);

// Sync rules
count = syncFiles('rules');
console.log(`  Synced ${count} rules`);

// Copy MEMORY.md
const srcMemory = join(sourceDir, 'MEMORY.md');
const tgtMemory = join(targetDir, 'MEMORY.md');
if (existsSync(srcMemory)) {
  writeFileSync(tgtMemory, readFileSync(srcMemory, 'utf8'), 'utf8');
  console.log('  Synced MEMORY.md');
}

console.log('Memory sync complete.');
