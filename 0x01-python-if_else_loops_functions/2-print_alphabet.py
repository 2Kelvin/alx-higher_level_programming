#!/usr/bin/python3
# ASCII code for small letters => 97 - 122
for letter in range(97, 123):
    # chr() converts ascii number to the respective alphabet
    # end="" replaces print's newline with nothing
    print("{}".format(chr(letter)), end="")
