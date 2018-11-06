
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next_ = next_

class LinkedListUnderflow(ValueError):
    pass


class LList(list):
    def __init__(self, iterable = None):
        self.head = LNode(0)
        if iterable:
            last = self.head.next_
            while last:
                last = last.next_
            for item in iterable:
                last.next_ = LNode(item)
                last.next_ = last.next_.next_

    def append(self, p_object): # real signature unknown; restored from __doc__
        """ L.append(object) -> None -- append object to end """
        last = self.head.next_
        node = LNode(p_object)
        while last:
            last = last.next_
        last.next_ = node
        self.head.elem += 1

    def prepend(self, p_object):
        """ L.appendhead(object) -> None -- append object to head"""
        # if not self.head:
        #     self.head = LNode(p_object)
        # else:
        # if list is empty
        self.head.next_ = LNode(p_object, self.head)
        self.head.elem += 1

    def insert(self, index, p_object): # real signature unknown; restored from __doc__
        """ L.insert(index, object) -- insert object before index """
        node = LNode(p_object)
        pre = self.head.next_
        i = 0
        while i < index - 1 and pre:
            pre = pre.next_
            i += 1
        pre.next_, node.next_ = node, pre.next
        self.head.elem += 1

    def clear(self):
        """
        L.clear() -> None -- remove all items from L
        """
        self.head.elem = 0
        self.head.next_ = None

    def copy(self): # real signature unknown; restored from __doc__
        """ L.copy() -> list -- a shallow copy of L """
        return []

    def count(self, value): # real signature unknown; restored from __doc__
        """ L.count(value) -> integer -- return number of occurrences of value """
        occurs = 0
        current = self.head.next_
        while current:
            if current.elem == value:
                occurs += 1
            current = current.next_
        return occurs

    def extend(self, iterable): # real signature unknown; restored from __doc__
        """ L.extend(iterable) -> None -- extend list by appending elements from the iterable """
        last = self.head.next_
        while last:
            last = last.next_
        for item in iterable:
            last.next_ = LNode(item)
            last.next_ = last.next_.next_

    def index(self, value, start=None, stop=None): # real signature unknown; restored from __doc__
        """
        L.index(value, [start, [stop]]) -> integer -- return first index of value.
        Raises ValueError if the value is not present.
        """
        start = start if start else 0
        stop = stop if stop else self.head.elem
        current_node = self.head.next_
        find = False
        while start < stop:
            current_node = current_node.next_
            start += 1
            if current_node.elem == value:
                find = True
                break
        if not find:
            raise ValueError('the value in not present')
        return start

    def pop(self, index=None): # real signature unknown; restored from __doc__
        """
        L.pop([index]) -> item -- remove and return item at index (default last).
        Raises IndexError if list is empty or index is out of range.
        """
        if not self.head.next_:
            raise IndexError('the list is empty')
        if index:
            if self.head.elem < index:
                raise IndexError("index is out of range")

            pre = self.head.next_
            for i in range(index):
                pre = pre.next_
            e = pre.next_.elem
            pre.next_ = pre.next_.next_
            return e
        else:
            e = self.head.next_.elem
            self.head.next_ = self.head.next_.next_
            return e

    def remove(self, value): # real signature unknown; restored from __doc__
        """
        L.remove(value) -> None -- remove first occurrence of value.
        Raises ValueError if the value is not present.
        """
        pre = self.head.next_
        while pre:
            if pre.next_ and pre.next_.elem == value:
                pass
            pre = pre.next_

    def reverse(self): # real signature unknown; restored from __doc__
        """ L.reverse() -- reverse *IN PLACE* """
        pass

    def sort(self, key=None, reverse=False): # real signature unknown; restored from __doc__
        """ L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE* """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Implement self+=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Implement self*=value. """
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        return self.head.elem

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value.n """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __reversed__(self): # real signature unknown; restored from __doc__
        """ L.__reversed__() -- return a reverse iterator over the list """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ L.__sizeof__() -- size of L in memory, in bytes """
        pass

    __hash__ = None