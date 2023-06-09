#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    attrs = dir(hidden_4)
    for n in attrs:
        if not n.startswith("__"):
            print(n)
