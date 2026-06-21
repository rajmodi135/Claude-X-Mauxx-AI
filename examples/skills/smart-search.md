---
name: smart-search
description: "AI-powered codebase search with natural language queries"
metadata:
  type: skill
  category: development
  version: 1
---

# Smart Search

Search the codebase using natural language.

## Usage

- `smart-search "where do we handle auth errors?"`
- `smart-search "show me all rate-limiting code"`
- `smart-search "how does payment processing work?"`

## How It Works

1. Embeds your query
2. Vector search over codebase chunks
3. Returns top 5 most relevant files with excerpts
4. Ranks by semantic similarity + recency

## Powered by

- smart-memory skill
- glob/grep for fast keyword fallback