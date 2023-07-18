#!/usr/bin/python3
"""Contains the Base class
"""


import json


class Base:
    """Base class for other classes

    Creates a private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor
        """
        if id:
            self.id = id

        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"

        if not list_dictionaries:
            return "[]"

        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        """
        filename = "{}.json".format(cls.__name__)

        my_list = []

        if list_objs is not None:
            for obj in list_objs:
                my_list.append(cls.to_dictionary(obj))

        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string
        """
        if json_string is None or not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            dummy = Rectangle(2, 1)

        elif cls is Square:
            dummy = Square(1)

        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        """
        filename = "{}.json".format(cls.__name__)

        lst = []

        try:
            with open(filename, "r") as f:
                lst = cls.from_json_string(f.read())

            for i, val in enumerate(lst):
                lst[i] = cls.create(**lst[i])

        except FileNotFoundError:
            pass

        return lst
