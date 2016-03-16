# -*- coding: utf-8 -*-


class Heap(object):
    '''Create heap using nodes'''

    def __init__(self, user_input=None):
        self.heap = [None]
        self.size = 0
        try:
            [self.insert(val) for val in user_input]
        except TypeError:
            print('Argument is not iterable.')

    def _sift_up(self, idx):
        print('**************** sift up')
        start = idx
        while start//2 > 0:
            print('**** outer while')
            idx = start
            while idx//2 > 0:
                print('idx: ', idx, '  idx//2: ', idx//2)
                print(self.heap[idx], '**', self.heap[idx//2])
                if self.heap[idx] > self.heap[idx//2]:
                    self.heap[idx], self.heap[idx//2] = self.heap[idx//2], self.heap[idx]
                idx = idx//2
            start = start//2

    def _sift_down(self):
        idx = 1
        while idx*2 < self.size:
            if self.heap[idx] < self.heap[idx*2] or self.heap[idx] < self.heap[(idx*2) + 1]:
                bigger_child = max(self.heap[idx*2], self.heap[(idx*2) + 1])
                child_idx = self.heap.index(bigger_child)
                self.heap[idx], bigger_child = bigger_child, self.heap[idx]
            idx = child_idx

    def insert(self, val):
        self.size += 1
        self.heap.append(val)
        self._sift_up(self.size)

    def extract(self):
        try:
            return_val = self.heap[1]
            del self.heap[1]
            self.heap.insert(1, self.heap.pop(len(self.heap) - 1))
            self._sift_down()
            return return_val
        except IndexError:
            print('This heap is empty.')


new_heap = Heap([34, 56, 78, 90, 3, 4, 1, 6, 29, 66, 5, 4, 8, 9, 24, 20, 24, 45, 92, 93, 65, 87, 19, 9, 46, 72, 85, 4, 76])
print(new_heap.heap)
new_heap.extract()
print(new_heap.heap)
