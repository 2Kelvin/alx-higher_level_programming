#!/usr/bin/python3
def uniq_add(my_list=[]):
    mySet = set(my_list)
    uniqList = list(mySet)
    total = 0
    for n in uniqList:
        total += n
    return total
