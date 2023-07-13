#!/usr/bin/python3
"""
the class Rectangle that inherits from Base:
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor:
        Call the super class with id - this super call with
        use the logic of the __init__ of the Base class
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @width.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        return self.__x

    @width.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
