import pytest

GRAPH_LIST = [[{1: {2: 3}, 2: {}}, 1, 2, True],
              [{1: {2: 3}, 2: {3: 9}, 3: {1: 9}}, 1, 9, False],
              [{1: {2: 2, 3: 2}, 2: {}, 3: {}}, 1, 3, True],
              [{1: {2: 2, 3: 2}, 2: {4: 6, 5: 6, 6: 6},
                3: {7: 2, 8: 2}, 4: {}, 5: {}, 6: {}, 7:
                {6: 1}, 8: {}, 99: {}}, 1, 99, False],
              [{1: {2: 1, 3: 5}, 2: {4: 3, 5: 3, 6: 3}, 3: {7: 2, 8: 2},
                4: {}, 5: {}, 6: {}, 7: {6: 22}, 8: {}}, 1, 8, True]]


@pytest.mark.parametrize('graph, start, finish, bool',
                         GRAPH_LIST)
def test_depth_traversal_param(graph, start, finish, bool):
    from simple_graph import Graph
    from graphtraverse import graph_path
    new_graph = Graph()
    new_graph.node_map = graph
    assert graph_path(new_graph, start, finish) == bool


@pytest.mark.parametrize('graph, start, finish, bool',
                         GRAPH_LIST)
def test_depth_based_path(graph, start, finish, bool):
    from simple_graph import Graph
    from graphtraverse import depth_based_path
    new_graph = Graph()
    new_graph.node_map = graph
    assert depth_based_path(new_graph, start, finish) == bool
