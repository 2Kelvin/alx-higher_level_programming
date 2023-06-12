#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m in matrix:
        for e in m:
            if e == 3 or e == 6 or e == 9:
                print("{:d}".format(e), end="")
            else:
                print("{:d}".format(e), end=" ")
        print()
