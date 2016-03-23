# -*- coding: utf-8 -*-
import pytest

VAL_LIST = [10, "person", 'graphs', 'are', 'boring', 77, 'steam', 6.66778]
PAIR_LIST = [(10, "person"),
             ('graphs', 'are'),
             ('boring', 77),
             ('steam', 6.66778)]
MAP_LIST = [(10, "person"), (10, 'are'), (10, 77), (10, 6.66778)]

GRAPH = {1: [2, 3], 2: [4, 5, 6], 3: [7, 8],
         4: [], 5: [], 6: [], 7: [6], 8: []}
GRAPH_LIST = [[{1: []}, [1], [1]],
              [{1: [1]}, [1], [1]],
              [{1: [2], 2: []}, [1, 2], [1, 2]],
              [{1: [2], 2: [1]}, [1, 2], [1, 2]],
              [{1: [2], 2: [3], 3: [1]}, [1, 2, 3], [1, 2, 3]],
              [{1: [2, 3], 2: [], 3: []}, [1, 2, 3], [1, 2, 3]],
              [{1: [2, 3], 2: [3], 3: []}, [1, 2, 3], [1, 2, 3]],
              [{1: [2, 3], 2: [4, 5, 6],
                3: [7, 8], 4: [], 5: [], 6: [], 7: [6], 8: []},
              [1, 2, 4, 5, 6, 3, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]]]


@pytest.mark.parametrize('value', VAL_LIST)
def test_add_node(value):
    from simple_graph import Graph
    new_graph = Graph()
    new_graph.add_node(value)
    assert len(new_graph.node_map) > 0


@pytest.mark.parametrize('value', VAL_LIST)
def test_del_node(value):
    from simple_graph import Graph
    new_graph = Graph()
    new_graph.add_node(value)
    new_graph.del_node(value)
    assert value not in new_graph.node_map


@pytest.mark.parametrize('value', VAL_LIST)
def test_node(value):
    from simple_graph import Graph
    new_graph = Graph()
    new_graph.add_node(value)
    assert value in new_graph.node()


@pytest.mark.parametrize('key, value', PAIR_LIST)
def test_add_edge(key, value):
    from simple_graph import Graph
    new_graph = Graph()
    new_graph.add_edge(key, value)
    assert new_graph.node_map[key][0] == value


@pytest.mark.parametrize('key, value', PAIR_LIST)
def test_edges(key, value):
    from simple_graph import Graph
    new_graph = Graph()
    new_graph.add_node(value)


@pytest.mark.parametrize('key, value', PAIR_LIST)
def test_del_edge(key, value):
    from simple_graph import Graph
    new_graph = Graph()
    new_graph.add_edge(key, value)
    new_graph.del_edge(key, value)
    assert value not in new_graph.node_map[key]


@pytest.mark.parametrize('value', VAL_LIST)
def test_has_node(value):
    from simple_graph import Graph
    new_graph = Graph()
    new_graph.add_node(value)
    assert new_graph.has_node(value) is not False


def test_neighbors():
    from simple_graph import Graph
    new_graph = Graph()
    for pair in MAP_LIST:
        new_graph.add_edge(pair[0], pair[1])
    assert new_graph.neighbors(10) == ["person", 'are', 77, 6.66778]


@pytest.mark.parametrize('key, value', PAIR_LIST)
def test_adjacent(key, value):
    from simple_graph import Graph
    new_graph = Graph()
    node1 = new_graph.add_node(key)
    node2 = new_graph.add_node(value)
    new_graph.add_edge(node1, node2)
    assert new_graph.adjacent(node1, node2) is True


def test_depth_first_traverse():
    from simple_graph import Graph
    new_graph = Graph()
    new_graph.node_map = GRAPH
    assert new_graph.depth_first_traverse(1) == [1, 2, 4, 5, 6, 3, 7, 8]


def test_breadth_first_traverse():
    from simple_graph import Graph
    new_graph = Graph()
    new_graph.node_map = GRAPH
    assert new_graph.breadth_first_traverse(1) == [1, 2, 3, 4, 5, 6, 7, 8]


@pytest.mark.parametrize('input_dict, depth_output, breadth_output',
                         GRAPH_LIST)
def test_depth_traversal_param(input_dict, depth_output, breadth_output):
    from simple_graph import Graph
    new_graph = Graph()
    new_graph.node_map = input_dict
    assert new_graph.depth_first_traverse(1) == depth_output


@pytest.mark.parametrize('input_dict, depth_output, breadth_output',
                         GRAPH_LIST)
def test_breadth_traversal_param(input_dict, depth_output, breadth_output):
    from simple_graph import Graph
    new_graph = Graph()
    new_graph.node_map = input_dict
    assert new_graph.breadth_first_traverse(1) == breadth_output
