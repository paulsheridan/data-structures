# -*- coding: utf-8 -*-

import linked_list


class Stack(object):

    def __init__(self, init_val):
        self.stack = linked_list.LinkedList(init_val)

    def pop(self):
        pop_val = self.stack.pop()
        return(pop_val)

    def push(self, val):
        self.stack.insert(val)
