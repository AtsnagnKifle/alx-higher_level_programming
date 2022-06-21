#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    re = None
    try:
        re = fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
    return re
