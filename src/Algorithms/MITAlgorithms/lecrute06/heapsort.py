import heapq
import unittest


class heap:
    def __init__(self, alist,max=True):
        if max:
            self.heapfy = self._max_heapfy
        else:
            self.heapfy = self._min_heapfy
        self._heap = alist
        self.length = len(self._heap)
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // 2, 0):
            self.heapfy(i - 1)

    def sort(self):
        for i in range(self.length - 1, 1):
            self._heap[i], self._heap[0] = self._heap[1], self._heap[0]
            self.heapfy(0)

    def _max_heapfy(self, index):
        left_child = self._left(index)
        right_child = self._right(index)
        largest = index
        if left_child <= len(self._heap) and self._heap[left_child] > self._heap[index]:
            largest = left_child
        if right_child <= len(self._heap) and self._heap[right_child] > self._heap[index]:
            largest = right_child
        if largest != index:
            self._heap[largest], self._heap[index] = self._heap[index], self._heap[largest]
            self.heapfy(largest)

    def _min_heapfy(self, index):
        left_child = self._left(index)
        right_child = self._right(index)
        smallest = index
        if left_child <= len(self._heap) and self._heap[left_child] < self._heap[index]:
            smallest = left_child
        if right_child <= len(self._heap) and self._heap[right_child] < self._heap[index]:
            smallest = right_child
        if smallest != smallest:
            self._heap[smallest], self._heap[index] = self._heap[index], self._heap[smallest]
            self.heapfy(smallest)


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
