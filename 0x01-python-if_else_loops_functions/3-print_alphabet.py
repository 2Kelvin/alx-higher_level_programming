#!/usr/bin/python3
for alphaOk in range(97, 123):
    if alphaOk == 101 or alphaOk == 113:
        continue
    else:
        print("{}".format(chr(alphaOk)), end='')
