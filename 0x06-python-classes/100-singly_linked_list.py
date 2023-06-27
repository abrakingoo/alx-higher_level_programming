#!/usr/bin/python3
"""defines a node of a singly linked list"""


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Instantiation with data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for the data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for the data attribute"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for the next_node attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for the next_node attribute"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Simple instantiation"""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and value >= current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Prints the entire list"""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
