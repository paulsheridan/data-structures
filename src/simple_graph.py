# -*- coding: utf-8 -*-
from collections import Counter
from stack import Stack
from queue import Queue


class Node(object):
    """Node Object"""
    def __init__(self, val=None):
        self.val = val


class Graph(object):
    "Create a simple Graph."
    def __init__(self):
        self.node_map = {}

    def add_node(self, val):
        new_node = Node(val)
        self.node_map[new_node] = []
        return new_node

    def del_node(self, node):
        self.node_map.pop(node)

    def node(self):
        node_list = []
        for key in self.node_map:
            node_list.append(key)
        return node_list

    def edges(self):
        edge_list = []
        for key, value in self.node_map:
            for item in value:
                edge_list.append((key, value))
        return edge_list

    def add_edge(self, node1, node2):
        if node2 not in self.node_map:
            self.node_map[node2] = []
        if node1 not in self.node_map:
            self.node_map[node1] = [node2]
        else:
            self.node_map[node1] += [node2]

    def del_edge(self, node1, node2):
        self.node_map[node1].remove(node2)

    def has_node(self, node):
        if node in self.node_map:
            return True
        else:
            return False

    def neighbors(self, node):
        return self.node_map[node]

    def adjacent(self, node1, node2):
        try:
            if node2 in self.node_map[node1]:
                return True
            elif node1 in self.node_map[node2]:
                return True
            else:
                return False
        except KeyError:
            print("One of those nodes doesn't exist.")

    def depth_first_traverse(self, node):
        stack, path = Stack(), []
        stack.push(node)
        try:
            while True:
                node = stack.pop()
                if node not in path:
                    path = path + [node]
                    for item in self.node_map[node]:
                        stack.push(item)
        except KeyError:
            return path

    def breadth_first_traverse(self, node):
        queue, path = Queue(), []
        queue.enqueue(node)
        try:
            while True:
                node = queue.dequeue()
                if node not in path:
                    path = path + [node]
                    for item in self.node_map[node]:
                        queue.enqueue(item)
        except KeyError:
            return path
