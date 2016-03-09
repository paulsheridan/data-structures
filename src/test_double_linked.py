# -*- coding: utf-8 -*-
"""Test module for double linked list."""
import pytest


TUP_INPUT = (3, 4, 5)
LIST_INPUT = [6, 7, 8, 9]



def test_prev_node_init():
    from double_linked import Dbl_Node
    node = Dbl_Node()
    assert node.next_node is None and node.prev_node is None


# @pytest.fixture(scope='function')
def test_linked_node_init_next():
    from double_linked import DoubleLinkedList
    new_list = DoubleLinkedList((3, 4, 5))
    assert new_list.head.next_node.data == 4


def test_insert():
    from double_linked import DoubleLinkedList
    new_list = DoubleLinkedList((4, 5, 65))
    new_list.insert(45)
    assert new_list.head.data == 45


def test_append():
    from double_linked import DoubleLinkedList
    new_list = DoubleLinkedList((4, 5, 65))
    new_list.append(45)
    assert new_list.tail.data == 45


def test_pop():
    from linked_list import LinkedList
    new_list = LinkedList(LIST_INPUT)
    assert new_list.pop() == 9
