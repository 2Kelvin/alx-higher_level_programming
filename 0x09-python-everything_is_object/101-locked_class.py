#!/usr/bin/python3
"""Contains LockedClass"""


class LockedClass():
    """
    A locked class

    It only allows one instance attribute to be created: 'first_name'
    """
    __slots__ = ["first_name"]
