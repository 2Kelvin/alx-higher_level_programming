#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listCopy = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return listCopy
    for i in range(len(my_list)):
        if i == idx:
            listCopy[i] = element
    return listCopy
