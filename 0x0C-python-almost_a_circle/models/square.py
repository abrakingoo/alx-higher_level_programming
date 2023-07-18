#!/usr/bin/python3
"""Contains the Square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updater for the class Square
        """
        if args:
            self.__squareArgs(*args)
        else:
            self.__squareArgs(**kwargs)

    def __squareArgs(self, id=None, size=None, x=None, y=None):
        """Validates the args passed"""
        if id is not None:
            self.id = id

        if size is not None:
            self.size = size

        if x is not None:
            self.x = x

        if y is not None:
            self.y = y

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                                                        self.id,
                                                        self.x,
                                                        self.y,
                                                        self.size)

    def to_dictionary(self):
        """returns a dictionary representation of a square
        """
        my_dict = {}
        my_dict['id'] = self.id
        my_dict['size'] = self.size
        my_dict['x'] = self.x
        my_dict['y'] = self.y

        return (my_dict)
