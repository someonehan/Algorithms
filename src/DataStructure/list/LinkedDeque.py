
from . import DoubleLinkedBase
from ..common import Empty

class LinkedDeque(DoubleLinkedBase):
    def __init__(self):
        super(LinkedDeque, self).__init__()

    def first(self):
        if self.is_empty():
            raise Empty("deque is empty")
        return self._header_._next._element

    def last(self):
        if self.is_empty():
            raise Empty("deque is empty")
        return self._trailer._prev._element

    def insert_first(self, e):
        """add an element to the front of the deque"""
        self.insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self.insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        self.delete_node(self._header._next)

    def delete_last(self):
        self.delete_node(self._trailer._prev)