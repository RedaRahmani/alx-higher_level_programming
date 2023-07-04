#!/usr/bin/python3
"""
Defines a name-printing function.
Module say_my_name
Prints a given first name and last name.
"""


def say_my_name(first_name, last_name=""):
    """Print a string with <first_name> and <last_name>.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")

    if (type(last_name) is not str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
