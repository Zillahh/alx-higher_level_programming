#!/usr/bin/python3
"""A class Rectangle that defines a rectangle based on the file 0-rectangle.py"""


class Rectangle:
    """Defining the class for rectangle"""
    def __init__(self, width=0 height=0):
        """instantiation with optional width and height"""
        self.width = width
        self.height = height

        """private instance attribute"""
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
        """a private instance getter for height"""
        returnn self.__height

    @height.setter
    def height(self, value):
        """the setter for the height property"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

