# def convert_numpy(obj):
#     import numpy as np
#     import pandas as pd

#     # Handle dict
#     if isinstance(obj, dict):
#         return {k: convert_numpy(v) for k, v in obj.items()}

#     # Handle list
#     elif isinstance(obj, list):
#         return [convert_numpy(i) for i in obj]

#     # 🔥 Handle pandas DataFrame
#     elif isinstance(obj, pd.DataFrame):
#         return obj.to_dict(orient="records")

#     # 🔥 Handle pandas Series
#     elif isinstance(obj, pd.Series):
#         return obj.to_dict()

#     # Handle numpy types
#     elif isinstance(obj, np.integer):
#         return int(obj)

#     elif isinstance(obj, np.floating):
#         return float(obj)

#     elif hasattr(obj, "item"):
#         return obj.item()

#     return obj