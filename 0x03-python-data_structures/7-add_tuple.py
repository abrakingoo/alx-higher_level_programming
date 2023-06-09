#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a, b = 0, 0
    c, d = 0, 0

    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0, 0)
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0, 0)

    a, b = tuple_a[:2]
    c, d = tuple_b[:2]

    return a + c, b + d
