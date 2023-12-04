#!/usr/bin/python3
""" Python - Inheritance, for task 0 """


def lookup(obj):
    """It returns the list of available attributes and methods of an object.

    Args:
        obj (any): object of any type

    Returns:
        list of available attributes and methods

    """
    return dir(obj)
