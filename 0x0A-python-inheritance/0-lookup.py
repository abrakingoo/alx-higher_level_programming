#!/usr/bin/python3
def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

    Args:
        object to examine

    Return:
         list of available attributes and methods of an object

    """

    return dir(obj)
