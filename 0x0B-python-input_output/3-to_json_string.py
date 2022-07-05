#!/usr/bin/python3
import json
"""
    returns json representation
"""


def to_json_string(my_obj):
    """
        returns the json representation
    """
    data = json.dumps(my_obj)
    return data
