import matplotlib.pyplot as plt
import pandas as pd

def create_visualization(df, chart_type, selected):
    if chart_type == "bar":
        data = df[[selected["category"], selected["value"]]].dropna()
        grouped = data.groupby(selected["category"])[selected["value"]].mean()
        grouped = grouped.sort_values(ascending=False).head(20)

        plt.figure(figsize=(10, 6))
        grouped.plot(kind="bar")
        plt.title(f"{selected['value']} by {selected['category']}")
        plt.xlabel(selected["category"])
        plt.ylabel(selected["value"])
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

    elif chart_type == "line":
        data = df[[selected["x"], selected["value"]]].dropna()
        converted = pd.to_datetime(data[selected["x"]], errors="coerce")
        if converted.notna().all():
            data = data.copy()
            data[selected["x"]] = converted
            data = data.sort_values(selected["x"])

        plt.figure(figsize=(10, 6))
        plt.plot(data[selected["x"]], data[selected["value"]], marker="o")
        plt.title(f"{selected['value']} over {selected['x']}")
        plt.xlabel(selected["x"])
        plt.ylabel(selected["value"])
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

    elif chart_type == "pie":
        data = df[[selected["category"], selected["value"]]].dropna()
        grouped = data.groupby(selected["category"])[selected["value"]].sum()
        grouped = grouped.sort_values(ascending=False).head(10)

        plt.figure(figsize=(8, 8))
        plt.pie(grouped.values, labels=grouped.index, autopct="%1.1f%%", startangle=90)
        plt.title(f"{selected['value']} distribution by {selected['category']}")
        plt.tight_layout()
        plt.show()

    elif chart_type == "scatter":
        data = df[[selected["x"], selected["y"]]].dropna()

        plt.figure(figsize=(10, 6))
        plt.scatter(data[selected["x"]], data[selected["y"]])
        plt.title(f"{selected['y']} vs {selected['x']}")
        plt.xlabel(selected["x"])
        plt.ylabel(selected["y"])
        plt.tight_layout()
        plt.show()
