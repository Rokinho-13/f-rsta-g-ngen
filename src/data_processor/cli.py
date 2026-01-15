"""Command-line interface for the data processor."""

import argparse
import sys
from pathlib import Path

from data_processor import DataProcessor


def main() -> int:
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Process CSV and Excel files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "input",
        type=Path,
        help="Input file path (CSV or Excel)",
    )

    parser.add_argument(
        "-o", "--output",
        type=Path,
        help="Output file path (default: processed_<input>)",
    )

    parser.add_argument(
        "--select",
        type=str,
        nargs="+",
        metavar="COLUMN",
        help="Select specific columns",
    )

    parser.add_argument(
        "--drop",
        type=str,
        nargs="+",
        metavar="COLUMN",
        help="Drop specific columns",
    )

    parser.add_argument(
        "--drop-duplicates",
        action="store_true",
        help="Remove duplicate rows",
    )

    parser.add_argument(
        "--drop-na",
        action="store_true",
        help="Remove rows with missing values",
    )

    parser.add_argument(
        "--sort-by",
        type=str,
        nargs="+",
        metavar="COLUMN",
        help="Sort by columns",
    )

    parser.add_argument(
        "--descending",
        action="store_true",
        help="Sort in descending order (use with --sort-by)",
    )

    parser.add_argument(
        "--summary",
        action="store_true",
        help="Print data summary and exit",
    )

    args = parser.parse_args()

    if not args.input.exists():
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        return 1

    try:
        processor = DataProcessor(args.input).load()

        if args.summary:
            summary = processor.summary()
            print(f"Rows: {summary['rows']}")
            print(f"Columns: {', '.join(summary['columns'])}")
            print("\nData types:")
            for col, dtype in summary["dtypes"].items():
                print(f"  {col}: {dtype}")
            print("\nMissing values:")
            for col, count in summary["missing_values"].items():
                if count > 0:
                    print(f"  {col}: {count}")
            return 0

        if args.select:
            processor.select_columns(args.select)

        if args.drop:
            processor.drop_columns(args.drop)

        if args.drop_duplicates:
            processor.drop_duplicates()

        if args.drop_na:
            processor.drop_na()

        if args.sort_by:
            processor.sort_by(args.sort_by, ascending=not args.descending)

        output_path = args.output
        if output_path is None:
            output_path = args.input.parent / f"processed_{args.input.name}"

        processor.save(output_path)
        print(f"Processed data saved to: {output_path}")

        return 0

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
