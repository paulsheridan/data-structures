# -*- coding: utf-8 -*-
from stack import Stack
from queue import Queue
from math import inf
import heapq


class Graph(object):
    "Create a simple Graph."
    def __init__(self):
        self.node_map = {}

    def add_node(self, node):
        self.node_map[node] = {}

    def del_node(self, node):
        self.node_map.pop(node)
        for key in self.node_map:
            if node in key:
                self.node_map[key].pop(node, None)

    def node(self):
        node_list = []
        for key in self.node_map:
            node_list.append(key)
        return node_list

    def edges(self):
        edge_list = []
        for key in self.node_map:
            for item in self.node_map[key]:
                edge_list.append({(key, item): self.node_map[key][item]})
        return edge_list

    def add_edge(self, node1, node2):
        if node2 not in self.node_map:
            self.node_map[node2] = {}
        if node1 not in self.node_map:
            self.node_map[node1] = {}
        if node2 not in self.node_map[node1]:
            self.node_map[node1][node2] = 1
        else:
            self.node_map[node1][node2] += 1

    def del_edge(self, node1, node2):
        self.node_map[node1][node2] -= 1

    def has_node(self, node):
        if node in self.node_map:
            return True
        else:
            return False

    def neighbors(self, node):
        neighbors_list = []
        for key in self.node_map[node]:
            neighbors_list.append(key)
            print(neighbors_list)
        return neighbors_list

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
        stack = Stack()
        path = []
        stack.push(node)
        try:
            while True:
                node = stack.pop()
                if node not in path:
                    path = path + [node]
                    for item in self.node_map[node]:
                        stack.push(item)
        except (AttributeError, IndexError):
            return path

    def breadth_first_traverse(self, node):
        queue = Queue()
        path = []
        queue.enqueue(node)
        try:
            while True:
                node = queue.dequeue()
                if node not in path:
                    path = path + [node]
                    for item in self.node_map[node]:
                        queue.enqueue(item)
        except (AttributeError, IndexError):
            return path


    def shortest_dist(dist):
    distance = inf
    best = None
    for vertex in dist:
        if dist[vertex] < best:
            (distance, best) = (vertex, dist[vertex])
    return best_node


    def dijkstra(self, source):
        path_dist = {}
        path_dist[vertex] = 0
        final_dist = {}
        while True:
            shortest = shortest_dist(path_dist)
            final_dist[shortest] = path_dist[shortest]
            for item in self.graph[shortest]:
                if item not in final_dist:
                    if item not in path_dist:
                        path_dist[shortest] = final_dist[shortest] + self.graph[item][shortest]
                    elif final_dist[shortest] + self.graph[item][shortest] < path_dist[shortest]:
                        path_dist[shortest] = final_dist[shortest] + self.graph[item][shortest]
        return final_dist



if __name__ == '__main__':
    new_graph = Graph()
    new_graph.node_map = {1: [2, 3], 2: [4, 5, 6],
                          3: [7, 8], 4: [], 5: [],
                          6: [], 7: [6], 8: []}
    print('*** A sample graph traversed breadth-first. ***')
    new_graph.breadth_first_traverse()
    print('*** That same graph traversed depth-first. ***')
    new_graph.depth_first_traverse()
