#!/usr/bin/python3
"""
    an empty class Rectangle that defines a rectangle:
"""


class Rectangle:
    """
    an empty class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
         returns the rectangle area

         Returns:
             returns the rectangle area
        """

        return (self.__height * self.__width)

    def perimeter(self):
        """
        Public instance method
        that returns the rectangle perimeter

        Returns:
            the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:

            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):

        mystr = ""

        if self.__height == 0 or self.__width == 0:

            return mystr

        else:

            for i in range(self.__height):
                mystr += "#" * self.__width
                if i != self.__height - 1:
                    mystr += "\n"

            return mystr
