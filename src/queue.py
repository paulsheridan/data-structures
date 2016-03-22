# -*- coding: utf-8 -*-

from double_linked import DoubleLinkedList


class Queue(object):
    '''Stack is a composition of LinkedList'''

    def __init__(self, input=None):
        self.queue = DoubleLinkedList(input)

    def enqueue(self, val):
        self.queue.insert(val)

    def dequeue(self):
        shift_val = self.queue.shift()
        return shift_val

    def size(self):
        return self.queue._size()

    def peek(self):
        return self.queue.tail.data
