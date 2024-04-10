#!/usr/bin/python3

class LockedClass:
    """A class that prevents instance except instance with the attribute first_name
    """
    __slots__ = ["first_name"]
