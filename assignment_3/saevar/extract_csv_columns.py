#!/usr/bin/env python3
"""
Read the Mother Jones mass shootings CSV and report (or export) its column headers.

Usage:
  python3 extract_csv_columns.py
  python3 extract_csv_columns.py "path/to/file.csv"
  python3 extract_csv_columns.py --json
  python3 extract_csv_columns.py --output columns.txt
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

DEFAULT_CSV = Path(__file__).resolve().parent / (
    "Mother Jones - Mass Shootings Database, 1982 - 2026 - Sheet1.csv"
)


def read_header_row(path: Path) -> list[str]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        try:
            row = next(reader)
        except StopIteration:
            return []
    return row


def main() -> int:
    parser = argparse.ArgumentParser(
        description="List column names from the Mother Jones mass shootings CSV."
    )
    parser.add_argument(
        "csv_path",
        nargs="?",
        type=Path,
        default=DEFAULT_CSV,
        help=f"Path to CSV (default: {DEFAULT_CSV.name})",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print columns as a JSON array",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        metavar="FILE",
        help="Write one column name per line to this file",
    )
    args = parser.parse_args()
    path: Path = args.csv_path

    if not path.is_file():
        print(f"error: file not found: {path}", file=sys.stderr)
        return 1

    columns = read_header_row(path)
    if not columns:
        print(f"error: empty or unreadable CSV: {path}", file=sys.stderr)
        return 1

    counts = Counter(columns)
    dupes = {name: n for name, n in counts.items() if n > 1}

    if args.json:
        print(json.dumps(columns, indent=2))
    else:
        print(f"File: {path}")
        print(f"Column count: {len(columns)}")
        if dupes:
            print("Duplicate header names (appear multiple times):", dupes)
        print("Columns (index: name):")
        for i, name in enumerate(columns):
            print(f"  {i:2d}  {name}")

    if args.output:
        args.output.write_text("\n".join(columns) + "\n", encoding="utf-8")
        if not args.json:
            print(f"\nWrote {len(columns)} names to {args.output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
