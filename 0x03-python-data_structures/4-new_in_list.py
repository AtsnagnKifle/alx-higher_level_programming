#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    ln = len(my_list)
    li = list.copy(my_list)
    if idx < 0 or (ln-1) < idx:
        return li
    li[idx] = element
    return li
