# -*- coding: utf-8 -*-

TEST_INPUT_ONE = (2, 3, 9, 16, 'craig')
TEST_INPUT_TWO = [2, 3, 4, 5, 6, 7, 8]


def test_queue_init():
    from queue import Queue
    new_queue = Queue((TEST_INPUT_ONE))
    assert new_queue.queue.head.data == 'craig'


def test_enqueue():
    from queue import Queue
    new_queue = Queue((TEST_INPUT_ONE))
    new_queue.enqueue(89)
    assert new_queue.queue.head.data == 89


def test_enqueue_dequeue():
    from queue import Queue
    new_queue = Queue()
    new_queue.enqueue(89)
    assert new_queue.dequeue() == 89


def test_enqueue_dequeue_two():
    from queue import Queue
    new_queue = Queue()
    new_queue.enqueue(1)
    new_queue.dequeue()
    for item in TEST_INPUT_TWO:
        new_queue.enqueue(item)
    for item in TEST_INPUT_TWO:
        assert new_queue.dequeue() == item


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
