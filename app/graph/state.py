from typing import TypedDict, Any

class AgentState(TypedDict):
    query: str
    df: Any
    plan: str
    analysis: Any
    visualization: str
    final_answer: str