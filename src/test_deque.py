# -*- coding: utf-8 -*-
import pytest

TEST_INPUT = [34, "Frank", "Facts", 42, True]
ONE_INPUT = [5]


def test_append():
    from deque import Deque
    new_deque = Deque(TEST_INPUT)
    new_deque.append(989)
    assert new_deque.deque.tail.data == 989


def test_append_left():
    from deque import Deque
    new_deque = Deque(TEST_INPUT)
    new_deque.append_left("989")
    assert new_deque.deque.head.data == "989"


def test_pop():
    from deque import Deque
    new_deque = Deque(TEST_INPUT)
    assert new_deque.pop() is True


def test_pop_empty():
    from deque import Deque
    new_deque = Deque()
    with pytest.raises(IndexError):
        new_deque.pop()


def test_pop_left_empty():
    from deque import Deque
    new_deque = Deque()
    with pytest.raises(IndexError):
        new_deque.pop_left()


def test_pop_left():
    from deque import Deque
    new_deque = Deque(TEST_INPUT)
    assert new_deque.pop_left() == 34


def test_peek():
    from deque import Deque
    new_deque = Deque(TEST_INPUT)
    assert new_deque.peek_left() == 34


def test_peek_left():
    from deque import Deque
    new_deque = Deque(TEST_INPUT)
    assert new_deque.peek() is True


def test_size():
    from deque import Deque
    new_deque = Deque(TEST_INPUT)
    assert new_deque.size() == 5
