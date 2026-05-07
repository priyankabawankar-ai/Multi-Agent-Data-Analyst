# import pandas as pd

# def schema_analyzer_agent(df: pd.DataFrame):
#     schema = []

#     for col in df.columns:
#         col_data = df[col]

#         dtype = str(col_data.dtype)

#         # detect numeric
#         is_numeric = pd.api.types.is_numeric_dtype(col_data)

#         # detect datetime
#         is_date = False
#         try:
#             pd.to_datetime(col_data.dropna().iloc[:10])
#             is_date = True
#         except:
#             pass

#         schema.append({
#             "column": col,
#             "dtype": dtype,
#             "is_numeric": is_numeric,
#             "is_date": is_date
#         })

#     return schema