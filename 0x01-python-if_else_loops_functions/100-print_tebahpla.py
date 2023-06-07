#!/usr/bin/python3
for al in range(123, 96, -1):
    if al % 2 == 0:
        cs = 0
    elif al % 2 != 0:
        cs = 32
    print("{}".format(chr(al - cs)), end="")
