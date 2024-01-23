#!/usr/bin/python3
def no_c(my_string):
    new_list = list(my_string)
    for i in new_list:
        if ord(i) == 99:
            new_list.remove(i)
    result = ''.join(new_list)
    return result
