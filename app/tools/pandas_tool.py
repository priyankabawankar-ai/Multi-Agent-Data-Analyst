import pandas as pd

def analyze_data(df, operation: str):
    try:
        if operation == "mean":
            return df.mean(numeric_only=True).to_dict()
        elif operation == "sum":
            return df.sum(numeric_only=True).to_dict()
        elif operation == "describe":
            return df.describe().to_dict()
        else:
            return "Unsupported operation"
    except Exception as e:
        return str(e)