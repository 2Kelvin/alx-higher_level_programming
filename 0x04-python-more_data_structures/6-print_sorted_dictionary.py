#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortDict = dict(sorted(a_dictionary.items()))
    for dKey, dValue in sortDict.items():
        print(f"{dKey}: {dValue}")
