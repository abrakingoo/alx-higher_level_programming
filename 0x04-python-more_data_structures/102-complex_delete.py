#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    if value:

        keys_to_be_deleted = []

        for key, val in a_dictionary.items():
            if val == value:
                keys_to_be_deleted.append(key)

        for key in keys_to_be_deleted:
            del a_dictionary[key]

        return a_dictionary

    else:
        return a_dictionary
