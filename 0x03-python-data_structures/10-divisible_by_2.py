#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list is None:
        my_list = []

    result = [i%2 == 0 for i in my_list]
    return result
