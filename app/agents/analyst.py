from app.utils.llm import get_llm

def analyst_agent(state):
    llm = get_llm()
    df = state["df"]
    query = state["query"]

    if "mean" in query:
        result = df.mean(numeric_only=True).to_dict()
    elif "sum" in query:
        result = df.sum(numeric_only=True).to_dict()
    else:
        result = df.describe().to_dict()

    return {"analysis": result}