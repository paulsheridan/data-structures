# -*- coding: utf-8 -*-
"""Test module for double linked list."""
import pytest


TUP_INPUT = (3, 4, 5)
LIST_INPUT = [6, 7, 8, 9]


def test_toward_head_init():
    from double_linked import Node
    node = Node()
    assert node.toward_tail is None and node.toward_head is None


def test_empty_double_linked():
    from double_linked import DoubleLinkedList
    new_list = DoubleLinkedList()
    new_list.insert(999)
    assert new_list.shift() == 999


def test_linked_node_init_next():
    from double_linked import DoubleLinkedList
    new_list = DoubleLinkedList((3, 4, 5))
    assert new_list.head.toward_tail.data == 4


def test_insert_int():
    from double_linked import DoubleLinkedList
    new_list = DoubleLinkedList((4, 5, 65))
    new_list.insert(45)
    assert new_list.head.data == 45


def test_insert_str():
    from double_linked import DoubleLinkedList
    new_list = DoubleLinkedList((4, 5, 65))
    new_list.insert('dog')
    assert new_list.head.data == 'dog'


def test_append_int():
    from double_linked import DoubleLinkedList
    new_list = DoubleLinkedList((4, 5, 65))
    new_list.append(45)
    assert new_list.tail.data == 45


def test_append_list():
    from double_linked import DoubleLinkedList
    new_list = DoubleLinkedList((4, 5, 65))
    new_list.append([45, 'nine', False])
    assert new_list.tail.data == [45, 'nine', False]


def test_pop():
    from double_linked import DoubleLinkedList
    new_list = DoubleLinkedList(LIST_INPUT)
    new_list.pop()
    assert new_list.pop() == 8


def test_shift():
    from double_linked import DoubleLinkedList
    new_list = DoubleLinkedList(LIST_INPUT)
    assert new_list.shift() == 6


def test_remove():
    from double_linked import DoubleLinkedList
    new_list = DoubleLinkedList(LIST_INPUT)
    new_list.remove(9)
    new_list.remove(7)
    assert new_list.head.data == 8


def test_remove_error():
    from double_linked import DoubleLinkedList
    new_list = DoubleLinkedList(LIST_INPUT)
    with pytest.raises(ValueError):
        new_list.remove('eight')
