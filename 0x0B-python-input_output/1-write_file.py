#!/usr/bin/python3
"""
    write file
"""


def write_file(filename="", text=""):
    """
        write file
    """
    with open(filename, mode="w", encoding="utf-8") as a_file:
        wr = a_file.write(text)
    return wr
