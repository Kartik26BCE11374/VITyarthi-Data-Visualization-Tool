# Automatic Data Visualization Tool

A Python project that loads a user-selected data file, analyzes its columns, automatically selects suitable headers, and creates a requested visualization.

## Supported files
CSV, XLSX, XLS, JSON

## Visualizations
1. Bar chart
2. Line chart
3. Pie chart
4. Scatter plot

## Install

Windows Command Prompt:

    python -m pip install -r requirements.txt

If `python` is not recognized:

    py -m pip install -r requirements.txt

## Run

    python main.py

or:

    py main.py

## Test

Use the included `sample_data.csv`.

This version uses rule-based automatic column selection. It is intentionally simple so that the logic can be understood and extended later.
