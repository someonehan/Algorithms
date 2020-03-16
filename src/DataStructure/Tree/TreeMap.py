from .BinaryTree import LinkedBinaryTree
from ..Dict import MapBase

""" 
implements ordered dict ADT using the binary search tree
"""


class TreeMap(LinkedBinaryTree, MapBase):
    """stored map implementation using a binary search tree"""

    #------------------override Position class-------------------
    # the Position class hold the Node
    class Position(LinkedBinaryTree.Position):
        def key(self):
            """return key of map's key-value pair"""
            return self.element().key

        def value(self):
            """return value of map's key-value pair"""
            return self.element().value

    #------------------no public utilities------------------------
    def _subtree_search(self, p, k):
        """return position of p's subtree having key, or last node searched"""
        if k == p.key():
            return p
        if p < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p

    def _subtree_minmum(self, p):
        """return position of first item in subtree rooted as p"""
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_maxmum(self, p):
        """return position of last item in the subtree rooted as p"""
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk

    #----------------------publci utilities------------------------
    def first(self):
        """return the first position in the tree
        None if empty
        """
        return self._subtree_minmum(self._root) if self._root is not None else None

    def last(self):
        """return the last position in the tree
        None if empty
        """
        return self._subtree_maxmum(self._root) if self._root is not None else None

    def pre(self, p):
        """return the position just before p in the natural order
        None if p is the first element
        """
        # if the position has left substree the pre node is the minmum item of the subtree
        # rooted with left child
        if self.left(p):
            return self._subtree_maxmum(self.left(p))
        else:
            walk = p
            parent = self.parent(p)
            while parent is not None and walk == self.left(parent):
                walk = parent
                parent = self.parent(walk)
            return parent

    def succ(self, p):
        """return the position just after p in the natural order
        None if p is the last element
        """
        if self.right(p):
            return self._subtree_minmum(self.right(p))
        else:
            walk = p
            parent = self.parent()
            while parent is not None and walk == self.right(parent):
                walk = parent
                parent = self.parent(walk)
            return parent

    def find_position(self, k):
        """return position with key k, or else neighbor
        None if empty
        """
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)  # hook for balanced tree subclass
            return p

    def find_min(self):
        """return (key, value) pair with minimum key
        None if empty
        """
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())

    def find_ge(self, k):
        """return (key, value) pair with least key greater than ot equal to k
        None if does not exists such a key
        """
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() < k:
                p = self.succ(p)
            return (p.key(), p.value())

    def find_range(self, start, end):
        """iterate all (key, value) pairs such that start <= key < stop
        if start is None: iteration begins with the minimum key of tree
        if end is None: iteration ends with the maximum key of tree
        """
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                p = self.find_position(start)
                if p.key() < start:
                    p = self.succ(p)
            while p is not None and (end is None or p.key() < end):
                yield (p.key(), p.value())
                p = self.succ(p)

    def __getitem__(self, item):
        """return value associated with key k
        raise KeyError if not found
        """
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), item)
            self._rebalance_access(p)
            if item != p.key():
                raise KeyError("Key Error {0}".format(repr(item)))
            return p.value()

    def __setitem__(self, key, value):
        """assign value to key k, overwriting existing value if present"""
        if self.is_empty():
            leaf =  self._add_root(self._Item(key = key, vlaue = value))
        else:
            p = self._subtree_search(self.root(), key)
            if p.key() == key:
                p.element.value = value
                self._rebalance_access(p)
                return
            else:
                item = self._Item(key = key, value = value)
                if p.key() < key:
                    leaf = self._add_right(p, item)
                else:
                    leaf = self._add_left(p, item)
        self._rebalance_insert(leaf)

    def __iter__(self):
        """generate an iteration of all keys in the map order"""
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.succ(p)

    def __delitem__(self, key):
        if not self.is_empty():
            p = self._subtree_search(key)
            if key == p.key():
                self.delete(key)
                return

            self._rebalance_access(p)
        raise KeyError("Key Error {0}".format(repr(key)))

    def delete(self, p):
        """remove the item at a given position"""
        self._validate_position(p)
        if self.left(p) and self.right(p):
            replacement = self.succ(p)
            self._replace(p, replacement.element())
            p = replacement

        self._delete(p)
        self._rebalance_delete(p)

    def _rebalance_access(self, p):
        pass

    def _rebalance_insert(self, leaf):
        pass

    def _rebalance_delete(self, p):
        pass