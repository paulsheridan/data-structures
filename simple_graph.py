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

    def node():
        node_list = []
        for key in self.node_map:
            node_list.append(key)
        return node_list

    def edges():
        edge_list = []
        for key, value in self.node_map:
            for item in value
                edge_list.append((key,value))
        return edge_list

    def add_edge(node1, node2):
        if node2 not in self.node_map:
            self.node_map[node2] = []
        if node1 not in self.node_map:
            self.node_map[node1] = [node2]
        else:
            self.node_map[node1] += [node2]

    def del_edge(node1, node2):
        self.node_map[node1].remove(node2)

    def has_node(node):
        if node in self.node_map:
            return True
        else:
            return False

    def neighbors(node):
        return self.node_map[node]

    def adjecent(node1, node2):
        try:
            if node2 in node1.value:
                return True
            else:
                return False
        except KeyError:
            Print "Failed"





