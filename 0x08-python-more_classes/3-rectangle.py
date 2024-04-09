#!/usr/bin/python3
# by OLADAPO ODEDEYI : dapoodedeyi@yahoo.com
"""A class that defines a rectangle based on 1-rectangle.py"""


class Rectangle:
    """This is a defined class for rectangle"""
    def __init__(self, width=0, height=0):
        """instantiation with the width and height optional"""
        self.width = width
        self.height = height

    """Private instance attribute"""
    @property
    def width(self):
        """property setter FOR WIDTH"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter for the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """another private instance"""
    @property
    def height(self):
        """a  private instance getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """the setter for the height property"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """public instance method"""
        return self.__width * self.__height

    def perimeter(self):
        """public instance method for the erimeter of a rectangle"""
        if self.__width == 0 or self.__height == int(0):
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ Returns the printable representation of the rectangle


        with the # character"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rec_print = []
        for i in range(self.__height):
            [rec_print.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                rec_print.append("\n")
        return ("".join(rec_print))
