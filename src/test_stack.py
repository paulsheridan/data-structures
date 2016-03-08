# -*- coding: utf-8 -*-

import pytest

TEST_INPUT_ONE = (2, 3, 9, 16)
TEST_INPUT_TWO = (9, 8, 7)


def test_stack_init():
    from stack import Stack
    new_stack = Stack((TEST_INPUT_ONE))
    assert new_stack.stack.head.data == 16


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
