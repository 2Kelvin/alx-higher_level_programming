#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m in matrix:
        for e in m:
            if e == m[-1]:
                print("{:d}".format(e), end="")
            else:
                print("{:d}".format(e), end=" ")
        print()
