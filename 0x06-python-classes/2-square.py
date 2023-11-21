#!/usr/bin/python3
"""Defines a square"""

class Square:
    """
    The class square that has attributes:
        size
    some attributes are protected from input.
    """
    def __init__(self, size=0):
        """
        Initialization function for the square class
        checks for input errors for size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
