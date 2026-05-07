from langchain_openai import ChatOpenAI
from app.utils.llm import get_llm

llm = ChatOpenAI(model="gpt-4o-mini")

def planner_agent(state):
    llm=get_llm()
    query = state["query"]

    plan = llm.invoke(f"""
    Break this task into steps for a data analyst:
    {query}
    """)

    return {"plan": plan.content}