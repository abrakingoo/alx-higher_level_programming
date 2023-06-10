#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    rev_list = my_list[::-1]

    for i in range(length):
        print("{:d}".format(rev_list[i]))
