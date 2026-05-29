#!/usr/bin/env python3
"""Convert CSV data to JSON file.

Provides `convert_csv_to_json` which reads a CSV file and writes
the data as a JSON array to `data.json`.
"""
import csv
import json
from typing import Any


def convert_csv_to_json(csv_filename: str) -> bool:
    """Read `csv_filename` and write the rows as JSON to `data.json`.

    Returns True on success, False on error (e.g., file not found).
    """
    try:
        with open(csv_filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)

        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(rows, jsonfile, indent=4)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
