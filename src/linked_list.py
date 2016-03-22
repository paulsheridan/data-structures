# -*- coding: utf-8 -*-


class Node(object):
    """Node class"""
    def __init__(self, data=None):
        self.data = data
        self.toward_tail = None


class LinkedList(object):
    def __init__(self, user_input=None):
        self.head = None
        if user_input is not None:
            try:
                [self.insert(x) for x in user_input]
            except TypeError:
                print('input is not an iterable')

    def insert(self, val):
        new_node = Node(val)
        new_node.toward_tail = self.head
        self.head = new_node

    def search(self, val):
        current = self.head
        found = False
        while current and found is False:
            if current.data == val:
                found = True
                return val
            else:
                current = current.toward_tail
        else:
            return None

    def pop(self):
        return_val = self.head.data
        self.head = self.head.toward_tail
        return return_val

    def size(self):
        size = 0
        current_spot = self.head
        while current_spot:
            size += 1
            current_spot = current_spot.toward_tail
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
                current = current.toward_tail
        if current is None:
            print('The specified value is not in the list')
        if previous is None:
            self.head = current.toward_tail
        else:
            previous.set_next = current.toward_tail

    def display(self):
        display_list = []
        current = self.head
        while current:
            display_list.append(current.data)
            current = current.toward_tail
        return tuple(reversed(display_list))
