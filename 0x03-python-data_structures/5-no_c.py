#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        if i < len(my_string):
            if my_string[i] == "c" or my_string[i] == "C":
                noC = my_string[:i] + my_string[(i + 1):]
    return noC
