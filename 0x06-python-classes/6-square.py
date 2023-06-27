#!/usr/bin/python3
""" a class Square that defines a square by size"""


class Square:
    """Instantiation with size"""
    def __init__(self, size=0, position=(0, 0)):
        """Private instance attribute: size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

    def area(self):
        """returns the current square area"""

        return self.__size ** 2

    @property
    def position(self):
        """adding a getter for the private attribute size"""
        return self.__position

    @position.setter
    def size(self, position=(0, 0)):
        """setting the new value for the private attribute"""
        if not isinstance(position[0], int) \
                and not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """adding a getter for the private attribute size"""
        return self.__size

    @size.setter
    def size(self, size):
        """setting the new value for the private attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()

        else:
            for _ in range(self.size):
                for _ in range(self.__position[0]):
                    print(" ", end="")
                for _ in range(self.size):
                    print("#", end="")
                print()
