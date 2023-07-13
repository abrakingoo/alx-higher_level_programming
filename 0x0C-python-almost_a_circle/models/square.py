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

        self.__width = size
        self.__height = size

    def update(self, *args, **kwargs):
        """
        adding the public method update(self, *args, **kwargs)
        that assigns attributes:

        """

        if not args:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.height = value
                    self.width = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
        else:

            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
                self.height = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
