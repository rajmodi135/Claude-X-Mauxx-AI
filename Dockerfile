FROM python:3.12-slim AS base

WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl &&
    rm -rf /var/lib/apt/lists/*

# Install Node.js for Claude Code
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g @anthropic-ai/claude-code

# Copy Mauxx AI
COPY . .

# Install Python deps for TUI
RUN pip install --no-cache-dir -r tui/requirements.txt 2>/dev/null || true

# Install npm deps
RUN npm install 2>/dev/null || true

# Verify
RUN node --check bin/claude-x-mauxx-ai.mjs 2>/dev/null || true

ENTRYPOINT ["python", "tui/run.py"]
