# -*- coding: utf-8 -*-

TEST_INPUT_ONE = (2, 3, 9, 16, 'craig')


def test_queue_init():
    from queue import Queue
    new_queue = Queue((TEST_INPUT_ONE))
    assert new_queue.queue.head.data == 'craig'


def test_enqueue():
    from queue import Queue
    new_queue = Queue((TEST_INPUT_ONE))
    new_queue.enqueue(89)
    assert new_queue.queue.head.data == 89

def test_dequeue():
    from queue import Queue
    new_queue = Queue((TEST_INPUT_ONE))
    assert new_queue.dequeue() == 2

def test_size():
    from queue import Queue
    new_queue = Queue((TEST_INPUT_ONE))
    assert new_queue.size() == 5

def test_peek():
    from queue import Queue
    new_queue = Queue((TEST_INPUT_ONE))
    assert new_queue.peek() == 2
