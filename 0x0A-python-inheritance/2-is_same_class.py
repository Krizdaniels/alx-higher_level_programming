#!/usr/bin/python3
""" Python - Inheritance, for task 2 """


def is_same_class(obj, a_class):
    """It tests if an object is exactly an instance of a specific class.

    Args:
        obj (any): object of any type
        a_class (class): class to test against

    Returns:
        True if obj is an instance of a_class, False otherwise.

    """
    return (type(obj) == a_class)
