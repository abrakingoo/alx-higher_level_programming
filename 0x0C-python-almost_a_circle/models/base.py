#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project.
"""


class Base:
    """
    Class Base: with
    private class attribute __nb_objects = 0
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor:
            :if id is not None, assign the public instance
            attribute id with this argument value

            :otherwise, increment __nb_objects and assign the new value
            to the public instance attribute id
        """

        if id is not None:
            self.id = id

        else:
             self.__class__.__nb_objects += 1
             self.id = self.__class__.__nb_objects
