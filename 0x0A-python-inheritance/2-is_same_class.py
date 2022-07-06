#!/usr/bin/python3
"""
2-is_same_class module
"""


def is_same_class(obj, a_class):
    """
    returns True if obj is exactly an instance of a_class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
