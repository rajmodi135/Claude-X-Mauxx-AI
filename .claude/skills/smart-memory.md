---
name: smart-memory
description: "Vector search over past plans, facts, and decisions. Returns only relevant context for the current task — keeps conversation small."
metadata:
  type: skill
  category: memory
  version: 1
  costImpact: medium
---

# Smart Memory Skill

**Auto-loaded on session start.** Semantic search over the memory directory.

## What It Does

1. **Embeds** every plan/fact/decision when created
2. **Searches** semantically (not just keyword) when context is needed
3. **Returns** top-K relevant items (~5 by default)
4. **Caches** frequently-accessed embeddings
5. **Prunes** old/stale memories automatically

## Storage

Uses `sqlite-vec` (embedded, $0 cost) at `memory/vectors.db`:

```sql
CREATE VIRTUAL TABLE vectors USING vec0(
  id TEXT PRIMARY KEY,
  embedding FLOAT[1536],
  text TEXT,
  type TEXT,    -- 'plan' | 'fact' | 'rule' | 'state'
  source TEXT,  -- file path
  created_at TIMESTAMP
);
```

## API

```python
# Embed and store
smart_memory.embed_and_store(
    text="Fixed auth rate-limit bug. Issue: 100 req/sec too aggressive. Fix: 10 req/sec per IP.",
    type="fact",
    source="fact-auth-rate-limit.md"
)

# Semantic search
results = smart_memory.search(
    query="how to fix rate limiting bug?",
    k=5,
    filter={"type": "fact"}
)
# Returns: top 5 semantically similar memories
```

## When It Fires

- **On session start:** Index any new memory files
- **Before each plan step:** Search for related past work
- **On error:** Search for "how did I fix this before?"
- **On new task:** Search for "have I done this before?"

## Integration with Existing Memory

- Uses the `memory/` directory as source of truth
- Indexes plan-*.md, fact-*.md, archive-*.md, rule-*.md
- Skips: state-*.md (transient), session-*.md (transient)

## Example

```python
# Current task: "Add rate limiting to /api/login"
results = smart_memory.search("rate limiting API login", k=3)
# Returns:
# 1. fact-auth-rate-limit-bug.md (85% match)
#    → "Reduced to 10 req/sec per IP"
# 2. plan-rate-limiter-setup.md (72% match)
#    → "Use slowapi library"
# 3. archive-2026-05-rate-limit.md (68% match)
#    → "Implemented with Redis backend"

# Saves 2-3 turns of asking "how did I do this before?"
```

## Performance

- Indexing: ~50ms per file
- Search: ~10ms for 10K memories
- Storage: ~2KB per memory
- Total for 1000 memories: ~2MB

## Fallback

If sqlite-vec not installed, gracefully degrades to keyword search using Grep. No functionality lost, just less smart.

---

🧠 **Result: Smarter context, fewer redundant questions.**
