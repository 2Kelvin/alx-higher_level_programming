#!/usr/bin/python3
"""Class Node and SinglyLinkedList"""


class Node:
    """Initializing a node instance
    Attributes:
        data: node data
        next_node: next node element in the singly linked list
    Raises:
        TypeError: if data not an integer & there's no node object next
    """
    def __init__(self, data, next_node=None):
        if type(data) != int:
            raise TypeError("data must be an integer")
        if next_node is not None or type(next_node) != Node:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if self.__next_node is not None or type(self.__next_node) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Instantiate a singly linked list
    Attributes:
        head: singly linked list head node
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
