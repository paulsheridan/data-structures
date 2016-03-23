# -*- coding: utf-8 -*-
import pytest

VAL_LIST = [10, "person", 'graphs', 'are', 'boring', 77, 'steam', 6.66778]
PAIR_LIST = [(10, "person"),
             ('graphs', 'are'),
             ('boring', 77),
             ('steam', 6.66778)]
MAP_LIST = [(10, "person"), (10, 'are'), (10, 77), (10, 6.66778)]

GRAPH_LIST = [[{1: {}}, [1], [1]],
              [{1: {1: 3}}, [1], [1]],
              [{1: {2: 3}, 2: {}}, [1, 2], [1, 2]],
              [{1: {2: 3}, 2: {1: 45}}, [1, 2], [1, 2]],
              [{1: {2: 3}, 2: {3: 9}, 3: {1: 9}}, [1, 2, 3], [1, 2, 3]],
              [{1: {2: 2, 3: 2}, 2: {}, 3: {}}, [1, 2, 3], [1, 2, 3]],
              [{1: {2: 2, 3: 2}, 2: {3: 14}, 3: {}}, [1, 2, 3], [1, 2, 3]],
              [{1: {2: 2, 3: 2}, 2: {4: 6, 5: 6, 6: 6},
                3: {7: 2, 8: 2}, 4: {}, 5: {}, 6: {}, 7: {6: 1}, 8: {}},
              [1, 2, 4, 5, 6, 3, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]],
              [{1: {2: 1, 3: 5}, 2: {4: 3, 5: 3, 6: 3}, 3: {7: 2, 8: 2},
                4: {}, 5: {}, 6: {}, 7: {6: 22}, 8: {}},
               [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 4, 5, 6, 3, 7, 8]]]


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
    assert new_graph.node_map[key][value] == 1


@pytest.mark.parametrize('key, value', PAIR_LIST)
def test_edges(key, value):
    from simple_graph import Graph
    new_graph = Graph()
    new_graph.add_edge(key, value)
    assert new_graph.edges() == [{(key, value): 1}]


def test_multiple_edges():
    from simple_graph import Graph
    new_graph = Graph()
    for pair in PAIR_LIST:
        new_graph.add_edge(pair[0], pair[1])
    for pair in PAIR_LIST:
        assert {(pair[0], pair[1]): 1} in new_graph.edges()


@pytest.mark.parametrize('key, value', PAIR_LIST)
def test_del_edge(key, value):
    from simple_graph import Graph
    new_graph = Graph()
    new_graph.add_edge(key, value)
    new_graph.del_edge(key, value)
    assert new_graph.node_map[key][value] == 0


@pytest.mark.parametrize('value', VAL_LIST)
def test_has_node(value):
    from simple_graph import Graph
    new_graph = Graph()
    new_graph.add_node(value)
    assert new_graph.has_node(value) is not False


def test_neighbors():
    output = ["person", 'are', 77, 6.66778]
    from simple_graph import Graph
    new_graph = Graph()
    for pair in MAP_LIST:
        new_graph.add_edge(pair[0], pair[1])
    for item in output:
        assert item in new_graph.neighbors(10)


@pytest.mark.parametrize('key, value', PAIR_LIST)
def test_adjacent(key, value):
    from simple_graph import Graph
    new_graph = Graph()
    node1 = new_graph.add_node(key)
    node2 = new_graph.add_node(value)
    new_graph.add_edge(node1, node2)
    assert new_graph.adjacent(node1, node2) is True


@pytest.mark.parametrize('input_dict, depth_output, breadth_output',
                         GRAPH_LIST)
def test_depth_traversal_param(input_dict, depth_output, breadth_output):
    from simple_graph import Graph
    new_graph = Graph()
    new_graph.node_map = input_dict
    output = new_graph.depth_first_traverse(1)
    assert set(output) - set(depth_output) == set()


@pytest.mark.parametrize('input_dict, depth_output, breadth_output',
                         GRAPH_LIST)
def test_breadth_traversal_param(input_dict, depth_output, breadth_output):
    from simple_graph import Graph
    new_graph = Graph()
    new_graph.node_map = input_dict
    output = new_graph.breadth_first_traverse(1)
    assert set(output) - set(breadth_output) == set()
