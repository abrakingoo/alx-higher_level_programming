#!/usr/bin/python3


"""
a function that appends a string at the end of a text file (UTF8)
and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """
    writes a string to a text file

    Args:
        filename:
            the file to write to

        text:
            the string to write to the text file

    Return:
        The number of characters written

    """

    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
