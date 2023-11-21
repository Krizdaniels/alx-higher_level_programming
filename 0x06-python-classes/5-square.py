#!/usr/bin/python3
"""Defines a square"""


class Square:
    """
    It class square that has attributes:
        size
    some attributes are protected from input.
    """
    def __init__(self, size=0):
        """
        The initialization function for our square clasee
        """
        if self.__validate_size(size):
            self.__size = size

    @property
    def size(self):
        """
        The getter for the size property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        The setter for the size property
        """
        if self.__validate_size(value):
            self.__size = value

    def area(self):
        """
        It calculates the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        it prints the square using '#' characters
        """
        i = 0
        for i in range(0, self.__size):
            j = 0
            for j in range(0, self.__size):
                print("#", end='')
            print()

    def __validate_size(self, size):
        """
        It validates the size, checking for errors
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True
        return False
