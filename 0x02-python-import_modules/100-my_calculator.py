#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    length = len(argv)

    if length < 3:

        print("Usage: ./100-my_calculator.py <a> <operator> <b>")

        exit(1)

    num1 = int(argv[1])
    num2 = int(argv[3])
    operator = argv[2]

    match operator:

        case "+":

            print("{:d} + {:d} = {}".format(num1, num2, add(num1, num2)))

        case "-":

            print("{:d} - {:d} = {}".format(num1, num2, sub(num1, num2)))

        case "+":

            print("{:d} * {:d} = {}".format(num1, num2, mul(num1, num2)))

        case "/":

            print("{:d} / {:d} = {}".format(num1, num2, div(num1, num2)))

        case _:

            print("Unknown operator. Available operators: +, -, * and /")

            exit(1)
