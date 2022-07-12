#!/usr/bin/python3
"""
5-save_to_json_file module
"""


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file using a JSON representation
    """
    import json
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
