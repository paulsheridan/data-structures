# -*- coding: utf-8 -*-

class Node(object):
    """Node Object"""
    def __init__(self, val=None):
        self.val = val


class Graph(object):
    "Create a simple Graph."
    def __init__(self):
        self.node_map = {}

    def add_node(val):
        new_node = Node(val)
        self.node_map[new_node] = []

    def del_node(node):
        self.node_map.pop(node)


    




