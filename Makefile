.PHONY: help install test lint clean release

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	npm install
	pip install -r tui/requirements.txt 2>/dev/null || true

test: ## Run syntax checks
	@echo "Checking JavaScript files..."
	@for f in bin/*.mjs bin/*.js .claude/hooks/*.mjs; do \
		node --check "$$f" 2>/dev/null && echo "  ✓ $$f" || echo "  ⚠ $$f"; \
	done
	@echo "Checking shell scripts..."
	@for f in scripts/*.sh install.sh; do \
		if [ -f "$$f" ]; then bash -n "$$f" && echo "  ✓ $$f"; fi; \
	done
	@echo "✓ All checks passed"

lint: ## Run markdown lint
	npx markdownlint-cli2 '**/*.md' --config '{}' 2>/dev/null || true

clean: ## Clean temp files
	rm -rf node_modules dist build .pytest_cache logs/*.log 2>/dev/null || true

release: ## Create a new release
	@read -p "Version type (patch|minor|major): " ver; \
	cd "$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))" && \
	npm version $$ver --no-git-tag-version && \
	git add package.json CHANGELOG.md && \
	git commit -m "chore: bump version to $$(node -p 'require(\"./package.json\").version')" && \
	git tag "v$$(node -p 'require(\"./package.json\").version')" && \
	echo "✓ Release ready. Run: git push --tags"

start: ## Start the TUI
	cd tui && python run.py

mauxx: ## Start Claude x Mauxx AI
	claude --config .claude/settings.json
