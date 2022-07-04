#!/usr/bin/python3

"""
    Task to demonstrate a class that makes it impossible to create
    new instance attributes of it dynamically
"""


class LockedClass:
    """ class that prevents creation of new instance attributes
        dynamically
    """
    __slots__ = ["first_name"]

    def __init__(self):
        pass
