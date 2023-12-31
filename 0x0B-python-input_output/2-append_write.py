#!/usr/bin/python3
"""Python - Input/Output, task 2. Append to a file """


def append_write(filename="", text=""):
    """It appends a string at the end of a text file (UTF8) and returns the
number of characters added.

    Args:
        filename (str): name of file to be opened
        text (str): chars to be written

    """
    with open(filename, 'a', encoding='utf-8') as file:
        chars_written = file.write(text)
        return chars_written
