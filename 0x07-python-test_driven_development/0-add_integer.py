#!/usr/bin/python3
""" a function that computes the addition of two ints"""


def add_integer(a, b=98):
    """it returns the integer addition of a and b """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return (int(a) + int(b))
