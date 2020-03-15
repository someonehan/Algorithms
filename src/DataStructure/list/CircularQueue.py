from ..common import Empty

class CircularQueue:

    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """create an empty queue"""
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("empty queue")
        return self._tail._next._element

    def dequeue(self):
        if self.is_empty():
            raise Empty("empty queue")
        answer = self._tail._next._element
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = answer._next
        self._size -= 1
        return answer

    def enqueue(self, e):
        newNode = self._Node(e, None)
        if self.is_empty():
            newNode._next = newNode
        else:
            newNode._next = self._tail._next
            self._tail._next = newNode
        self._tail = newNode
        self._size += 1