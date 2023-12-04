#!/usr/bin/python3
""" Python - Inheritance, for task 12 """


class MyInt(int):
    """The custom int type inverting behavior of != and == operators.

    """

    def __eq__(self, other):
        """it reverses behavior of == operator.

        """
        return int(self) != int(other)

    def __ne__(self, other):
        """It reverses behavior of != operator.

        """
        return int(self) == int(other)
