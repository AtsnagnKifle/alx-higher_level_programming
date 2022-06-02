#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    li = sys.argv[1:]
    li_len = len(li)
    a = li[0]
    b = li[2]
    if li_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif li[1] == "+":
        print("{} + {} = {}".format(a, b, add(int(li[0]), int(li[2]))))
    elif li[1] == "-":
        print("{} - {} = {}".format(a, b, sub(int(li[0]), int(li[2]))))
    elif li[1] == "*":
        print("{} * {} = {}".format(a, b, mul(int(li[0]), int(li[2]))))
    elif li[1] == "/":
        print("{} / {} = {}".format(a, b, div(int(li[0]), int(li[2]))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    exit(0)
