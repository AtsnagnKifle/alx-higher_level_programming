#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    ln = len(my_list)
    if idx < 0 or (ln-1) < idx:
        return my_list
    my_list[idx] = element
    return my_list
