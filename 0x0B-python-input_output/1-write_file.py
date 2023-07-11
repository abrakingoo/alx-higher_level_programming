#!/usr/bin/python3
"""
a function that writes a string to a text file (UTF8)
and returns the number of characters written:
"""


def write_file(filename="", text=""):
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

    with open(filename, 'w', encoding="utf-8") as file:
        count = file.write(text)

    return count
