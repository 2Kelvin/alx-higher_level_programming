#!/usr/bin/python3
"""Contains class Rectangle"""


class Rectangle():
    """Defines a rectangle
    Args:
        width: rectangle's width
        height: rectangle's height

    Raises:
        TypeError: width & height must be an integer
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets private instance attribute width"""
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets private instance attribute height"""
        if (type(value) != int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle
        Returns: The area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """Calculates the rectangle's perimeter
        Returns: rectangle's perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)
