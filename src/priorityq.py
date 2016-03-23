# -*- coding: utf-8 -*-


class PriorityQueue(object):
    '''Create queue using nodes'''

    def __init__(self, user_input=None):
        self.queue = []
        if user_input is not None:
            try:
                [self.insert(tup) for tup in user_input]
            except TypeError:
                print('Argument is not iterable.')

    def _sift_up(self):
        idx = self._length() - 1
        while idx > 0:
            child = idx
            parent = (idx - 1) // 2
            if self.queue[child][0] > self.queue[parent][0]:
                self.queue[child], self.queue[parent] = self.queue[parent], self.queue[child]
                idx = (idx - 1) // 2
                continue
            break

    def _sift_down(self):
        idx = 0
        while idx < (self._length() - 1) // 2:
            print(idx)
            parent = idx
            child_l = idx * 2 + 1
            child_r = idx * 2 + 2
            idx += 1
            print(self.queue)
            if self.queue[parent][0] < self.queue[child_l][0]:
                self.queue[parent], self.queue[child_l] = self.queue[child_l], self.queue[parent]
            if self.queue[parent][0] < self.queue[child_r][0]:
                self.queue[parent], self.queue[child_r] = self.queue[child_r], self.queue[parent]
            continue

    def insert(self, tup):
        self.queue.append(tup)
        self._sift_up()

    def pop(self):
        try:
            return_val = self.queue[0]
            del self.queue[0]
            self.queue.insert(0, self.queue.pop(self._length() - 1))
            self._sift_down()
            return return_val
        except IndexError:
            print('This queue is empty.')

    def _length(self):
        return len(self.queue)
