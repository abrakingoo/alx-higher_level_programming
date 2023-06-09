#!/usr/bin/python3

def delete_at(my_list=[], idx=0):

    length = len(my_list)

    if idx < 0 or idx > length:

        return my_list

    else:

        for i in range(length):

            if i == idx:
                del(my_list[i])

        return my_list
