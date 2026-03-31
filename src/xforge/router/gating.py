from typing import List
import json
from xai_sdk import Client
from xai_sdk.chat import system, user

class MoERouter:
    """Mixture-of-Experts Gating Network (top-k sparse activation)
    Exactly like Grok-1's router: inspects task + context, activates only 2-3 experts.
    Change the gating prompt or add experts here → instantly updates the whole system.
    """
    EXPERTS = ["planner", "coder", "critic", "researcher", "tool_executor", "memory_manager"]
    
    def __init__(self, model: str = "grok-4"):
        try:
            self.client = Client()
            self.model = model
            self.has_api = True
        except Exception:
            self.has_api = False
            print("⚠️  No XAI_API_KEY set, using mock router")
            self.model = model
    
    def route(self, user_intent: str, context_summary: str) -> List[str]:
        """Returns only the activated experts (sparse = efficient)"""
        if not self.has_api:
            # Mock for demo without API key
            selected = ["planner", "coder"]
            print(f"🧠 Router activated (mock): {selected}")
            return selected
        
        # In production we'd use embeddings; here use LLM call
        prompt = f"""You are the MoE Router for xForge (inspired by Grok-1).
Task: {user_intent}
Context: {context_summary[:500]}
Select ONLY the top 2-3 experts that should activate (top-k gating). 
Return ONLY valid JSON like: {{"experts": ["planner", "coder"]}}"""
        
        try:
            chat = self.client.chat.create(
                model=self.model,
                messages=[
                    system("You are a precise JSON-only router."),
                    user(prompt)
                ],
            )
            response = chat.sample()
            content = response.content
            # Parse JSON if possible
            try:
                if isinstance(content, str):
                    parsed = json.loads(content)
                    selected = parsed.get("experts", ["planner", "coder"])
                else:
                    selected = ["planner", "coder"]
            except:
                selected = ["planner", "coder"]
            print(f"🧠 Router activated: {selected}")
            return selected
        except Exception as e:
            print(f"⚠️ Router error: {e}, using default")
            return ["planner", "coder"]
