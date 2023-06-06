#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdigit = number % -10
elif number < 10:
    lastdigit = number
elif number >= 10 and number <= 10000:
    lastdigit = number % 10

const = f"Last digit of {number} is {lastdigit}"

if lastdigit > 5:
    print(const + " and is greater than 5")
elif lastdigit == 0:
    print(const + " and is 0")
elif lastdigit < 6 and lastdigit != 0:
    print(const + " and is less than 6 and not 0")
