#!/usr/bin/python3
"""
    base class
"""
import json


class Base:
    """
        base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Base class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            return JSON string representation
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def from_json_string(self, json_string):
        """
            returns a list of json string representation
        """
        if json_string is None or json_string == 0:
            return []
        return json.loads(json_string)
