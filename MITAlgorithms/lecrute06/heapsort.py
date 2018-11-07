import heapq
import unittest

class heap:
    def __init__(self, max = True):
        if max:
            self.heapfy = self._max_heapfy
        else:
            self.heapfy = self._min_heapfy
        self._heap = []

    def _max_heapfy(self, index):
        pass

    def _min_heapfy(self):
        pass

    def _parent(self, index):
        return index // 2

    def _left(self, index):
        return index * 2 + 1

    def _right(self, index):
        return index * 2 + 2


class TestHeap(unittest.TestCase):
    def setUp(self):
        self.solution = heap()

    def test_heapfy(self):
        pass


if __name__ == "__main__":
    unittest.main()
