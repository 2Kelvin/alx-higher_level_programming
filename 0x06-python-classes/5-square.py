#!/usr/bin/python3
"""Square class that creates square instances"""


class Square:
    """instantiating a square object
    Attributes:
        size: one square side

    Raises:
        TypeError: if size passed in is not an int
        ValueError: if the size is less than 0
    """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the square area
        Returns:
            area of the square instance
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """Retrieve private size atrribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the private size attribute
        Args:
            value: new size's value to be set
        Raises:
            TypeError: if value passed in is not an int
            ValueError: if the value is less than 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print the square in #"""
        for sqRow in range(self.__size):
            for sqCol in range(self.__size):
                print("#", end="")
            print()
