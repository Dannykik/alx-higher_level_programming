#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE# Extract
if number > 0:
    last_digit = number % 10

    # Print the required output
    print("Last digit of", number, "is", last_digit, end=" ")
    if last_digit > 5:
        print("and is greater than 5")
    if last_digit == 0:
        print("and is 0")
if number < 0:
    last_digit = abs(number) % 10
    last_digit = last_digit*(-1)
    print("Last digit of", number, "is", last_digit, end=" ")
    if last_digit < 6 and last_digit != 0:
        print("and is less than 6 and not 0")
