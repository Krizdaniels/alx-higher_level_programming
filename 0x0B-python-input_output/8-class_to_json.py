#!/usr/bin/python3
"""Python - Input/Output,for task 8. Class to JSON"""


def class_to_json(obj):
    """It returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object.

    Args:
        obj (any): object to be serialized

    """
    return obj.__dict__
