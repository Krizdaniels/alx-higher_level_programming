#!/usr/bin/python3
""" Python - Inheritance, for task 1 """


class MyList(list):
    """The custom list type intended to only contain integers.

    """

    def print_sorted(self):
        """It prints MyList lists in ascending order by value.

        """
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
