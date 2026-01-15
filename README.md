# f-rsta-g-ngen

A Python data processing tool for CSV and Excel files.

## Features

- Load and process CSV and Excel files
- Filter, select, and transform columns
- Remove duplicates and handle missing values
- Sort and rename data
- Export to CSV or Excel format
- Method chaining for clean, readable code
- Command-line interface for quick processing

## Installation

```bash
pip install -e .
```

For development dependencies:

```bash
pip install -e ".[dev]"
```

## Usage

### As a Library

```python
from data_processor import DataProcessor

# Load and process data with method chaining
processor = (
    DataProcessor("data.csv")
    .load()
    .drop_na()
    .drop_duplicates()
    .select_columns(["name", "age", "city"])
    .filter_rows(lambda df: df["age"] > 25)
    .sort_by(["name"])
)

# Save the processed data
processor.save("output.csv")

# Get a summary of the data
print(processor.summary())
```

### Command-Line Interface

```bash
# View data summary
data-processor input.csv --summary

# Select specific columns
data-processor input.csv --select name age city -o output.csv

# Drop columns and remove duplicates
data-processor input.xlsx --drop id timestamp --drop-duplicates -o clean.xlsx

# Remove missing values and sort
data-processor data.csv --drop-na --sort-by name --descending -o sorted.csv
```

## API Reference

### DataProcessor

| Method | Description |
|--------|-------------|
| `load()` | Load data from file |
| `filter_rows(condition)` | Filter rows using a condition function |
| `select_columns(columns)` | Keep only specified columns |
| `drop_columns(columns)` | Remove specified columns |
| `rename_columns(mapping)` | Rename columns using a dictionary |
| `drop_duplicates(subset)` | Remove duplicate rows |
| `drop_na(subset)` | Remove rows with missing values |
| `fill_na(value)` | Fill missing values |
| `sort_by(columns, ascending)` | Sort data by columns |
| `apply_transform(column, func)` | Apply function to a column |
| `save(path)` | Save data to file |
| `summary()` | Get data summary |

## Running Tests

```bash
pytest
```

## License

MIT