# -*- coding: utf-8 -*-


class Heap(object):
    '''Create heap using nodes'''

    def __init__(self, user_input=None):
        self.heap = []
        try:
            [self.push(val) for val in user_input]
        except TypeError:
            print('Argument is not iterable.')

    def _sift_up(self):
        idx = self.length() - 1
        while idx > 0:
            child = idx
            parent = (idx - 1) // 2
            if self.heap[child] > self.heap[parent]:
                self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
                idx = (idx - 1) // 2
                continue
            break

    def _sift_down(self):
        idx = 0
        while idx < (self.length() - 1) // 2:
            print(idx)
            parent = idx
            child_l = idx * 2 + 1
            child_r = idx * 2 + 2
            idx += 1
            print(self.heap)
            if self.heap[parent] < self.heap[child_l]:
                self.heap[parent], self.heap[child_l] = self.heap[child_l], self.heap[parent]
            if self.heap[parent] < self.heap[child_r]:
                self.heap[parent], self.heap[child_r] = self.heap[child_r], self.heap[parent]
            continue

    def push(self, val):
        self.heap.append(val)
        self._sift_up()

    def pop(self):
        try:
            return_val = self.heap[0]
            del self.heap[0]
            self.heap.insert(0, self.heap.pop(self.length() - 1))
            self._sift_down()
            return return_val
        except IndexError:
            print('This heap is empty.')

    def length(self):
        return len(self.heap)


new_heap = Heap([10, 7, 8, 3, 1, 4, 2, 12])
big_heap = Heap([34, 56, 78, 90, 3, 4, 1, 6, 29, 66, 5, 4, 8, 9, 24, 20,
                 24, 45, 92, 93, 65, 87, 19, 9, 46, 72, 85, 4, 76, 900])
print(big_heap.pop())
