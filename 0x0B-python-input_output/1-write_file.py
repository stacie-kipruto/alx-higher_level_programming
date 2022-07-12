#!/usr/bin/python3
"""
1-write_file module
"""


def write_file(filename="", text=""):
    """
    write a string to a text file and returns number of characters
    written
    """
    char_count = 0
    with open(filename, mode="w", encoding="utf-8") as f:
        for letter in text:
            char_count += 1
            f.write(letter)
    return char_count
