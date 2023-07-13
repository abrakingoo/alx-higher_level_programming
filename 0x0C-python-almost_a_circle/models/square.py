#!/usr/bin/python3
""""
the class Square that inherits from Rectangle:
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
        Calls the super class
        """
        self.x = x
        self.y = y
        self.size = size
        self.id = id
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        The overloading __str__ method
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("width must be an integer")

        self.__size = size
