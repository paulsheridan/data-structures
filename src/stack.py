# -*- coding: utf-8 -*-

from linked_list import LinkedList


class Stack(object):
    '''Stack is a composition of LinkedList'''

    def __init__(self, val=None):
        self.stack = LinkedList(val)

    def pop(self):
        pop_val = self.stack.pop()
        return(pop_val)

    def push(self, val):
        self.stack.insert(val)
