from .MapBase import MapBase, HashMapBase


class UnsortedTableMap(MapBase):
    """ map implementation using an unordered list """
    def __init__(self):
        self._table = []

    def __getitem__(self, key):
        """return the value associated with key k(raise KeyError if not found)"""
        for item in self._table:
            if key == item._key:
                return item._value
        raise KeyError("Key Error" + repr(key))

    def __setitem__(self, key, value):
        """assign value v to key, overwriting existing value if present"""
        for item in self._table:
            if key == item._key:
                item._value = value
                return

        # did not found a item match key
        self._table.append(self._Item(key, value))

    def __delitem__(self, key):
        """remove item associated with key (raise KeyError if not found)"""
        for i in range(len(self._table)):
            if self._table[i]._key == key:
                self._table.pop(i)
                return
        raise KeyError("Key Error" + repr(key))

    def __len__(self):
        """return the number of the items in the table"""
        return len(self._table)

    def __iter__(self):
        """generate iteration of the tuple keys"""
        for item in self._table:
            yield item._key


class ChainHashTableMap(HashMapBase):
    """ hash map implemented with separate chaining for collision resolution"""
    def _bucket_getitem(self, index, key):
        bucket = self._table[index]
        if bucket is None:
            raise KeyError("Key Error" + repr(key))
        return bucket[key]

    def _bucket_setitem(self, index, key, value):
        if self._table[index] == None:
            self._table[index] = UnsortedTableMap()
        _size = len(self._table[index])
        self._table[index][key] = value
        if len(self._table[index]) > _size:
            self._n += 1

    def _bucket_delitem(self, index, key):
        bucket = self._table[index]
        if bucket is None:
            raise KeyError("Key Error" + repr(key))
        del bucket[key]
        self._n -= 1

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for item in bucket:
                    yield item._key


class ProbeHashTableMap(HashMapBase):
    _AVAL = object()

    def _is_available(self, index):
        return self._table[index] is None or self._table[index] is ProbeHashTableMap._AVAL

    def _find_slot(self, index, key):

        first_aval = None
        while True:
            if self._is_available(index):
                if first_aval is None:
                    first_aval = index
                if self._table[index] is None:
                    return (False, first_aval)
            elif self._table[index]._key == key:
                return (True, index)
            index = (index + 1) % len(self._table)

    def _bucket_getitem(self, index, key):
        found, index = self._find_slot(index, key)
        if not found:
            raise KeyError("Key Error" + repr(key))
        return self._table[index]._value

    def _bucket_setitem(self, index, key, value):
        found, aval = self._find_slot(index, key)
        if not found:
            self._table[aval] = self._Item(key, value)
            self._n += 1
        else:
            self._table[aval]._value = value

    def _bucket_delitem(self, index, key):
        found, aval = self._find_slot(index, key)
        if not found:
            raise KeyError("Key Error" + repr(key))
        self._table[index]._value = ProbeHashTableMap._AVAL
        self._n -= 1

    def __iter__(self):
        for index in range(len(self._table)):
            if not self._is_available(index)[0]:
                yield self._table[index]._key


class SortedTableMap(MapBase):
    def __init__(self):
        """create an empty map"""
        self._table = []

    def __len__(self):
        """return the number of items in the map"""
        return len(self._table)

    def _find_index(self, l, r, key):
        left, right = l, r
        while left < right:
            mid = (left + right) // 2
            if self._table[mid]._key == key:
                return mid
            elif self._table[mid]._key > key:
                right = mid - 1
            else:
                left = mid + 1
        return right + 1

    def __getitem__(self, key):
        """return the value associated with key (raise KeyError if not found"""
        left, right = 0, len(self._table) - 1
        index = self._find_index(left, right, key)
        if index == len(self._table) or self._table[index]._key != key:
            raise KeyError("Key Error" + repr(key))
        else:
            return self._table[index]._value

    def __setitem__(self, key, value):
        """Assign value to key, overwriting existing value if present"""
        left, right = 0, len(self._table) - 1
        index = self._find_index(left, right, key)
        if index < len(self._table) and self._table[index]._key == key:
            self._table[index]._value = value
        else:
            self._table.insert(index, self._Item(key, value))

    def __delitem__(self, key):
        """remove item associated with key(raise KeyError if not found)"""
        left, right = 0, len(self._table) - 1
        index = self._find_index(left, right, key)
        if index == len(self._table) or self._table[index]._key != key:
            raise KeyError("Key Error" + repr(key))
        else:
            self._table.pop(index)

    def __iter__(self):
        """generate keys of the map order"""
        for item in self._table:
            yield item._key

    def __reversed__(self):
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None

    def find_ge(self, key):
        """return (key, value) pair with least key greater than or equal to k"""
        index = self._find_index(0, len(self._table) - 1, key)
        if index < len(self._table):
            return (self._table[index]._key, self._table[index]._value)
        else:
            return None

    def find_lt(self, key):
        """return (key, value) pair with largest key less than k"""
        index = self._find_index(0, len(self._table) - 1, key)
