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
            new_node.toward_head = None
            self.head.toward_head = new_node
            self.head = new_node
        else:
            self.head = self.tail = new_node

    def append(self, val):
        new_node = Node(val)
        if self.head is not None:
            new_node.toward_head = self.tail
            new_node.toward_tail = None
            self.tail.toward_tail = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node

    def pop(self):
        if self.head is not None:
            head_val = self.head.data
            self.head.toward_head = None
            self.head = self.head.toward_tail
            return head_val
        else:
            raise IndexError('list is empty')

    def shift(self):
        if self.tail is not None:
            tail_val = self.tail.data
            self.tail.toward_tail = None
            self.tail = self.tail.toward_head
            return tail_val
        else:
            raise IndexError('list is empty')

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


new_dll = DoubleLinkedList([1, 2, 3, 4, 5, 6, 7])
print(new_dll.pop())
print(new_dll.shift())
print(new_dll.pop())
print(new_dll.shift())
