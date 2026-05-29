#!/usr/bin/env python3
"""Basic serialization utilities.

Provides functions to serialize a Python dictionary to a JSON
file and to load/deserialize it back to a Python dictionary.
"""
import json
from typing import Any, Dict


def serialize_and_save_to_file(data: Dict[str, Any], filename: str) -> None:
    """Serialize `data` to JSON and write it to `filename`.

    If the file exists it will be replaced.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename: str) -> Dict[str, Any]:
    """Load JSON from `filename` and return as a Python dictionary."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
