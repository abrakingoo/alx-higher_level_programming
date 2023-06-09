#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    length = len(my_list)

    if idx < 0 or idx > length:

        return my_list

    else:

        list_copy = my_list.copy()

        for i in range(length):

            if i == idx:

                list_copy[i] = element

        return list_copy
