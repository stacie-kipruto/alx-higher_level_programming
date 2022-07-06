#!/usr/bin/python3
"""
3-is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """
    return True if obj is instance of a_class or instance of
    a class that inherited from a_class.
    otherwise return False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
