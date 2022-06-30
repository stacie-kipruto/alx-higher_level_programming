#!/usr/bin/python3

"""
    Test-driven development
    text_indentation
"""


def text_indentation(text):
    """ prints a text with two lines after ?, . or :
    Args:
        text: string to process
        If text is not a string, raise a TypeError with message
        'text must be a string'
        There should be no space at the beginning and end of each
        printed line
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    line = ""
    for ch in text:
        line = line + ch
        if ch in '?.:':
            print("{}".format(line.strip()))
            print()
            line = ""
    print(line.strip(), end="")
