# Contributing to Claude × Mauxx AI

Thanks for your interest! Here's how to contribute.

## Code of Conduct

Be kind. Be patient. We're all building something cool together.

## How to Contribute

### 1. Report a Bug
Open an issue at https://github.com/rajmodi135/Claude-X-Mauxx-AI/issues

Include:
- Steps to reproduce
- Expected behavior
- Actual behavior
- OS + Node.js + Python versions
- Logs (anonymized)

### 2. Suggest a Feature
Open a discussion at https://github.com/rajmodi135/Claude-X-Mauxx-AI/discussions

### 3. Submit a Preset Agent
Create a new file at `.claude/agents/<name>.md` with:

```yaml
---
name: your-preset
description: What this preset does
metadata:
  type: agent-preset
  version: 1
  modelTier: sonnet
  stack:
    language: [python]
    framework: [fastapi]
---
```

Then describe:
- Detected stack triggers
- Auto-configured agents
- Default workflow
- Conventions
- Pre-loaded skills

Submit a PR!

### 4. Submit a Skill
Create `.claude/skills/<name>.md`:

```yaml
---
name: your-skill
description: What this skill does
metadata:
  type: skill
  category: category-name
  version: 1
---
```

Then describe usage, integration, examples.

### 5. Improve Documentation
- Fix typos
- Add examples
- Translate to other languages

### 6. Submit a Workflow
For complex multi-step tasks, add to `.claude/workflows/`:

```javascript
// your-workflow.js
export const meta = {
  name: 'your-workflow',
  description: 'What it does',
};

phase('Phase 1');
const result = await agent('Your task description');

return { result };
```

## Development Setup

```bash
git clone https://github.com/rajmodi135/Claude-X-Mauxx-AI.git
cd Claude-X-Mauxx-AI
git checkout -b feature/your-feature

# Make changes
git add -A
git commit -m "feat: your feature description"
git push origin feature/your-feature

# Open PR
```

## Conventional Commits

We use Conventional Commits. Format:

```
<type>(<scope>): <description>

[body]
[footer]
```

Types:
- `feat` — new feature
- `fix` — bug fix
- `docs` — documentation only
- `style` — formatting, no code change
- `refactor` — code change that neither fixes a bug nor adds a feature
- `perf` — performance improvement
- `test` — add tests
- `chore` — build, dependencies, tooling
- `ci` — CI configuration

Examples:
- `feat(preset): add rust-cli preset`
- `fix(hook): handle null input in PostToolUse`
- `docs: update FAQ with troubleshooting tips`

## Testing

```bash
# Test the TUI:
cd tui && pip install -r requirements.txt && python run.py

# Test hooks:
bash scripts/batch-commits.sh

# Test memory system:
ls memory/
```

## Release Process

1. Update `VERSION_ROADMAP.md`
2. Update `CHANGELOG.md`
3. Tag: `git tag v2.x.x`
4. Push tag: `git push --tags`
5. GitHub Actions publishes to npm automatically

## Recognition

All contributors are listed in the README. Major contributors get a shoutout in the next release notes.

## Questions?

Open an issue or discussion. We're happy to help!
