# from langchain_openai import ChatOpenAI

# llm = ChatOpenAI(model="gpt-4o-mini")

# def map_columns(df):

#     columns = list(df.columns)

#     prompt = f"""
# Map dataset columns to business meaning.

# Columns:
# {columns}

# Return JSON like:
# {{
#   "revenue": "Revenue Column",
#   "date": "Date Column",
#   "units": "Units Column"
# }}
# Only return JSON.
# """

#     res = llm.invoke(prompt).content

#     try:
#         import json
#         return json.loads(res)
#     except:
#         return {"raw_columns": columns}