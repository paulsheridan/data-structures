# -*- coding: utf-8 -*-
import pytest


TUP_INPUT = (3, 4, 5)
LIST_INPUT = [6, 7, 8, 9]


def test_empty_node_init():
    from linked_list import Node
    empty_node = Node()
    assert empty_node.next_node is None


def test_linked_node_init_next():
    from linked_list import Node
    empty_node = Node()
    linked_node = Node(12, empty_node)
    assert linked_node.next_node == empty_node


def test_linked_node_init_data():
    from linked_list import Node
    empty_node = Node()
    linked_node_two = Node(12, empty_node)
    assert linked_node_two.data == 12


def test_new_list_init_none():
    from linked_list import LinkedList
    new_list = LinkedList()
    assert new_list.head is None


def test_new_list_init_values():
    from linked_list import LinkedList
    new_list = LinkedList(TUP_INPUT)
    assert new_list is not None


def test_insert():
    from linked_list import LinkedList
    new_list = LinkedList()
    new_list.insert(45)
    assert new_list.head.data == 45


def test_search():
    from linked_list import LinkedList
    new_list = LinkedList(TUP_INPUT)
    assert new_list.search(4) == 4


def test_search_none():
    from linked_list import LinkedList
    new_list = LinkedList(TUP_INPUT)
    assert new_list.search(8) is None


def test_pop():
    from linked_list import LinkedList
    new_list = LinkedList(LIST_INPUT)
    assert new_list.pop() == 9


def test_size():
    from linked_list import LinkedList
    new_list = LinkedList(LIST_INPUT)
    assert new_list.size() == 4


def test_remove():
    from linked_list import LinkedList
    new_list = LinkedList(LIST_INPUT)
    new_list.remove(9)
    assert new_list.head.data == 8


def test_display():
    from linked_list import LinkedList
    new_list = LinkedList(LIST_INPUT)
    assert new_list.display() == (6, 7, 8, 9)
