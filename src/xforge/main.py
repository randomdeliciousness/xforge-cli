import typer
from dotenv import load_dotenv
from .router.gating import MoERouter
from .context.manager import ContextManager
from .agent.orchestrator import AgentOrchestrator
from .ui.app import xForgeApp

app = typer.Typer(help="xForge CLI - MoE-inspired agentic coding assistant")

@app.command()
def start(
    project_path: str = typer.Option(".", help="Project root"),
    model: str = typer.Option("grok-4", help="Grok model"),
):
    """Start the xForge CLI with MoE routing."""
    load_dotenv()
    print("🚀 Initializing xForge CLI (xAI-style MoE routing)...")
    
    context = ContextManager(project_path)
    router = MoERouter(model=model)  # ← change routing logic here = affects all experts
    orchestrator = AgentOrchestrator(router, context)
    
    ui_app = xForgeApp(orchestrator)
    # For demo, run a test process 
    print("🧪 Running demo task with router...")
    try:
        result = orchestrator.process("Implement a new feature for the coding assistant")
        print(f"✅ Demo complete: {result}")
    except Exception as e:
        print(f"⚠️  Demo error (likely missing XAI_API_KEY): {e}")
    
    print("\n💡 Foundation complete! Run with: python -m xforge.main start")
    print("To use full TUI: set XAI_API_KEY and uncomment ui_app.run() in main.py")
    # ui_app.run()  # Beautiful Textual TUI - run when ready


if __name__ == "__main__":
    app()
