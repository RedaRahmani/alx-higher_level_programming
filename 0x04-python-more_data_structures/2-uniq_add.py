#!/usr/bin/python3
def uniq_add(my_list=[]):
    newList = set(my_list)
    result = 0
    for number in newList:
        result += number
    return result
