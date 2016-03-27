from stack import Stack
from simple_graph import Graph


# implementation with the least amount of typing
def graph_path(graph, start, finish):
    path = graph.depth_first_traverse(start)
    if finish in path:
        return True
    else:
        return False


# faster implementation, modifying depth_first
def depth_based_path(graph, start, finish):
    stack = Stack()
    node = start
    stack.push(node)
    try:
        while True:
            node = stack.pop()
            if node != finish:
                for item in graph.node_map[node]:
                    stack.push(item)
                continue
            else:
                return True
    except (AttributeError, IndexError):
        return False
