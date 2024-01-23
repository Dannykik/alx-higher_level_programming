#!/usr/bin/python3
def max_integer(my_list=[]):
    leng = len(my_list) - 1 
    my_list.sort()
    mx = my_list[leng]
    return mx
