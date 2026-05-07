from fastapi import FastAPI, UploadFile
import pandas as pd
from dotenv import load_dotenv

from app.graph.workflow import build_graph

load_dotenv()

app = FastAPI()

@app.post("/analyze")
async def analyze(file: UploadFile, query: str):

    df = pd.read_csv(file.file)

    graph = build_graph()

    result = graph.invoke({
        "query": query,
        "df": df
    })

    return {
        "plan": result.get("plan"),
        "analysis": result.get("analysis"),
        "visualization": result.get("visualization"),
        "final_answer": result.get("final_answer")
    }