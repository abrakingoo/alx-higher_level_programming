#!/usr/bin/python3

def uppercase(str):
    length = len(str)
    new_str = ""
    for i in range(length):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            new_str += chr(ord(str[i]) - 32)
        else:
            new_str += str[i]

    print("{}".format(new_str))
