#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a_keys = list(a_dictionary)
    for k in a_keys:
        if k == key:
            del a_dictionary[key]
            return a_dictionary
        else:
            return a_dictionary
