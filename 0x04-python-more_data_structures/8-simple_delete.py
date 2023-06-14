#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if type(key) != str:
        return a_dictionary
    a_keys = list(a_dictionary.keys())
    for k in a_keys:
        if k == key:
            del a_dictionary[key]
    return a_dictionary
