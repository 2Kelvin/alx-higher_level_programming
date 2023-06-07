#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return (0.0001)
    else:
        return (a * (pow(a, (b - 1))))
