from .base import PriorityQueueBase
from ..list import PositionalList
from ..common import Empty


class PriorityQueue(PriorityQueueBase):
    def __init__(self):
        """create a new empty priority queue"""
        self._data = PositionalList()

    def __len__(self):
        """return the number of items in the priority queue"""
        return len(self._data)

    def _find_min(self):
        """return position of item with minimum key"""
        if self.is_empty():
            raise Empty("queue is empty")
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def add(self, key, value):
        """add a key-value pair"""
        self._data.add_last(self._Item(key, value))

    def min(self):
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """remove and return (k,v) tuple with minimum key"""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)


class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        """create an empty priority queue"""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue"""
        return len(self._data)

    def add(self, key, value):
        """add a key-value pair"""
        newest = self._Item(key, value)
        walk = self._data.last()
        # find the last element smaller that newest in data
        if walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)

    def min(self):
        """return but do not remove tuple with minimum key"""
        if self.is_empty():
            raise Empty("priority queue is empty")
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """return and remove tuple with minimum key"""
        if self.is_empty():
            raise Empty("priority queue is empty")
        p = self._data.first()
        item = p.element()
        self._data.delete(p)
        return (item._key, item._value)


class HeapPriorityQueue(PriorityQueueBase):
    def _up_heap(self, pos):
        if pos > 0:
            parent = self._parent(pos)
            if self._data[pos] < self._data[parent]:
                # tmp = self._data[pos]
                # self._data[pos] = self._data[parent]
                # self._data[parent] = tmp
                self._swap(pos, parent)
                self._up_heap(parent)

    def _down_heap(self, pos):
        heap_size = len(self._data)
        if pos < heap_size:
            left_index = self._left(pos)
            right_index = self._right(pos)
            largest_index = pos
            if left_index < heap_size and self._data[left_index] > self._data[largest_index]:
                largest_index = left_index

            if right_index < heap_size and self._data[right_index] > self._data[largest_index]:
                largest_index = right_index

            if largest_index != pos:
                # self._data[pos], self._data[largest_index] = self._data[largest_index], self._data[pos]
                self._swap(pos, largest_index)
                self._down_heap(largest_index)

    def _parent(self, i):
        """return the parent index"""
        return (i - 1) // 2

    def _left(self, i):
        """return the left child index"""
        return 2 * i + 1

    def _right(self,i):
        """return the right child index"""
        return 2 * i + 2

    def _heapfy(self):
        # for every not leaf position, rebuild the heap
        for i in range(len(self._data) - 1, -1, -1):
            self._down_heap(i)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    #-----------------------public methods-----------------------
    def __init__(self, contents = None):
        if contents is None:
            self._data = []
        else:
            # init the data list
            self._data = [self._Item(k, v) for k, v in contents]
            # heapfy the data list
            self._heapfy()

    def __len__(self):
        """return the number of element in the priority queue"""
        return len(self._data)

    def add(self, key, value):
        """add a key-value pair"""
        self._data.append(self._Item(key, value))
        self._up_heap(len(self._data) - 1)

    def min(self):
        """return but not remove the minimum key"""
        if self.is_empty():
            raise Empty("priority can't be empty")
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise Empty("priority can't be empty")
        # swap the root item and the last item
        # tmp = self._data[-1]
        # self._data[0] = self._data[-1]
        # self._data[-1] = tmp
        self._swap(-1, 0)

        item = self._data.pop()
        self._down_heap(0)
        return (item._key, item._value)

