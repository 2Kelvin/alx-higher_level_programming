#!/usr/bin/python3
def remove_char_at(str, n):
    strCopy = ""
    strlen = len(str)
    for nc in range(strlen):
        if nc != n:
            strCopy = strCopy + str[nc]
    return strCopy
