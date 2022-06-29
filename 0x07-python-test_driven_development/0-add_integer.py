#!/usr/bin/python3
"""
add integer
"""


def add_integer(a, b=98):
    """
        Adds two integers
    """
    try:
        assert type(a) in (float, int)
    except Exception as e:
        raise TypeError("a must be an integer")
    try:
        assert type(b) in (float, int)
    except Exception as e:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
