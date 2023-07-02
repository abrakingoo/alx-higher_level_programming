#!/usr/bin/python3
"""
    adds 2 integers.

    and returns their value

"""


def add_integer(a, b=98):
    """a function that adds 2 integers.

    Args:
        a: first argument
        b: second argument

    Returns:
        sum of the two arguments

    Raises:
        TypeError: if either of the arguments not int or float

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
