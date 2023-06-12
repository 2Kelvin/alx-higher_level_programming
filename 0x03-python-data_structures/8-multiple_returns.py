#!/usr/bin/python3
def multiple_returns(sentence):
    lst = []
    if sentence != "":
        lst.append(len(sentence))
        lst.append(sentence[0])
        return tuple(lst)
    else:
        lst.append(0)
        lst.append(None)
        return tuple(lst)
