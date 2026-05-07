# def router(state):
#     query = state["query"].lower()

#     if "plot" in query or "chart" in query:
#         print("ROUTER: visualizer")
#         return "visualizer"

#     elif "average" in query or "sum" in query or "total" in query:
#         print("ROUTER: analyst")
#         return "analyst"

#     else:
#         print("ROUTER: reporter")
#         return "reporter"