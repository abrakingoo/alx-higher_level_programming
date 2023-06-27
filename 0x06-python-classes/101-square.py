#!/usr/bin/python3
"""defines a square by: (based on 6-square.py)"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position"""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple
                            of 2 positive integers")
        self.__position = value

    def area(self):
        """Compute the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with # characters"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """String representation of the square"""
        output = ""
        if self.__size == 0:
            return output
        else:
            for _ in range(self.__position[1]):
                output += '\n'
            for _ in range(self.__size):
                output += " " * self.__position[0] + "#" * self.__size + '\n'
        return output.rstrip()
