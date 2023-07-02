#!/usr/bin/python3
"""
A function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int or float): The number to divide the matrix elements with.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is equal to 0.

    Returns:
        list: A new matrix with the divided elements.

    """

    if (
        not isinstance(matrix, list) or
        matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(
            isinstance(ele, int) or isinstance(ele, float)
            for ele in [num for row in matrix for num in row]
        )
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(x / div, 2) for x in row]
        for row in matrix
    ]
