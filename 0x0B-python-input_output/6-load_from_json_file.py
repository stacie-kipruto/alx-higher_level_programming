#!/usr/bin/python3
"""
6-load_from_json_file module
"""


def load_from_json_file(filename):
    """
    create object from a JSON file
    """
    import json
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.loads(f.read())
