#!/usr/bin/python3
class Square:
    """Square class that creates square instances"""
    def __init__(self, size=0):
        """A method instantiating a square object from class Square"""
        try:
            if type(size) != int:
                raise TypeError
            elif size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method that returns the current square area"""
        return (self.__size * self__size)
