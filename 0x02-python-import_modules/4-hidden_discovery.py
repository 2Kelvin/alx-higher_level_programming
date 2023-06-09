#!/usr/bin/python3
import hidden_4
if __names__ == "__main__":
    attrs = dir(hidden_4)
    for a in attrs:
        if not a.startswith("__"):
            print(a)
