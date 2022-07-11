#!/usr/bin/python3
"""
    rectangle class
"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            rectangle class constractor
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
            return width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            set width
        """
        self.__width = value

    @property
    def height(self):
        """
            return height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            set height
        """
        self.__height = value

    @property
    def x(self):
        """
            return x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            set x
        """
        self.__x = value

    @property
    def y(self):
        """
            return y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            set y
        """
        self.__y = value
