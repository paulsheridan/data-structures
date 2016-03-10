# -*- coding: utf-8 -*-
"""Module for double linked list."""

from linked_list import LinkedList
from linked_list import Node


class Dbl_Node(Node):
    """Node class."""

    def __init__(self, data=None, next_node=None):
        """__init__ function."""
        self.data = data
        self.next_node = next_node
        self.prev_node = None

    def set_next(self, next_node):
        self.next_node = next_node

    def set_prev(self, prev_node):
        self.prev_node = prev_node


class DoubleLinkedList(LinkedList):
    """Class for doube linked list."""

    def __init__(self, input=None):
        self.head = None
        self.tail = None
        if input is not None:
            try:
                [self.insert(x) for x in input]
            except TypeError:
                print('input is not an iterable')

    def insert(self, val):
        new_node = Dbl_Node(val)
        if self.head is not None:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
        else:
            self.tail = new_node
        self.head = new_node

    def pop(self):
        return_val = self.head.data
        self.head = self.head.next_node
        self.head.set_prev(None)
        return return_val

    def append(self, val):
        new_node = Dbl_Node(val)
        if self.tail is not None:
            self.tail.next_node = new_node.prev_node
        else:
            self.head = new_node
        self.tail = new_node

    def shift(self):
        return_val = self.tail.data
        self.tail = self.tail.prev_node
        self.tail.set_next(None)
        return return_val

    def remove(self, val):
        current = self.head
        found = False
        while current and found is False:
            if current.data == val:
                found = True
                if current.next_node is None:
                    self.pop()
                elif current.prev_node is None:
                    self.shift()
                else:
                    current.prev_node.next_node = current.next_node
                    current.next_node.prev_node = current.prev_node
            else:
                current = current.next_node
        if current is None:
            print('The specified value is not in the list')
