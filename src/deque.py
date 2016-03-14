# -*- coding: utf-8 -*-

from double_linked import DoubleLinkedList


class Deque(object):
    '''Deque is a composition of Double Linked List'''

    def __init__(self, input):
        '''create doubly linked list'''
        self.deque = DoubleLinkedList(input)

    def append(self, val):
        self.deque.append(val)

    def append_left(self, val):
        self.deque.insert(val)

    def pop(self):
        return self.deque.pop()

    def pop_left(self):
        return self.deque.shift()

    def peek(self):
        return self.deque.head.data

    def peek_left(self):
        return self.deque.tail.data

    def size(self):
        size = 0
        current_spot = self.deque.head
        while current_spot:
            size += 1
            current_spot = current_spot.next_node
        return size
