#!/usr/bin/python3


def safe_print_division(a, b):
    """
    It divides two integers and prints the result
    Then catches divide by zero exception
    """
    try:
        res = a / b
    except:
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res
