#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argC = len(sys.argv)
    if argC == 1:
        print("0 arguments.")
    elif argC == 2:
        print(f"1 argument:\n{argC - 1}: {sys.argv[1]}")
    else:
        print(f"{(argC - 1):d} arguments:")
        for arg in range(1, argC):
            print(f"{arg:d}: {sys.argv[arg]}")
