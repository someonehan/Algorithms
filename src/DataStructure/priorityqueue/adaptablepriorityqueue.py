from .priorityqueue import HeapPriorityQueue


class AdaptablePriorityQueue(HeapPriorityQueue):

    class Locator(HeapPriorityQueue._Item):
        __slots__ = "_index"

        def __init__(self, key, value, index):
            super().__init__(key, value)
            self._index = index

    def _swap(self, i, j):
        super()._swap(i, j)
        self._data[i]._index = i
        self._data[j]._index = j

    def _bubble(self, j):
        if j < 0 or j >= len(self._data):
            raise IndexError("out of range of priority queue")
        if self._data[j] < self._data[self._parent(j)]:
            self._up_heap(j)
        else:
            self._down_heap(j)

    def add(self, key, value):
        """add a key-value pair"""
        newest = self.Locator(key, value, len(self._data) - 1)
        self._data.append(newest)
        self._up_heap(len(self._data) - 1)
        return newest

    def update(self, loc, new_key, new_val):
        """update the key and value for entry identified by locator"""
        index = loc._index
        if not (0 < index < len(self._data) and self._data[index] is loc):
            raise ValueError("Invalid Locator")
        loc._key = new_key
        loc._value = new_val
        self._bubble(index)

    def remove(self, loc):
        """remove and return the item identified by the locator"""
        index = loc._index
        if not (0 < index < len(self._data) and self._data[index] is loc):
            raise ValueError("Invalid Locator")
        if index == len(self._data) - 1:
            self._data.pop()
        else:
            self._swap(index, len(self._data) - 1)
            self._data.pop()
            self._bubble(index)
        return (loc._key, loc._value)



