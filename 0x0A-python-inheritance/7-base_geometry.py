#!/usr/bin/python3
"""
5-base_geometry module
"""


class BaseGeometry:
    """
    public method "area"
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
