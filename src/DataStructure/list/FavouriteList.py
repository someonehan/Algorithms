from . import PositionalList


class FavouriteList:
    class _Item:
        __slots__ = "_value", "_count"

        def __init__(self, value):
            self._value = value
            self._count = 0

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def _find_position(self, e):
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        if p != self._data.first():
            walk = self._data.before(p)
            cnt = p.element()._count
            while walk is not self._data.first() and walk.element()._count <= cnt:
                walk = self._data.before(walk)
            self._data.add_before(walk, self._data.delete(p))

    def access(self, e):
        p = self._find_position(e)
        if p is None:
            self._data.add_last(e)
        p.element()._count += 1
        self._move_up(p)

    def remove(self, e):
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)

    def top(self, k):
        """
        Generate sequence of top k elements in terms of access count
        """
        walk = self._data.first()
        i = 0
        while i < k and walk is not None:
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)


