#!/usr/bin/python3

"""
    no module imported
"""


class Rectangle:
    """ An Empty Rectangle Class """

    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = height

    @property
    def width(self):
        """
            get the value of width
        """
        return self._width

    @property
    def height(self):
        """
            get the value of height
        """
        return self._height

    @width.setter
    def width(self, val):
        """
            set the value of width
            raise TypeError if value is not an int
            raise ValueError if value is < 0
        """
        if type(val) != int:
            raise TypeError("width must be an integer")
        elif val < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = val

    @height.setter
    def height(self, val):
        """
            set the value of height
            raise TypeError if value is not an int
            raise ValueError if value is < 0
        """
        if type(val) != int:
            raise TypeError("height must be an integer")
        elif val < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = val
