#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    numbers = []

    for i in range(1, len(argv)):

        numbers.append(int(argv[i]))

    print(sum(numbers))
