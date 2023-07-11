#!/usr/bin/python3


"""a class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size):
        """Instantiation with size"""

        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """the area() method"""
        return self.__size * self.__size

    def __str__(self):
        """the square description"""
        return f"[Square] {self.__size}/{self.__size}"
