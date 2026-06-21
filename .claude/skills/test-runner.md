---
name: test-runner
description: "Auto-runs tests after every code change. Reports results, suggests fixes on failure."
metadata:
  type: skill
  category: quality
  version: 1
---

# Test Runner Skill

Auto-runs tests after code changes.

## Triggers

- After every Edit/Write
- Before commit
- On /test command
- Periodic (every 30 min during active work)

## Test Frameworks Supported

| Stack | Framework | Command |
|-------|-----------|---------|
| Python | pytest | `pytest -v` |
| Python | unittest | `python -m unittest` |
| JS/TS | jest | `npm test` |
| JS/TS | vitest | `npm run test` |
| Rust | cargo test | `cargo test` |
| Go | go test | `go test ./...` |
| Java | mvn | `mvn test` |

## What It Reports

```
✓ 142 passed
✗ 3 failed
⏭ 5 skipped

Failures:
  tests/test_auth.py::test_login — AssertionError
  tests/test_user.py::test_delete — TypeError
  tests/test_api.py::test_health — ConnectionError
```

## On Failure

1. Re-reads test source
2. Identifies likely cause
3. Suggests fix
4. Retries once
5. Escalates to user if not fixable

## Commands

- `/test` — run all tests
- `/test <pattern>` — run matching tests
- `/test watch` — watch mode
- `/test coverage` — with coverage report
