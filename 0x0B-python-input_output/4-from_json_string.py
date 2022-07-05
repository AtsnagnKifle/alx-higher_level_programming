#!/usr/bin/python3
"""
    returns python data structure
"""
import json


def from_json_string(my_str):
    """
        returns Python data structure)
    """
    data = json.loads(my_str)
    return data
