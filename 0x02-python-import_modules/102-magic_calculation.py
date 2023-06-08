#!/usr/bin/python3

from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    if a < b:
        c = a + b
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)

if __name__ == "__main__":
    result = magic_calculation(4, 7)
    print(result)

