# -*- coding: utf-8 -*-


class Node(object):
    """Node class."""

    def __init__(self, data=None):
        """Init node with optional argument data"""
        self.data = data
        self.toward_tail = None
        self.toward_head = None


class DoubleLinkedList(object):
    """Class for doube linked list."""
    def __init__(self, user_input=None):
        self.head = None
        self.tail = None
        if user_input is not None:
            try:
                [self.insert(x) for x in user_input]
            except TypeError:
                print('input is not an iterable')

    def insert(self, val):
        new_node = Node(val)
        if self.head is not None:
            new_node.toward_tail = self.head
            self.head.toward_head = new_node
            self.head = new_node
        else:
            self.head = self.tail = new_node

    def append(self, val):
        new_node = Node(val)
        if self.tail is not None:
            new_node.toward_head = self.tail
            self.tail.toward_tail = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node

    def pop(self):
        if not self.head:
            raise IndexError('list is empty')
        else:
            head_val = self.head.data
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.toward_tail
                self.head.toward_head = None
            return head_val

    def shift(self):
        if not self.tail:
            raise IndexError('list is empty')
        else:
            tail_val = self.tail.data
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.toward_head
                self.tail.toward_tail = None
            return tail_val

    def remove(self, val):
        current = self.head
        found = False
        while current and found is False:
            if current.data == val:
                found = True
                if current.toward_tail is None:
                    self.shift()
                elif current.toward_head is None:
                    self.pop()
                else:
                    current.toward_head.toward_tail = current.toward_tail
                    current.toward_tail.toward_head = current.toward_head
            else:
                current = current.toward_tail
        if current is None:
            raise ValueError('item not in list')

    def _size(self):
        size = 0
        current_spot = self.head
        while current_spot:
            size += 1
            current_spot = current_spot.toward_tail
        return size
