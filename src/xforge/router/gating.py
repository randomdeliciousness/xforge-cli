import json
import os
from typing import List
from dotenv import load_dotenv
from xai_sdk import Client
from xai_sdk.chat import system, user

load_dotenv()  # loads XAI_API_KEY from .env

class MoERouter:
    """
    Mixture-of-Experts Gating Network (exactly like Grok-1's router)
    
    This is the BRAIN of xForge.
    It inspects the user request + context and decides which 2-3 specialists
    (experts) should activate — sparse activation = efficient & scalable.
    
    Grok-1 connection: Grok-1 had 8 experts per layer and a router that picked top-2.
    Here we do the same at the agent level (top-2 or top-3 experts).
    """
    
    # All available experts 
    EXPERTS = [
        "planner",      # high-level strategy & plan
        "coder",        # actual code editing & implementation
        "critic",       # quality, safety, truth-checking
        "researcher",   # codebase search & memory
        "tool_executor",# git, fs, bash with approvals
        "memory_manager"# long-term context & notes
    ]
    
    def __init__(self, model: str = "grok-4"):
        self.model = model
        self.client = Client()  # official xAI SDK — auto-reads XAI_API_KEY
    
    def route(self, user_intent: str, context_summary: str = "") -> List[str]:
        """Returns ONLY the activated experts (sparse top-k gating)"""
        
        prompt = f"""You are the MoE Router for xForge CLI (inspired directly by Grok-1 gating).
        User intent: {user_intent}
        Current project context: {context_summary[:800]}
        
        Select ONLY the 2-3 most relevant experts that should activate.
        Available experts: {self.EXPERTS}
        
        Respond with ONLY valid JSON in this exact format:
        {{"experts": ["expert1", "expert2"]}}
        No explanation, no extra text."""

        # Official xAI SDK chat pattern
        chat = self.client.chat.create(model=self.model)
        chat.append(system("You are a precise MoE routing specialist. Always output clean JSON."))
        chat.append(user(prompt))
        
        response = chat.sample()
        content = response.content.strip()
        
        try:
            data = json.loads(content)
            selected = data.get("experts", ["planner", "coder"])  # fallback
            # Safety: only use real experts
            selected = [e for e in selected if e in self.EXPERTS][:3]
            print(f"🧠 MoE Router activated experts: {selected}")
            return selected
        except Exception as e:
            print(f"⚠️ Router fallback (JSON parse failed): {e}")
            return ["planner", "coder"]  # safe default
