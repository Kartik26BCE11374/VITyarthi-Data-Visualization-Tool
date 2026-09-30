from pathlib import Path
from data_loader import load_data
from analyzer import analyze_dataset, choose_columns
from visualizer import create_visualization

def main():
    print("=" * 60)
    print("        AUTOMATIC DATA VISUALIZATION TOOL")
    print("=" * 60)

    while True:
        file_path = input("\nEnter the complete file location: ").strip().strip('"')

        if not Path(file_path).is_file():
            print("ERROR: File not found.")
            continue

        try:
            df = load_data(file_path)
        except Exception as e:
            print(f"ERROR: Could not read the file: {e}")
            continue

        print(f"\nFile loaded successfully. Rows: {len(df)} | Columns: {len(df.columns)}")
        print("\nAvailable columns:")
        for i, column in enumerate(df.columns, 1):
            print(f"  {i}. {column}")

        info = analyze_dataset(df)

        print("\nChoose a visualization:")
        print("1. Bar Chart")
        print("2. Line Chart")
        print("3. Pie Chart")
        print("4. Scatter Plot")
        print("5. Dataset Information")
        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "0":
            break

        if choice == "5":
            print("\nNumeric:", info["numeric"])
            print("Categorical:", info["categorical"])
            print("Date:", info["date"])
            print("Missing values:", info["missing"])
            continue

        chart_types = {"1": "bar", "2": "line", "3": "pie", "4": "scatter"}

        if choice not in chart_types:
            print("Invalid choice.")
            continue

        try:
            chart_type = chart_types[choice]
            selected = choose_columns(df, chart_type, info)

            print("\nAutomatically selected columns:")
            for role, column in selected.items():
                print(f"  {role}: {column}")

            create_visualization(df, chart_type, selected)

        except ValueError as e:
            print(f"\nCannot create visualization: {e}")
        except Exception as e:
            print(f"\nUnexpected error: {e}")

        again = input("\nCreate another visualization? (y/n): ").strip().lower()
        if again != "y":
            break

    print("Program closed.")

if __name__ == "__main__":
    main()
