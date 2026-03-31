from typing import List
from ..router.gating import MoERouter
from ..context.manager import ContextManager

class AgentOrchestrator:
    """Orchestrates multiple experts based on router decisions."""
    
    def __init__(self, router: MoERouter, context: ContextManager):
        self.router = router
        self.context = context
        self.active_experts: List[str] = []
        print("🤖 AgentOrchestrator ready with MoE routing")
    
    def process(self, task: str):
        """Route task to appropriate experts."""
        summary = self.context.get_summary()
        self.active_experts = self.router.route(task, summary)
        print(f"🎯 Activated experts: {self.active_experts}")
        return f"Processed task with {len(self.active_experts)} experts"
