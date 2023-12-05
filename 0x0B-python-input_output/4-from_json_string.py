#!/usr/bin/python3
"""Python - Input/Output, task 4. From JSON string to Object  """


def from_json_string(my_str):
    """It returns an object (Python data structure) represented
    by a JSON string.

    Args:
        my_obj (any): object to be serialized

    """
    import json

    return json.loads(my_str)
