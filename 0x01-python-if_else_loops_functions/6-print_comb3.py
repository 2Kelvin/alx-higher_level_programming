#!/usr/bin/python3
for f in range(10):
    for ls in range(10):
        if f != ls and f < ls:
            if f == 8 and ls == 9:
                print(89)
            else:
                print("{0}{1}".format(f, ls), end=", ")
