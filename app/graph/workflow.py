from langgraph.graph import StateGraph,END
from app.graph.state import AgentState

from app.agents.planner import planner_agent
from app.agents.analyst import analyst_agent
from app.agents.visualizer import visualizer_agent
from app.agents.reporter import reporter_agent


def build_graph():

    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_agent)
    graph.add_node("analyst", analyst_agent)
    graph.add_node("visualizer", visualizer_agent)
    graph.add_node("reporter", reporter_agent)

    graph.set_entry_point("planner")

    graph.add_edge("planner", "analyst")
    graph.add_edge("analyst", "visualizer")
    graph.add_edge("visualizer", "reporter")
    graph.add_edge("reporter", END)

    return graph.compile()