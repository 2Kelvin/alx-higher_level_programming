#!/usr/bin/python3
for al in range(123, 96, -1):
    if al % 2 == 0:
        print(chr(al), end="")
    elif al % 2 != 0:
        al = al - 32
        print(chr(al), end="")
