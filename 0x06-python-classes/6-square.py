#!/usr/bin/python3
"""Defines a square"""

class Square:
    """
    The class square that has attributes:
        size
    some attributes are protected from input.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        The initialization function for our square clasee
        """
        if self.__validate_size(size):
            self.__size = size
        if self.__validate_pos(position):
            self.__position = position

    @property
    def size(self):
        """
        The getter for size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        The setter for size attribute
        """
        if self.__validate_size(value):
            self.__size = value

    @property
    def position(self):
        """
        The getter for position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        The setter for position attribute
        """
        if self.__validate_pos(value):
            self.__position = value

    def area(self):
        """
        It calculates the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        It prints the square using '#' characters
        also takes into account position (x, y) offsets
        """
        i = 0
        if self.__size == 0:
            print()
            return
        for i in range(0, self.__position[1]):
            print()
        i = 0
        for i in range(0, self.__size):
            j = 0
            x_pad = 0
            for x_pad in range(0, self.__position[0]):
                print(" ", end='')
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

    def __validate_pos(self, position):
        """
        It validates the position, checking for type errors
        """
        if not isinstance(position, type((0, 0))):
            raise TypeError("position must be a tuple of 2 positive integers")
            return False
        return True
