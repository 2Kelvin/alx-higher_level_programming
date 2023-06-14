#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiDict = []
    for dkey, dvalue in a_dictionary.items():
        pairTup = (dkey, dvalue * 2)
        multiDict.append(pairTup)
    return dict(multiDict)
