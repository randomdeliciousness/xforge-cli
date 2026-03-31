from pathlib import Path
from typing import Dict, Any

class ContextManager:
    """Manages project context, code analysis, and embeddings for routing."""
    
    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.context_summary = "No context loaded yet."
        print(f"📁 ContextManager initialized for: {self.project_path}")
    
    def get_summary(self) -> str:
        """Return a summary of the current project context."""
        return self.context_summary
    
    def update_context(self, new_info: str):
        self.context_summary = new_info[:1000]
        print(f"🔄 Context updated: {len(new_info)} chars")
