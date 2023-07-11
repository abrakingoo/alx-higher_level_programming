#!/usr/bin/python3


""" a function that adds a new attribute to
an object if it’s possible:
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: Object to add the attribute to.
        attr: Name of the attribute to be added.
        value: Value of the attribute.

    Raises:
        TypeError: If the object already has the attribute.

    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
