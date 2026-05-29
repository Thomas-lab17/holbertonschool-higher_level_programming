#!/usr/bin/env python3
"""XML serialization utilities.

Provides `serialize_to_xml` and `deserialize_from_xml` for simple
dictionary <-> XML conversion.
"""
import xml.etree.ElementTree as ET
from typing import Dict, Optional


def serialize_to_xml(dictionary: Dict[str, object], filename: str) -> None:
    """Serialize a dictionary to an XML file at `filename`.

    Each key becomes a child element of the root; values are stored
    as text. Values are converted to strings.
    """
    root = ET.Element('root')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename: str) -> Optional[Dict[str, str]]:
    """Deserialize XML file at `filename` and return a dictionary.

    Returns None on parse/file errors.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result: Dict[str, str] = {}
        for child in root:
            result[child.tag] = child.text if child.text is not None else ''
        return result
    except (FileNotFoundError, ET.ParseError):
        return None
