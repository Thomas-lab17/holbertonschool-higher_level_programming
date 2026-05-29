#!/usr/bin/env python3
"""Pickle serialization for a custom class.

Provides `CustomObject` with `serialize` and `deserialize` methods.
If serialization/deserialization fails, methods return None.
"""
import pickle
from typing import Optional


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self) -> None:
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str) -> Optional[None]:
        """Serialize this instance to `filename` using pickle.

        Returns None on failure.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename: str) -> Optional["CustomObject"]:
        """Load and return a `CustomObject` instance from `filename`.

        Returns None if the file does not exist, is malformed, or
        does not contain a `CustomObject`.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            return None
        except (FileNotFoundError, pickle.UnpicklingError, EOFError, AttributeError, Exception):
            return None
