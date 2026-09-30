# Automatic Data Visualization Tool

**VITyarthi – Build Your Own Project | Data Visualization**

## Overview
A modular Python application that loads a dataset, analyzes its structure, automatically chooses compatible columns, and generates common visualizations. The project demonstrates data loading, preprocessing/profiling, rule-based decision logic, visualization, error handling and testing.

## Functional Modules
1. **Data Input & Validation** – loads CSV, XLSX, XLS and JSON files and rejects unsupported/empty inputs.
2. **Dataset Analysis** – identifies numeric, categorical and date-like columns and reports missing values.
3. **Visualization & Reporting** – creates bar, line, pie and scatter charts plus a dataset summary.

## Technologies
- Python 3.10+
- Pandas
- Matplotlib
- OpenPyXL / XLRD
- Pytest

## Project Structure
```text
VITyarthi_Data_Visualization_Project/
├── main.py
├── requirements.txt
├── statement.md
├── README.md
├── data/
│   └── sample_data.csv
├── src/
│   ├── __init__.py
│   ├── cli.py
│   ├── data_loader.py
│   ├── analyzer.py
│   ├── visualizer.py
│   └── reporter.py
├── tests/
│   └── test_project.py
├── docs/
│   ├── architecture.md
│   ├── workflow.md
│   ├── uml.md
│   └── report_content.md
└── outputs/
```

## Installation
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run
```bash
python main.py
```
Then enter the path to a CSV/XLSX/XLS/JSON dataset. Use the included `data/sample_data.csv` for a demo.

## Testing
```bash
pytest -q
```

## Outputs
Generated charts are saved as PNG files in `outputs/`; the dataset profile is saved as `outputs/dataset_summary.txt`.

## VITyarthi Documentation
See `statement.md` and the `docs/` folder for the problem statement, requirements, architecture, workflow, UML design, implementation notes, testing and report content.
