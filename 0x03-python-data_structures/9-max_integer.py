#!/usr/bin/python3
def max_integer(my_list=[]):
    ma = 0
    if my_list == []:
        return None
    else:
        for i in my_list:
            if i > ma:
                ma = i
    return ma
