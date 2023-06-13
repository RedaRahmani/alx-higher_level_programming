#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """replaces an element of a list at a specific position (like in C)"""
    if idx < len(my_list) and idx >= 0:
        my_list[idx] = element
    return (my_list)
