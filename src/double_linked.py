# -*- coding: utf-8 -*-
"""Module for double linked list."""

from linked_list import LinkedList


class Node(object):
    """Node class."""

    def __init__(self, data=None, next_node=None, prev_node=None):
        """__init__ function."""
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def set_next(self, next_node):
        self.next_node = next_node


    def set_prev(self, prev_node):
        self.prev_node = prev_node


class DoubleLinkedList(LinkedList):
    """Class for doube linked list."""
    def __init__(self, head=None):
        self.head = head


    def insert(self, val):
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node


    def pop(self):
        return_val = self.head.data
        self.head = self.head.next_node
        self.head.prev_node = None
        return return_val


