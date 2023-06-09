#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = 0

    for arg in range(1, len(sys.argv)):
        if len(sys.argv) == 1:
            print(0)
        else:
            res = res + int(sys.argv[arg])
    print(res)
