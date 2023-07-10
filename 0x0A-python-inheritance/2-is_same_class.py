#!/usr/bin/python3
"""
a function that returns True if the object is exactly an instance of
the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    checks the class of an object

    Args:
        obj: objext to be checked

        a_class: checks if the obj is of this class

    Return:
        True:if the object is exactly an instance of
            the specified class

        False: if the object is not of exactly  instance as
            the specified class

    """
    return type(obj) is a_class
