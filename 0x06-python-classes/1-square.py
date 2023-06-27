#!/usr/bin/python3
"""A class Square that defines square instances"""


class Square:
    """Instantiate square with private attribute size
    Args:
        size: size of one side of the square
    """

    def __init__(self, size):
        self.__size = size
