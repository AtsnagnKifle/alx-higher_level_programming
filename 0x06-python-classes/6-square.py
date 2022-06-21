#!/usr/bin/python3
"""
no module imported
"""


class Square:
    """
    defines a square by private attribute size,
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        private instance attribute
        parameters
        size : integer else TypeError
        if size less than 0, raise value error
        position : private instance attribute
        """
        self.__size = size
        self.__position = position
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

    @property
    def position(self):
        """
        retrieve private sttribute position
        """
        return self.__position

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
        print squre
        """
        if self.size == 0:
            print()
        for i in range(self.positsion[1]):
            print("\n")
        for i in range(self.size):
            for j in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()
