# -*- coding: utf-8 -*-

import pytest

TEST_INPUT_ONE = (2, 3, 9, 16)
TEST_INPUT_TWO = (9, 8, 7)
TEST_INPUT_LIST = [[1, 2, 3], [7, 6, 5]]


def test_stack_init():
    from stack import Stack
    new_stack = Stack((TEST_INPUT_ONE))
    assert new_stack.stack.head.data == 16


def test_stack_order():
    from stack import Stack
    new_stack = Stack()
    new_stack.push(12)
    assert new_stack.pop == 12


@pytest.mark.parametrize('input_list', TEST_INPUT_LIST)
def test_push_pop(input_list):
    from stack import Stack
    new_stack = Stack()
    for item in input_list:
        new_stack.push(item)
    for item in reversed(input_list):
        assert new_stack.pop() == item


def test_stack_order():
    from stack import Stack
    new_stack = Stack()
    new_stack.push(12)
    assert new_stack.pop() == 12


def test_stack_pop():
    from stack import Stack
    new_stack = Stack((TEST_INPUT_TWO))
    assert new_stack.pop() == 7


def test_stack_pop_twice():
    from stack import Stack
    new_stack = Stack((TEST_INPUT_TWO))
    new_stack.pop()
    assert new_stack.pop() == 8


def test_stack_push():
    from stack import Stack
    new_stack = Stack((TEST_INPUT_TWO))
    new_stack.push('dog')
    assert new_stack.stack.head.data == 'dog'
