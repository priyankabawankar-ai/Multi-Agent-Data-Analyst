from langchain_openai import ChatOpenAI
from app.utils.llm import get_llm

llm = ChatOpenAI(model="gpt-4o-mini")

def reporter_agent(state):
    llm=get_llm()
    analysis = state.get("analysis", "")
    plan = state.get("plan", "")

    response = llm.invoke(f"""
    Plan:
    {plan}

    Analysis:
    {analysis}

    Generate final business insights.
    """)

    return {"final_answer": response.content}