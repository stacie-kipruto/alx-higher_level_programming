#!/usr/bin/python3
"""
module documentation
"""


class Square:
    """
    Square documentation
    """
    def __init__(self, size=0):
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, x):
        if type(x) == int:
            if x >= 0:
                self.__size = x
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        if self.__size <= 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
