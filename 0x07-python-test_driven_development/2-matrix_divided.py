#!/usr/bin/python3

"""
    test-driven development exercise 1
    matrix_divide
"""


def matrix_divided(matrix, div):
    """ divide all elements of a matrix by a specified number
    Args:
        matrix: list of lists(matrix)
        div: number to divide by
    Matrix must be a list of lists of integers or floats,
        Otherwise raise a TypeError exception with the message:
        'matrix must be a matrix (list of lists) of integers/floats'
    Each row of the matrix must be of the same size,
        Otherwise raise a TypeError exception with the message:
        'Each row of the matrix must have the same size'
    div must be a number (integer or float),
        Otherwise raise a TypeError exception with the message:
        'div must be a number'
    div can’t be equal to 0,
        Otherwise raise a ZeroDivisionError exception with the message:
        'division by zero'
    All elements of the matrix should be divided by div,
        rounded to 2 decimal places
    Return: a new matrix
    """
    if not isinstance(matrix, list) or len(matrix) == 0 or \
       not all(isinstance(row, list) for row in matrix) or \
       not all(isinstance(elem, (int, float)) for row in matrix
               for elem in row):
        msg = 'matrix must be a matrix (list of lists) of integers/floats'
        raise TypeError(msg)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(elem / div, 2) for elem in row] for row in matrix]
