#!/usr/bin/python3
"""
 a function that returns the list of available
 attributes and methods of an object:
"""


def lookup(obj):
    """
    perints the list of available attributes and methods of an object

    Args:
        object

    Return:
         list of available attributes and methods of an object

    """

    return(dir(obj))
