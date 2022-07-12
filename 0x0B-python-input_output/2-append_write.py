#!/usr/bin/python3
"""
2-append_write module
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file and returns the
    number of characters added
    """
    char_count = 0
    with open(filename, mode="a", encoding="utf-8") as f:
        for letter in text:
            char_count += 1
            f.write(letter)
    return char_count
