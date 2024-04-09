#!/usr/bin/python3
# by UGWU BONIFACE OYU : ugwubonifaceotu1998@gmail.com
"""A class that defines a rectanglie based on 5-rectangle.py"""


class Rectangle:
    """This is a defined class for rectangle"""

    """ A class Attribute which is public  """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """instantiation with the width and height optional"""
        self.__class__.number_of_instances += 1
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
            ([rec_print.append(str(self.print_symbol))
                for j in range(self.__width)])
            if i != self.__height - 1:
                rec_print.append("\n")
        return ("".join(rec_print))

    def __repr__(self):
        """ A string rep.. of the Rectangle n the format Rectangle(2, 4)"""
        rect_rep = "Rectangle(" + str(self.__width)
        rect_rep += ", " + str(self.__height) + ")"
        return rect_rep

    def __del__(self):
        """ Prints a message when a Rectangle is being deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
