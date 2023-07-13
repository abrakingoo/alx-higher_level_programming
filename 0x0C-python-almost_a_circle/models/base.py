#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project.
"""
import json


class Base:
    """
    Class Base: with
    private class attribute __nb_objects = 0
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor:
            :if id is not None, assign the public instance
            attribute id with this argument value

            :otherwise, increment __nb_objects and assign the new value
            to the public instance attribute id
        """

        if id is not None:
            self.id = id

        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
         static method def to_json_string(list_dictionaries): that
         returns the JSON string representation of list_dictionaries:
         """

        if list_dictionaries is None:
            return []

        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__+".json"
        if list_objs is None:
            with open(file_name, "w") as file:
                json.dump([], file)

        else:
            my_list = []
            for obj in list_objs:
                my_list.append(obj.to_dictionary())
            with open(file_name, "w", encoding="utf-8") as file:
                json.dump(my_list, file)


    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []

        else:
            return json.loads(json_string)
