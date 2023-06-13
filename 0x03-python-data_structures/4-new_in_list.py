#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """replaces an element in a list at a specific position as a copy"""

    copy_list = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        copy_list[idx] = element
        return copy_list
