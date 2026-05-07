# from langchain_openai import ChatOpenAI
# from langchain.tools import Tool
# from langchain.agents import initialize_agent, AgentType

# from app.tools.pandas_tool import analyze_data
# from app.tools.plot_tool import create_plot

# llm = ChatOpenAI(model="gpt-4o-mini")

# def create_agent(df):

#     tools = [
#         Tool(
#             name="Data Analysis Tool",
#             func=lambda x: analyze_data(df, x),
#             description="Use this to perform operations like mean, sum, describe on dataset"
#         ),
#         Tool(
#             name="Visualization Tool",
#             func=lambda x: create_plot(df),
#             description="Use this to generate plots for the dataset"
#         )
#     ]

#     agent = initialize_agent(
#         tools,
#         llm,
#         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#         verbose=True
#     )

#     return agent