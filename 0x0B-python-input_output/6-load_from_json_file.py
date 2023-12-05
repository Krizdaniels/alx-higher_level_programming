#!/usr/bin/python3
"""Python - Input/Output,for task 6. Create object from a JSON file  """


def load_from_json_file(filename):
    """It creates an object from a JSON file.

    Args:
        filename (str): file containing serialized object string

    """
    import json

    with open(filename, encoding='utf-8') as file:
        return json.load(file)
