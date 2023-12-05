#!/usr/bin/python3
"""Python - Input/Output,for task 0. Read file """


def read_file(filename=""):
    """It reads contents of a text file and print to stdout.

    Args:
        filename (str): name of file to be opened

    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
