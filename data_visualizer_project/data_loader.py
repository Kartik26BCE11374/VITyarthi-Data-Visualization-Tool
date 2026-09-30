from pathlib import Path
import pandas as pd

def load_data(file_path):
    extension = Path(file_path).suffix.lower()

    if extension == ".csv":
        return pd.read_csv(file_path)
    elif extension in (".xlsx", ".xls"):
        return pd.read_excel(file_path)
    elif extension == ".json":
        return pd.read_json(file_path)

    raise ValueError("Unsupported file type. Use CSV, XLSX, XLS or JSON.")
