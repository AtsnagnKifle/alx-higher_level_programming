#!/usr/bin/python3
def element_at(my_list, idx):
    ln = len(my_list)
    if idx < 0 or (ln-1) < idx:
        return None
    return my_list[idx]
