# -*- coding: utf-8 -*-
import pytest


TEST_LISTS = ([(34, 34), (56, 56), (78, 78), (90, 90), (3, 3), (4, 4), (1, 1), (6, 6)],
              [(34, 34), (56, 56), (78, 78), (90, 90), (9, 9), (24, 24), (20, 20), (3, 3), (4, 4), (1, 1), (6, 6), (29, 29), (66, 66), (5, 5), (4, 4), (8, 8)],
              [(24, 24), (45, 45), (92, 92), (93, 93), (65, 65), (87, 87), (19, 19), (9, 9), (46, 46), (72, 72), (85, 85), (4, 4), (76, 76), (900, 900)],
              [(34, 34), (56, 56), (78, 78), (90, 90), (45, 45), (92, 92), (93, 93), (65, 65), (87, 87), (19, 19), (9, 9), (46, 46), (72, 72), (85, 85), (4, 4), (76, 76), (900, 900)])

TEST_TUP = (([(34, 34), (56, 56), (78, 78), (90, 90), (3, 3), (4, 4), (1, 1), (6, 6)], (99, 99)),
            ([(34, 34), (56, 56), (78, 78), (90, 90), (3, 3), (4, 4), (1, 1), (6, 6)], (445, 445)),
            ([(34, 34), (56, 56), (78, 78), (90, 90), (3, 3), (4, 4), (1, 1), (6, 6)], (1, 1)),
            ([(34, 34), (56, 56), (78, 78), (90, 90), (3, 3), (4, 4), (1, 1), (6, 6)], (2122345, 2122345)),
            ([(34, 34), (56, 56), (78, 78), (90, 90), (3, 3), (4, 4), (1, 1), (6, 6)], (3, 3)),
            ([(34, 34), (56, 56), (78, 78), (90, 90), (3, 3), (4, 4), (1, 1), (6, 6)], (0, 0)))

@pytest.mark.parametrize('test_list', TEST_LISTS)
def test_sift_up(test_list):
    from priorityq import PriorityQueue
    new_queue = PriorityQueue(test_list)
    for idx, item in enumerate(new_queue.queue):
        if idx < (len(new_queue.queue) - 1) // 2:
            assert item > new_queue.queue[idx * 2 + 1]
            assert item > new_queue.queue[idx * 2 + 2]


@pytest.mark.parametrize('test_list', TEST_LISTS)
def test_sift_down(test_list):
    from priorityq import PriorityQueue
    new_queue = PriorityQueue(test_list)
    new_queue.pop()
    print(new_queue.queue)
    for idx, item in enumerate(new_queue.queue):
        if idx < (len(new_queue.queue) - 1) // 2:
            assert item > new_queue.queue[idx * 2 + 1]
            assert item > new_queue.queue[idx * 2 + 2]


@pytest.mark.parametrize('test_list', TEST_LISTS)
def test_pop(test_list):
    from priorityq import PriorityQueue
    new_queue = PriorityQueue(test_list)
    pop_val = new_queue.pop()
    assert pop_val not in new_queue.queue


@pytest.mark.parametrize('test_list, test_val', TEST_TUP)
def test_insert(test_list, test_val):
    from priorityq import PriorityQueue
    new_queue = PriorityQueue(test_list)
    new_queue.insert(test_val)
    assert test_val in new_queue.queue
