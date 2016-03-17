# When we look up nodes and edges, we need a set and a collection of some sort
# we can store a set with a dictionary
# keys are nodes and their values are other nodes

graph = {'a': ['c', 'd'],
         'b': ['d', 'a'],
         'c': ['b', 'e'],
         'd': ['e'],
         'e': []
         }
 def add_node(graph, n):
     add key to graph dict

def add_edge(graph, n1, n2):
    add connection from n1 to n2
    if not (n1|n2):
         add_node(nX)

def edges(graph):
    return a list of all edges
