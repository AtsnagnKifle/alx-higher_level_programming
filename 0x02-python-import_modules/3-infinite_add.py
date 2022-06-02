#!/usr/bin/python3
import sys
if __name__ == "__main__":
    li = [int(i) for i in sys.argv[1:]]
    print("{}".format(sum(li)))
