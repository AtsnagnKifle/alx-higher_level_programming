#!/usr/bin/python3
import sys
if __name__ == "__main__":
    li = sys.argv
    li_len = len(li)

    if li_len == 1:
        print("{} arguments.".format(0))
    elif li_len == 2:
        print("{} argument:".format(1))
    else:
        print("{} arguments:".format(li_len-1))
    for i in range(1, li_len):
        print("{}: {}".format(i, li[i]))
