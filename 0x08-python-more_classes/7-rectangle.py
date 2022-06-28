#!/usr/bin/python3

"""
    no module imported
"""


class Rectangle:
    """ An Empty Rectangle Class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        st = ""
        if self.__width == 0 or self.__height == 0:
            return st
        st += (str(self.print_symbol)*self.__width+"\n")*self.__height
        return st[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """
            get the value of width
        """
        return self.__width

    @property
    def height(self):
        """
            get the value of height
        """
        return self.__height

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
            self.__width = val

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
            self.__height = val

    # @classmethod
    # def print_symbol(self, val):
    #     """
    #         set the value of print_symbol
    #     """
    #     print(val)
    #     print("*******")
    #     Rectangle.print_symbol = val

    def area(self):
        """
            calculate and return the
            area of a Rectangle
        """
        area = self.__height * self.__width
        return area

    def perimeter(self):
        """
            calculate and return the
            perimeter of a rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        perimeter = 2 * (self.__width + self.__height)
        return perimeter
