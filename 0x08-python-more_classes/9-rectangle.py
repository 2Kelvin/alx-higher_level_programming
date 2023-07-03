#!/USR/BIn/python3
"""Contains class Rectangle"""


class Rectangle():
    """Defines a rectangle
    Args:
        width: rectangle's width
        height: rectangle's height

    Raises:
        TypeError: width & height must be an integer
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Draw a rectangle
        Returns: a '#' rectangle or an empty string
        """
        if self.width == 0 or self.height == 0:
            return ""
        hashRect = ""
        for h in range(self.height):
            for w in range(self.width):
                hashRect += str(self.print_symbol)
            if h < self.height - 1:
                hashRect += "\n"
        return hashRect

    def __repr__(self):
        """Returns a string representation of a rectangle"""
        return f"Rectangle({(self.width):d}, {(self.height):d})"

    def __del__(self):
        """Prints 'bye rectangle' when a rectangle object is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns rectangle with the biggest area
        Args:
            rect_1: rectangle 1
            rect_2: rectangle 2

        Raises:
            TypeError: rect_1 & rect_2 must be instances of Rectangle

        Returns: rectangle with the biggest area or rect_1 if equal
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Create new rectangle 'square', width = height
        Args:
            cls: a rectangle class
            size: sets width & height the same

        Returns: new rectangle 'square' instance
        """
        return Rectangle(size, size)
