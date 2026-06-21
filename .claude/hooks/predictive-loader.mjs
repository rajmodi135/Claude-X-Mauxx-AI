#!/usr/bin/env node
// UserPromptSubmit hook — predictive context loading
// Runs when user submits a prompt. Pre-fetches likely context.

import { existsSync, readFileSync } from 'fs';
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

async function main() {
  const input = await readStdin();
  if (!input) {
    console.log('{}');
    return;
  }

  let event;
  try {
    event = JSON.parse(input);
  } catch {
    console.log('{}');
    return;
  }

  const prompt = (event.prompt || '').toLowerCase();

  // Detect intent cheaply
  const isCodeTask = /\b(fix|edit|add|implement|refactor|create|write|build)\b/.test(prompt);
  const isReview = /\b(review|check|audit|verify)\b/.test(prompt);
  const isResearch = /\b(research|investigate|explore|find out|what is|how does)\b/.test(prompt);
  const isDeploy = /\b(deploy|release|publish|ship)\b/.test(prompt);

  // Output additional context to inject
  const output = {
    additionalContext: [],
    modelHint: 'sonnet',
  };

  if (isResearch) output.modelHint = 'haiku';
  if (isCodeTask) output.modelHint = 'sonnet';
  if (prompt.includes('architect') || prompt.includes('design system')) output.modelHint = 'opus';

  // Add a hint that the routing system should consider
  output.additionalContext.push(
    `💰 Model hint: ${output.modelHint} (based on prompt analysis)`
  );

  // For deploy/release tasks, suggest the deploy skill
  if (isDeploy) {
    output.additionalContext.push('🚀 Consider: scripts/deploy.sh or .github/workflows/release.yml');
  }

  console.log(JSON.stringify(output));
}

main().catch(() => {
  console.log('{}');
});
