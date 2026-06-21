# /test — Run Tests
# Invoke: /test [pattern]

Run project tests.

## Usage

```
/test                 — run all tests
/test auth            — run tests matching "auth"
/test --watch         — watch mode
/test --coverage      — with coverage
/test --fix           — auto-fix on failure
```

## What It Does

1. Detects test framework (pytest, jest, vitest, etc.)
2. Runs tests
3. Reports results
4. On failure: parses error, suggests fix
5. Retries if /test --fix
