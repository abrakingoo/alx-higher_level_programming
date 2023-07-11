#!/usr/bin/python3
"""a class MyInt that inherits from int:"""


class MyInt(int):
    """a class MyInt"""
    def __eq__(self, value):
        """ == operator inverted """
        return super().__ne__(value)

    def __ne__(self, value):
        """ != not equal to operator inverted """
        return super().__eq__(value)
