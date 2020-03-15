from .BinaryTree import BinaryTree

class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = "_element", "_parent", "_left", "_right"

        def __init__(self, element, parent = None, left = None, right = None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """an abstraction representing the location representing a location"""
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and self._node is other._node

        def __ne__(self, other):
            return self._node is not other._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be Position Type")
        if p._container is not self:
            raise TypeError("p does not belong to this container")
        if p._node._parent is p._node:
            raise TypeError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        """create an initially empty binary tree"""
        self._root = None
        self._size = 0

    def __len__(self):
        """return the total number of elements in the tree"""
        return self._size

    def root(self):
        """return root position of the tree"""
        return self._make_position(self._root)

    def parent(self, p):
        """return the position of p's parent"""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """return the position of p's left child"""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """return the position of p's righ__t child"""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """return the number of children of position p"""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        """place element e at the root of an empty tree and return new position
        Raise ValueError if tree no empty
        """
        if self._root is not None:
            raise ValueError("root exists")
        self._root = self._Node(e)
        self._size = 1
        return self._make_position(self._root)

    def _add_left(self, e, p):
        """create a new left child for position p storing e
        return the position of new node
        Raise ValueError if position p is invalid or p already has a left child
        """
        node = self._validate(p)
        if node._left is not None: raise ValueError("left child exists")
        node._left = self._Node(e, node)
        self._size += 1
        return self._make_position(node._left)

    def _add_right(self, e, p):
        """create a new right child for position p storing e
        return the position of new node
        Raise ValueError if position p is invalid or p already has a right child
        """
        node = self._validate(p)
        if node._left is not None: raise ValueError("right child exists")
        node._right = self._Node(e, node)
        self._size += 1
        return self._make_position(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """delete the node at position p, and replace it with its child, if any
        return the element that had been stored at position p
        Raise ValueError if position p is invalid or p has two children
        """
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError("p has two children")
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node.parent
        if self.is_root(p):
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = None
        return node._element


    def _attach(self, p, t1, t2):
        """attach trees t1 and t2 as left and right subtrees of external p

        :raise ValueError if position p is invalid or p is not a leaf
        :raise TypeError if t1 and t2 and self are not the same type
        """
        node = self._validate(p)
        if not self.is_leaf(p):raise ValueError("position must be leaf")
        if not type(self) is type(t1) is type(t2):
            raise TypeError("tree types must match")

        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0

if __name__ == "__main__":
    print("hello world")

