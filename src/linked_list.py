# -*- coding: utf-8 -*-


class Node(object):
    """Node class"""
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def set_next(self, next_node):
        self.next_node = next_node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        if self.head is not None:
            try:
                itbl = iter(self.head)
                self.head = None
                [self.insert(x) for x in itbl]
            except TypeError:
                print('input is not an iterable')

    def insert(self, val):
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node

    def search(self, val):
        current = self.head
        found = False
        while current and found is False:
            if current.data == val:
                found = True
                return val
            else:
                current = current.next_node
        else:
            return None

    def pop(self):
        return_val = self.head.data
        self.head = self.head.next_node
        return return_val

    def size(self):
        size = 0
        current_spot = self.head
        while current_spot:
            size += 1
            current_spot = current_spot.next_node
        return size

    def remove(self, val):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.data == val:
                found = True
            else:
                previous = current
                current = current.next_node
        if current is None:
            print('The specified value is not in the list')
        if previous is None:
            self.head = current.next_node
        else:
            previous.set_next = current.next_node

    def display(self):
        display_list = []
        current = self.head
        while current:
            display_list.append(current.data)
            current = current.next_node
        return tuple(reversed(display_list))
