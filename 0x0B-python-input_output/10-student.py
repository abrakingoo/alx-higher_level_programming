#!/usr/bin/python3
"""
a class Student that defines a student by
"""


class Student:
    """
    a class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Public instance attributes:
            first_name
            last_name
            age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
         retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__

        else:
            found = {}

            for attr in attrs:
                if hasattr(self, attr):
                    found[attr] = getattr(self, attr)

            return found
