# -*- coding: utf-8 -*-
import pytest


TEST_LISTS = ([40, 33, 60, 19, 10],
              [34, 56, 78, 90, 9, 24, 20, 3, 4, 1, 6, 29, 66, 5, 4, 8],
              [24, 45, 92, 93, 65, 87, 19, 9, 46, 72, 85, 4, 76, 900],
              [34, 56, 78, 90, 3, 4, 1, 6, 29, 66, 5, 4, 8, 9, 24, 20, 24, 45, 92, 93, 65, 87, 19, 9, 46, 72, 85, 4, 76, 900])

TEST_TUP = (([40, 33, 60, 19, 10], 99),
            ([40, 33, 60, 19, 10], 445),
            ([40, 33, 60, 19, 10], 1),
            ([40, 33, 60, 19, 10], 2122345),
            ([40, 33, 60, 19, 10], 3),
            ([40, 33, 60, 19, 10], 0))

@pytest.mark.parametrize('test_list', TEST_LISTS)
def test_sift_up(test_list):
    from heap import Heap
    new_heap = Heap(test_list)
    for idx, item in enumerate(new_heap.heap):
        if idx < (len(new_heap.heap) - 1) // 2:
            assert item > new_heap.heap[idx * 2 + 1]
            assert item > new_heap.heap[idx * 2 + 2]


@pytest.mark.parametrize('test_list', TEST_LISTS)
def test_sift_down(test_list):
    from heap import Heap
    new_heap = Heap(test_list)
    new_heap.pop()
    print(new_heap.heap)
    for idx, item in enumerate(new_heap.heap):
        if idx < (len(new_heap.heap) - 1) // 2:
            assert item > new_heap.heap[idx * 2 + 1]
            assert item > new_heap.heap[idx * 2 + 2]


@pytest.mark.parametrize('test_list', TEST_LISTS)
def test_pop(test_list):
    from heap import Heap
    new_heap = Heap(test_list)
    pop_val = new_heap.pop()
    assert pop_val not in new_heap.heap


@pytest.mark.parametrize('test_list, test_val', TEST_TUP)
def test_push(test_list, test_val):
    from heap import Heap
    new_heap = Heap(test_list)
    new_heap.push(test_val)
    assert test_val in new_heap.heap
