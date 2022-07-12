#!/usr/bin/python3
"""
module documentation
"""


class Square:
    """
    Square class
    """
    def __init__(self, size=0):
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
