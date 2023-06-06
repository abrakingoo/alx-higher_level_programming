#!/usr/bin/python3

new_str = ""
for i in range(26):

    if i % 2 == 0:

        new_str += chr(97 + i)

    else:

        new_str += chr(65 + i)

reversed_str = new_str[::-1].swapcase()
print("{}".format(reversed_str))
