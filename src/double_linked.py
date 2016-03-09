# -*- coding: utf-8 -*-
"""Module for double linked list."""


class Node(object):
    """Node class."""

    def __init__(self, data=None, next_node=None, prev_node=None):
        """__init__ function."""
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def set_next(self, next_node):
        self.next_node = next_node
