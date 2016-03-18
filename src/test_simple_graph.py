# -*- coding: utf-8 -*-
import pytest


VAL_LIST = [10, "person", 'graphs', 'are', 'boring', 77, 'steam', 6.66778]
PAIR_LIST = [(10, "person"), ('graphs', 'are'), ('boring', 77), ('steam', 6.66778)]
MAP_LIST = [(10, "person"), (10, 'are'), (10, 77), (10, 6.66778)]


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
    test_node = new_graph.add_node(value)
    new_graph.del_node(test_node)
    assert test_node not in new_graph.node_map


@pytest.mark.parametrize('value', VAL_LIST)
def test_node(value):
    from simple_graph import Graph
    new_graph = Graph()
    new_graph.add_node(value)
    return_list = new_graph.node()
    assert return_list[0].val == value


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
    test_node = new_graph.add_node(value)
    assert new_graph.has_node(test_node) is not False


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
