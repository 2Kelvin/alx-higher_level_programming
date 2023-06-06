#!/usr/bin/python3
# ASCII code for small letters => 97 - 122
# chr() converts ascii number to the respective alphabet
# end="" replaces print's newline with nothing
for alpha in range(97, 123):
    print("{}".format(chr(alpha)), end="")
