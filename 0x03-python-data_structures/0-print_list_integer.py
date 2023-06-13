#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """print integer of a list"""
    for number in range(len(my_list)):
        print("{:d}".format(my_list[number]))
