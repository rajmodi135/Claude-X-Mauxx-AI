---
name: schema-validator
description: "Validates JSON Schema, OpenAPI specs, GraphQL schemas, Prisma schemas, SQL DDL"
metadata:
  type: skill
  category: quality
  version: 1
---

# Schema Validator

Validates all kinds of schemas.

## Supported Schemas

| Type | Tool |
|------|------|
| JSON Schema | ajv |
| OpenAPI 3.0/3.1 | swagger-parser |
| GraphQL | graphql-js |
| Prisma | prisma validate |
| SQL DDL | sqlfluff |
| Protobuf | protoc |
| Avro | avro-tools |

## What It Detects

- Missing required fields
- Type mismatches
- Broken references
- Deprecated patterns
- Inconsistent naming
- Security issues (PII exposure)

## Usage

- `schema-validate <file>` — single file
- `schema-validate <dir>` — all schemas
- `schema-validate --strict` — warnings as errors
- `schema-validate --fix` — auto-fix where possible
