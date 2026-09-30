import pandas as pd

def analyze_dataset(df):
    numeric = list(df.select_dtypes(include="number").columns)

    date = []
    for column in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[column]):
            date.append(column)
        elif df[column].dtype == "object":
            converted = pd.to_datetime(df[column], errors="coerce")
            if len(df) > 0 and converted.notna().mean() >= 0.80:
                date.append(column)

    categorical = [
        c for c in df.columns
        if c not in numeric and c not in date
    ]

    missing = {
        c: int(n)
        for c, n in df.isna().sum().items()
        if n > 0
    }

    return {
        "numeric": numeric,
        "categorical": categorical,
        "date": date,
        "missing": missing
    }

def choose_columns(df, chart_type, info):
    numeric = info["numeric"]
    categorical = info["categorical"]
    dates = info["date"]

    if chart_type == "bar":
        if not numeric:
            raise ValueError("Bar chart requires a numeric column.")
        category = categorical[0] if categorical else (dates[0] if dates else None)
        if category is None:
            raise ValueError("Bar chart needs a categorical/date column.")
        return {"category": category, "value": numeric[0]}

    if chart_type == "line":
        if not numeric:
            raise ValueError("Line chart requires a numeric column.")
        x = dates[0] if dates else (categorical[0] if categorical else None)
        if x is None:
            raise ValueError("Line chart needs a date/time or categorical column.")
        return {"x": x, "value": numeric[0]}

    if chart_type == "pie":
        if not numeric or not categorical:
            raise ValueError("Pie chart needs categorical and numeric columns.")
        return {"category": categorical[0], "value": numeric[0]}

    if chart_type == "scatter":
        if len(numeric) < 2:
            raise ValueError("Scatter plot requires at least two numeric columns.")
        return {"x": numeric[0], "y": numeric[1]}

    raise ValueError("Unknown chart type.")
