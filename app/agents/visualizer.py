import matplotlib.pyplot as plt
from app.utils.llm import get_llm

def visualizer_agent(state):
    llm=get_llm()
    df = state["df"]

    df.plot()
    plt.savefig("output.png")

    return {"visualization": "output.png"}