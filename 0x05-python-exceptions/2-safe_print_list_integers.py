#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        y = 0
        for i in range(x):
            if type(my_list[i]) == int:
                y += 1
                print("{:d}".format(my_list[i]), end="")

        print()
        return y
    except TypeError:
        x = 0
        for m in my_list:
            x += 1
