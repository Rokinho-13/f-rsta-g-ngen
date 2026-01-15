"""Core data processing functionality."""

from pathlib import Path
from typing import Callable

import pandas as pd


class DataProcessor:
    """Process CSV and Excel files with various transformations."""

    def __init__(self, file_path: str | Path):
        """Initialize the processor with a file path.

        Args:
            file_path: Path to a CSV or Excel file.
        """
        self.file_path = Path(file_path)
        self._df: pd.DataFrame | None = None

    def load(self) -> "DataProcessor":
        """Load data from the file.

        Returns:
            Self for method chaining.

        Raises:
            ValueError: If file format is not supported.
        """
        suffix = self.file_path.suffix.lower()

        if suffix == ".csv":
            self._df = pd.read_csv(self.file_path)
        elif suffix in (".xlsx", ".xls"):
            self._df = pd.read_excel(self.file_path)
        else:
            raise ValueError(f"Unsupported file format: {suffix}")

        return self

    @property
    def data(self) -> pd.DataFrame:
        """Get the loaded DataFrame.

        Raises:
            RuntimeError: If data has not been loaded yet.
        """
        if self._df is None:
            raise RuntimeError("Data not loaded. Call load() first.")
        return self._df

    def filter_rows(self, condition: Callable[[pd.DataFrame], pd.Series]) -> "DataProcessor":
        """Filter rows based on a condition.

        Args:
            condition: A function that takes a DataFrame and returns a boolean Series.

        Returns:
            Self for method chaining.
        """
        self._df = self.data[condition(self.data)]
        return self

    def select_columns(self, columns: list[str]) -> "DataProcessor":
        """Select specific columns.

        Args:
            columns: List of column names to keep.

        Returns:
            Self for method chaining.
        """
        self._df = self.data[columns]
        return self

    def drop_columns(self, columns: list[str]) -> "DataProcessor":
        """Drop specific columns.

        Args:
            columns: List of column names to drop.

        Returns:
            Self for method chaining.
        """
        self._df = self.data.drop(columns=columns)
        return self

    def rename_columns(self, mapping: dict[str, str]) -> "DataProcessor":
        """Rename columns.

        Args:
            mapping: Dictionary mapping old names to new names.

        Returns:
            Self for method chaining.
        """
        self._df = self.data.rename(columns=mapping)
        return self

    def drop_duplicates(self, subset: list[str] | None = None) -> "DataProcessor":
        """Remove duplicate rows.

        Args:
            subset: Column names to consider for identifying duplicates.

        Returns:
            Self for method chaining.
        """
        self._df = self.data.drop_duplicates(subset=subset)
        return self

    def drop_na(self, subset: list[str] | None = None) -> "DataProcessor":
        """Remove rows with missing values.

        Args:
            subset: Column names to consider for identifying missing values.

        Returns:
            Self for method chaining.
        """
        self._df = self.data.dropna(subset=subset)
        return self

    def fill_na(self, value: any) -> "DataProcessor":
        """Fill missing values.

        Args:
            value: Value to use for filling missing values.

        Returns:
            Self for method chaining.
        """
        self._df = self.data.fillna(value)
        return self

    def sort_by(self, columns: list[str], ascending: bool = True) -> "DataProcessor":
        """Sort data by columns.

        Args:
            columns: Column names to sort by.
            ascending: Sort order.

        Returns:
            Self for method chaining.
        """
        self._df = self.data.sort_values(by=columns, ascending=ascending)
        return self

    def apply_transform(self, column: str, func: Callable) -> "DataProcessor":
        """Apply a transformation function to a column.

        Args:
            column: Column name to transform.
            func: Function to apply to each value.

        Returns:
            Self for method chaining.
        """
        self._df[column] = self.data[column].apply(func)
        return self

    def save(self, output_path: str | Path, index: bool = False) -> Path:
        """Save the processed data to a file.

        Args:
            output_path: Path for the output file.
            index: Whether to include the index in the output.

        Returns:
            Path to the saved file.

        Raises:
            ValueError: If output format is not supported.
        """
        output_path = Path(output_path)
        suffix = output_path.suffix.lower()

        if suffix == ".csv":
            self.data.to_csv(output_path, index=index)
        elif suffix in (".xlsx", ".xls"):
            self.data.to_excel(output_path, index=index)
        else:
            raise ValueError(f"Unsupported output format: {suffix}")

        return output_path

    def summary(self) -> dict:
        """Get a summary of the current data.

        Returns:
            Dictionary with data summary information.
        """
        return {
            "rows": len(self.data),
            "columns": list(self.data.columns),
            "dtypes": self.data.dtypes.to_dict(),
            "missing_values": self.data.isnull().sum().to_dict(),
        }
