"""Tests for the DataProcessor class."""

import tempfile
from pathlib import Path

import pandas as pd
import pytest

from data_processor import DataProcessor


@pytest.fixture
def sample_csv(tmp_path: Path) -> Path:
    """Create a sample CSV file for testing."""
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie", "Alice"],
        "age": [25, 30, None, 25],
        "city": ["NYC", "LA", "Chicago", "NYC"],
    })
    path = tmp_path / "sample.csv"
    df.to_csv(path, index=False)
    return path


@pytest.fixture
def sample_excel(tmp_path: Path) -> Path:
    """Create a sample Excel file for testing."""
    df = pd.DataFrame({
        "product": ["Apple", "Banana", "Cherry"],
        "price": [1.50, 0.75, 2.00],
        "quantity": [100, 150, 75],
    })
    path = tmp_path / "sample.xlsx"
    df.to_excel(path, index=False)
    return path


class TestDataProcessor:
    """Tests for DataProcessor class."""

    def test_load_csv(self, sample_csv: Path):
        """Test loading a CSV file."""
        processor = DataProcessor(sample_csv).load()
        assert len(processor.data) == 4
        assert list(processor.data.columns) == ["name", "age", "city"]

    def test_load_excel(self, sample_excel: Path):
        """Test loading an Excel file."""
        processor = DataProcessor(sample_excel).load()
        assert len(processor.data) == 3
        assert list(processor.data.columns) == ["product", "price", "quantity"]

    def test_load_unsupported_format(self, tmp_path: Path):
        """Test loading an unsupported file format."""
        path = tmp_path / "data.json"
        path.write_text("{}")
        processor = DataProcessor(path)
        with pytest.raises(ValueError, match="Unsupported file format"):
            processor.load()

    def test_data_not_loaded(self, sample_csv: Path):
        """Test accessing data before loading."""
        processor = DataProcessor(sample_csv)
        with pytest.raises(RuntimeError, match="Data not loaded"):
            _ = processor.data

    def test_select_columns(self, sample_csv: Path):
        """Test selecting specific columns."""
        processor = DataProcessor(sample_csv).load()
        processor.select_columns(["name", "city"])
        assert list(processor.data.columns) == ["name", "city"]

    def test_drop_columns(self, sample_csv: Path):
        """Test dropping columns."""
        processor = DataProcessor(sample_csv).load()
        processor.drop_columns(["age"])
        assert "age" not in processor.data.columns

    def test_rename_columns(self, sample_csv: Path):
        """Test renaming columns."""
        processor = DataProcessor(sample_csv).load()
        processor.rename_columns({"name": "full_name"})
        assert "full_name" in processor.data.columns
        assert "name" not in processor.data.columns

    def test_drop_duplicates(self, sample_csv: Path):
        """Test removing duplicate rows."""
        processor = DataProcessor(sample_csv).load()
        initial_rows = len(processor.data)
        processor.drop_duplicates(subset=["name", "city"])
        assert len(processor.data) < initial_rows

    def test_drop_na(self, sample_csv: Path):
        """Test removing rows with missing values."""
        processor = DataProcessor(sample_csv).load()
        processor.drop_na()
        assert len(processor.data) == 3  # One row had None

    def test_fill_na(self, sample_csv: Path):
        """Test filling missing values."""
        processor = DataProcessor(sample_csv).load()
        processor.fill_na(0)
        assert processor.data["age"].isnull().sum() == 0

    def test_sort_by(self, sample_csv: Path):
        """Test sorting data."""
        processor = DataProcessor(sample_csv).load()
        processor.drop_na().sort_by(["age"], ascending=False)
        ages = processor.data["age"].tolist()
        assert ages == sorted(ages, reverse=True)

    def test_filter_rows(self, sample_csv: Path):
        """Test filtering rows."""
        processor = DataProcessor(sample_csv).load()
        processor.filter_rows(lambda df: df["city"] == "NYC")
        assert len(processor.data) == 2
        assert all(processor.data["city"] == "NYC")

    def test_apply_transform(self, sample_csv: Path):
        """Test applying a transformation."""
        processor = DataProcessor(sample_csv).load()
        processor.apply_transform("name", str.upper)
        assert processor.data["name"].iloc[0] == "ALICE"

    def test_save_csv(self, sample_csv: Path, tmp_path: Path):
        """Test saving to CSV."""
        output = tmp_path / "output.csv"
        processor = DataProcessor(sample_csv).load()
        processor.save(output)
        assert output.exists()
        loaded = pd.read_csv(output)
        assert len(loaded) == 4

    def test_save_excel(self, sample_csv: Path, tmp_path: Path):
        """Test saving to Excel."""
        output = tmp_path / "output.xlsx"
        processor = DataProcessor(sample_csv).load()
        processor.save(output)
        assert output.exists()
        loaded = pd.read_excel(output)
        assert len(loaded) == 4

    def test_summary(self, sample_csv: Path):
        """Test getting data summary."""
        processor = DataProcessor(sample_csv).load()
        summary = processor.summary()
        assert summary["rows"] == 4
        assert "name" in summary["columns"]
        assert "age" in summary["missing_values"]

    def test_method_chaining(self, sample_csv: Path, tmp_path: Path):
        """Test method chaining."""
        output = tmp_path / "output.csv"
        processor = (
            DataProcessor(sample_csv)
            .load()
            .drop_na()
            .drop_duplicates(subset=["name"])
            .select_columns(["name", "city"])
            .sort_by(["name"])
        )
        processor.save(output)
        assert output.exists()
