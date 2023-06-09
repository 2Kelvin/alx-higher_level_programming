#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    args = len(sys.argv) - 1
    if args == 3:
        a = int(sys.argv[1])
        op = sys.argv[2]
        b = int(sys.argv[3])
        if op == '+':
            print(f"{a:d} + {b:d} = {add(a, b):d}")
            sys.exit(0)
        elif op == '-':
            print(f"{a:d} - {b:d} = {sub(a, b):d}")
            sys.exit(0)
        elif op == '*':
            print(f"{a:d} * {b:d} = {mul(a, b):d}")
            sys.exit(0)
        elif op == '/':
            print(f"{a:d} / {b:d} = {div(a, b):d}")
            sys.exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
