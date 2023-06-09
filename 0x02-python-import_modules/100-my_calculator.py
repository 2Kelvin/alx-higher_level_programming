#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    args = len(sys.argv) - 1
    if args == 3:
        arg1 = int(sys.argv[1])
        op = sys.argv[2]
        arg2 = int(sys.argv[3])
        if op == '+':
            print(f"{arg1:d} + {arg2:d} = {(add(arg1, arg2):d)}")
            sys.exit(0)
        elif op == '-':
            print(f"{arg1:d} - {arg2:d} = {(sub(arg1, arg2):d)}")
            sys.exit(0)
        elif op == '*':
            print(f"{arg1:d} * {arg2:d} = {(mul(arg1, arg2):d)}")
            sys.exit(0)
        elif op == '/':
            print(f"{arg1:d} / {arg2:d} = {(div(arg1, arg2):d)}")
            sys.exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
	    sys.exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
