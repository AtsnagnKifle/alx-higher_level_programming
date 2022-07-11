#!/usr/bin/python3
"""
    rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
        rectangle class
    """

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
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
            returns the area value of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
            print rectangle instance using # character
        """
        for line in range(self.__y):
            print()
        for i in range(self.__height):
            for space in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")

            print()

    def __str__(self):
        """
            str method to return rectangle representation
        """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)
