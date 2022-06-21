#!/usr/bin/python3
"""
no module imported
"""


class Square:
    """
    defines a square by private attribute size,
    """

    def __init__(self, size=0):
        """
        private instance attribute
        parameters
        size : integer else TypeError
        if size less than 0, raise value error
        """
        self.__size = size
        try:
            assert type(size) == int
        except Exception as e:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        public instance method
        return square area
        """
        return self.__size**2

    @property
    def size(self):
        """
        retrieve private attribute size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set private attribute
        """
        self.__size = value
        try:
            assert type(value) == int
        except Exception as e:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """
        print square
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
