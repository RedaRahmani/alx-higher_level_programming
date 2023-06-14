#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy_list = []
    for number in range(len(my_list)):
        if my_list[number] == search:
            copy_list.append(replace)
        else:
            copy_list.append(my_list[number])
    return copy_list
