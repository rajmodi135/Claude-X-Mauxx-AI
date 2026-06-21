# /review — Code Review
# Invoke: /review [path]

Run AI code review on a file, directory, or PR.

## Usage

```
/review               — review pending changes
/review src/auth.py   — review specific file
/review src/          — review directory
/review PR 123        — review a PR
/review --security    — security-focused
/review --perf        — performance-focused
```

## What It Checks

- Bugs and edge cases
- Security issues (OWASP)
- Performance bottlenecks
- Code style
- Best practices
- Test coverage
- Documentation
