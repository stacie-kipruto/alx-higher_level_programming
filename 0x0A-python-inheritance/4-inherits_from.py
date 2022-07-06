#!/usr/bin/python3
"""
4-inherits_from module
"""


def inherits_from(obj, a_class):
    """
    returns True if object is an instance of a class that inherited
    (directly or indirectly) from a_class.
    otherwise return False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
