# -*- coding: utf-8 -*-
"""Test module for double linked list."""
import pytest


TUP_INPUT = (3, 4, 5)


LIST_INPUT = [6, 7, 8, 9]


def test_prev_node_init():
    from linked_list import Node
    node = Node()
    assert node.next_node is None and node.prev_node is None


def test_linked_node_init_next():
    from linked_list import Node
    next_test_node = Node()
    prev_test_node = Node()
    linked_node = Node(12, next_test_node, prev_test_node)
    assert linked_node.next_node == next_test_node and linked_node.prev_node == prev_test_node


def test_insert():
    from linked_list import Node
    new_list = linked_list()
    new_list.insert(45)
    assert new_list.head.data == 45
