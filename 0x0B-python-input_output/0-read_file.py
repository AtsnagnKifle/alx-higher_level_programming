#!/usr/bin/python3
"""
    read file
"""


def read_file(filename=""):
    """
        read file
    """
    with open(filename, mode="r", encoding="utf-8") as a_file:
        for line in a_file:
            print(line, end="")
