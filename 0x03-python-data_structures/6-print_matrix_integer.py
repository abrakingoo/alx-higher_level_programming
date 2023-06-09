#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for i in range(len(matrix)):
        for j in matrix[i]:

            print("{}".format(j), end=' ')

        print()
