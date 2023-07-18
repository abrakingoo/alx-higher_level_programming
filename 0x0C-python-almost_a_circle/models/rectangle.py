#!/usr/bin/python3
"""Contains the "Rectangle" class
"""


from models.base import Base


class Rectangle(Base):
    """Inherits from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor

        Creates private instance attributes
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """defines a width getter
        """
        return self.__width

    @width.setter
    def width(self, val):
        """Defines a width setter
        """
        if type(val) is not int:
            raise TypeError("{} must be an integer".format("width"))

        if val <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = val

    @property
    def height(self):
        """defines a height getter
        """
        return self.__height

    @height.setter
    def height(self, val):
        """Defines a height setter
        """
        if type(val) is not int:
            raise TypeError("{} must be an integer".format("height"))

        if val <= 0:
            raise ValueError("{} must be > 0".format("height"))
        self.__height = val

    @property
    def x(self):
        """defines a x getter
        """
        return self.__x

    @x.setter
    def x(self, val):
        """Defines a x setter
        """
        if type(val) is not int:
            raise TypeError("{} must be an integer".format("x"))

        if val < 0:
            raise ValueError("{} must be >= 0".format("x"))
        self.__x = val

    @property
    def y(self):
        """defines a y getter
        """
        return self.__y

    @y.setter
    def y(self, val):
        """Defines a y setter
        """
        if type(val) is not int:
            raise TypeError("{} must be an integer".format("y"))

        if val < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__y = val

    def area(self):
        """Returns the area of the rectangle
        """
        A = self.width * self.height
        return (A)

    def display(self):
        """Prints Rectangle instance with '#' character
        """
        for i in range(self.y):
            print("")

        for i in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns a neatly formatted output
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                                                                self.id,
                                                                self.x,
                                                                self.y,
                                                                self.width,
                                                                self.height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        """
        if args:
            self.__argpassed(*args)
        else:
            self.__argpassed(**kwargs)

    def __argpassed(self, id=None, width=None, height=None, x=None, y=None):
        """Validates the args passed"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle
        """
        my_dict = {}
        my_dict['id'] = self.id
        my_dict['width'] = self.width
        my_dict['height'] = self.height
        my_dict['x'] = self.x
        my_dict['y'] = self.y

        return (my_dict)
