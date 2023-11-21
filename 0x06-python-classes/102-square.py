#!/usr/bin/python3
"""Square module."""

class Square:
    """Define a square."""


    def __init__(self, size=0):
        """
        The initialization function for our square clasee
        """
        if self.__validate_size(size):
            self.__size = size

    def __eq__(self, other):
        """
        It is used by == to check equality
        """
        return (self.area() == other.area())

    def __ne__(self, other):
        """
        It is used by != to check equality
        """
        return (self.area() != other.area())

    def __lt__(self, other):
        """
        It is used by < to check equality
        """
        return (self.area() < other.area())

    def __le__(self, other):
        """
        It is used by <= to check equality
        """
        return (self.area() <= other.area())

    def __gt__(self, other):
        """
        It is used by > to check equality
        """
        return (self.area() > other.area())

    def __ge__(self, other):
        """
        It is used by >= to check equality
        """
        return (self.area() >= other.area())

    @property
    def size(self):
        """Propert for the length of a side of this square.

        Raises:
            TypeError: If size is not an Integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        The setter for size attribute
        """
        if self.__validate_size(value):
            self.__size = value

    def area(self):
        """
        It calculates the area of the square
        """
        return self.__size ** 2

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
