#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = []
    for n in my_list:
        if n == search:
            newList.append(replace)
        else:
            newList.append(n)
    return newList
