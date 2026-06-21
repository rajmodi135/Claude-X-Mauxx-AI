# Claude x Mauxx AI — Example Presets

Copy these presets into your project's `.claude/agents/` directory to extend Mauxx AI.

Each preset auto-configures agents, workflow, and conventions for a specific project type.

## Available Presets

| Preset | File | Use For |
|--------|------|---------|
| Webapp Fullstack | `webapp-fullstack.md` | React + FastAPI + DB |
| API Microservice | `api-microservice.md` | Docker + K8s + REST |
| Mobile App | `mobile-app.md` | React Native + iOS/Android |
| Data Pipeline | `data-pipeline.md` | Airflow + dbt + Spark |
| CLI Tool | `cli-tool.md` | Python/Node/Rust CLI |
| Docs Site | `docs-site.md` | Docusaurus + MDX |
| Security Audit | `security-audit.md` | SAST + DAST + Compliance |
| Perf Tuning | `perf-tuning.md` | Profiling + Benchmarks |
| ML Training | `ml-training.md` | PyTorch + W&B + HF |
| Blockchain | `blockchain.md` | Solidity + Hardhat |

## How to Use

```bash
# Link a preset from the main repo
ln -s /path/to/Claude-x-Mauxx-AI/.claude/agents/webapp-fullstack.md .claude/agents/

# Or copy it
cp /path/to/Claude-x-Mauxx-AI/.claude/agents/webapp-fullstack.md .claude/agents/

# Then in CLAUDE.md:
echo "preset: webapp-fullstack" >> CLAUDE.md
```

## Creating a Custom Preset

See `PLUGIN_SDK.md` in the project root.
