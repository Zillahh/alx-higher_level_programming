#!/usr/bin/python3
#work by: ugwu boniface otu
"""A class with no class or object attribute

that prevents user: from creating new instance attribute

except: if the new instance attribute is called first_name

"""

class LockedClass:
    """A class that prevents instance except instance with the attribute first_name
    """
    __slots__ = ["first_name"]
