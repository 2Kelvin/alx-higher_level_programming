#!/usr/bin/python3
"""Square class that creates square instances"""


class Square:
    """instantiating a square object
    Attributes:
        size: one square side

    Raises:
        TypeError: if size passed in is not an int or position is negative
        ValueError: if the size is less than 0
    """

    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Position private attribute getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """Private position tuple attribute setter
        Args:
            value: new positon tuple

        Raises:
            TypeError: tuple of positive integers only
        """
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square in #"""
        if self.__size == 0:
            print()
        else:
            for sp in range(self.__position[1]):
                print()
            for sqRow in range(self.__size):
                for p in range(self.__position[0]):
                    print(end=" ")
                for sqCol in range(self.__size):
                    print("#", end="")
                print()
