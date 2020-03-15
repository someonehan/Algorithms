from collections import MutableMapping
from random import randrange
from abc import abstractmethod

class MapBase(MutableMapping):
    class _Item:
        __slots__ = "_key", "_value"

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < other._key


class HashMapBase(MapBase):
    def __init__(self, cap=11, p=109345121):
        self._table = cap * [None]
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p - 1)
        self._shift = randrange(p)

    def __len__(self):
        return self._n

    def _hash_function(self, key):
        return (hash(key) * self._scale + self._shift) % self._prime % len(self._table)

    @abstractmethod
    def _bucket_getitem(self, index, key):
        pass

    def __getitem__(self, key):
        index = self._hash_function(key)
        return self._bucket_getitem(index, key)

    @abstractmethod
    def _bucket_setitem(self, index, key, value):
        pass

    def _resize(self, size):
        old = list(self._table)
        self._table = size * [None]
        self._n = 0
        for k, v in old:
            # this will call __setitem__
            self[k] = v

    def __setitem__(self, key, value):
        index = self._hash_function(key)
        self._bucket_setitem(index, key, value)
        # if the load factor is bigger than 0.5
        if self._n > len(self._table) // 2:
            self._resize(len(self._table) * 2 - 1)
            # why -1??

    @abstractmethod
    def _bucket_delitem(self,index, key):
        pass

    def __delitem__(self, key):
        index = self._hash_function(key)
        self._bucket_delitem(index, key)
