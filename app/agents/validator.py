# from app.utils.llm import get_llm


# def validator_agent(state):
#     llm = get_llm()

#     query = state.get("query", "")
#     result = state.get("analysis")

#     prompt = f"""
#     Validate the result.

#     Query: {query}
#     Result: {result}

#     Answer:
#     - Is result correct? (yes/no)
#     - If no, what is wrong?

#     Keep answer short.
#     """

#     response = llm.invoke(prompt).content

#     return {
#         "validation": response
#     }