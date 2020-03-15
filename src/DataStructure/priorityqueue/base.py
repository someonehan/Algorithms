

class PriorityQueueBase:

    class _Item:
        """composite to store priority items"""
        __slots__ = "_key", "_value"

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):
        """Return true if the priority queue is empty"""
        return len(self) == 0

