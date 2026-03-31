# xForge CLI

xAI-inspired Mixture-of-Experts (MoE) coding assistant CLI. Built with Grok routing, Textual TUI, and agentic experts.

## Features
- **MoE Router**: Sparse expert activation (like Grok-1)
- **Textual TUI**: Beautiful terminal UI
- **Modular Experts**: Planner, Coder, Critic, Researcher, etc.
- **Project Context**: Smart code understanding with tree-sitter

## Quick Start

```bash
cd xforge-cli
python -m pip install -e .
python -m xforge.main start
```

Set `XAI_API_KEY` in `.env` for full LLM routing.

## Project Structure
- `src/xforge/router/`: Gating and MoE logic (edit here to change experts)
- `src/xforge/experts/`: Individual expert implementations
- `src/xforge/ui/`: Textual-based interface
- `src/xforge/context/`: Project analysis & embeddings

## Development
```bash
# Install dev deps
pip install -e ".[dev]"
ruff check .
```

Built as foundational Grok coding app.
