from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from ..agent.orchestrator import AgentOrchestrator
from typing import Optional

class xForgeApp(App):
    """Textual TUI for xForge CLI - beautiful interactive interface."""
    
    TITLE = "xForge CLI"
    SUB_TITLE = "xAI MoE Coding Assistant"
    
    def __init__(self, orchestrator: Optional[AgentOrchestrator] = None):
        super().__init__()
        self.orchestrator = orchestrator
        print("🖥️  xForge TUI initialized")
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Welcome to xForge CLI!\n\nType commands or tasks to get started.\nRouter and experts ready.", id="main")
        yield Footer()
    
    def on_mount(self):
        if self.orchestrator:
            print("🚀 Orchestrator connected to UI")
