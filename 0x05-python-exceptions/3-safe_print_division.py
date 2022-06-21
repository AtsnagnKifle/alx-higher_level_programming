#!/usr/bin/python3

def safe_print_division(a, b):
    result = None
    try:
        n = a/b
        result = n
    except ZeroDivisionError:
        pass
    print("Inside result: {}".format(result))
    return result
