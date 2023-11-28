#!/usr/bin/python3
"""The class with predefined number of slots"""


class LockedClass:
    """if the user is defined, no new items can be added to list"""
    __slots__ = ['first_name']
