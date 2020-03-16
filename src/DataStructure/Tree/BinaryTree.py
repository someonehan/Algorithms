
from abc import abstractmethod
from .tree import Tree


class BinaryTree(Tree):
    """abstract base class implement a binary tree structure"""

    @abstractmethod
    def left(self, p):
        """return a position representing p's left child
        return None if p does not have a left child
        """
        raise NotImplemented("must be implemented in the subclass")

    @abstractmethod
    def right(self, p):
        """return a positon representing p's right child
        return None if p does not have a right child
        """
        raise NotImplemented("must be implemneted in the subclass")

    def sibling(self, p):
        """return a position representing p's sibling
        None if no sibling
        """
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """generate an iteration of positon representing p's children"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


class LinkedBinaryTree(BinaryTree):
    """linked representing of a binary tree structure"""

    class _Node:
        __slots__ = "element", "left", "right", "parent"

        def __init__(self,element, **kwargs):
            self.element = element
            self.left = kwargs.get("left", None)
            self.right = kwargs.get("right", None)
            self.parent = kwargs.get("parent", None)

    class Position(BinaryTree.Position):
        """an implemention representing the location of a single element"""

        def __init__(self, container, node):
            """this constructor should not be invoked by user."""
            self.container = container
            self.node = node

        def element(self):
            """return the element stored in the position"""
            return self.node.element

        def __eq__(self, other):
            """override the the parent class
            return True if other is a position representing the same location
            """
            return type(self) == type(other) and self.node is other.node

    def __init__(self):
        """create an initally empty binary tree"""
        self._root = None
        self._size = 0

    def _make_position(self, node):
        """return the position for the given node
        or None if no node
        """
        return self.Position(self, node) if node is not None else None

    def _validate_position(self, p):
        """return the associate node, if the position valid"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p.container is not self:
            raise TypeError("p does not belong to this container")
        if p.node.parent is p.node:
            raise TypeError("p is no longer valid")
        return p.node

    def __len__(self):
        """return the total number of the tree
        or None if tree if empty
        """
        return self._size

    def root(self):
        """return the root position of the tree
        or None if the tree is empty"""
        return self._make_position(self._root)

    def parent(self, p):
        """return the position of p's parent
        or None if the p is root
        """
        node = self._validate_position(p)
        return self._make_position(node)

    def left(self, p):
        """return the position of p's left child
        or None if no left child
        """
        node = self._validate_position(p)
        return self._make_position(node.left)

    def right(self, p):
        """return the position of the p's right child
        or None if no right child
        """
        node = self._validate_position(p)
        return self._make_position(node.right)

    def num_children(self, p):
        """return the number of children of position p"""
        node = self._validate_position(p)
        count = 0
        if node.left is not None:
            count = count + 1
        if node.right is not None:
            count = count + 1
        return count

    #--------------udpate methods-----------------------------
    def _add_root(self, e):
        """place element e at the root of an empty tree and return new Position
        Raise ValueError if tree noempty
        """
        if self._root is not None:
            raise ValueError("root exists")
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """create a new left child for position p,storing element e
        return the position of new node
        Raise ValueError if position p is invalid or p already has a left child
        """
        node = self._validate_position(p)
        if node.left is not None:
            raise ValueError("left child exists")
        self._size += 1
        node.left = self._Node(e, parent=node)
        return self._make_position(node.left)

    def _add_right(self, p, e):
        """create a new right child for position p, storing element e
        return the position of new node
        Raise ValueError if position p is invalid or p already has a right child
        """
        node = self._validate_position(p)
        if node.right is not None:
            raise ValueError("right child exists")
        self._size += 1
        node.right = self._Node(e, parent=node)
        return self._make_position(node.right)

    def _replace(self, p, e):
        """replace the element at position of p with e
        and return the old element
        """
        node = self._validate_position(p)
        old = node.element
        node.element = e
        return old

    def _delete(self, p):
        """delete the node at position p, and replace it with it's child if any
        return the element that had been stored at position p
        Raise ValueError if position p is invalid or p has two position
        """
        node = self._validate_position(p)
        if self.num_children() == 2:
            raise ValueError("p has two children")
        child = node.left if node.left else node.right
        if child is not None:
            child.parent = node.parent

        if node is self._root:
            self._root = child
        else:
            parent = node.parent
            if child is parent.left:
                parent.left = child
            else:parent.right = child
        self._size -= 1
        node.parent = node  # convention for deprecated node
        return node.element

    def _attach(self, p, t1, t2):
        """attach trees t1 and t2 as left and right subtree of external p

        raise ValueError if the position is not left
        """
        node = self._validate_position(p)
        if not self.is_leaf(p):
            raise ValueError("position must be external p")
        if not type(self) is type(t1) is type(t2):
            raise ValueError("three types must be the same")
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root.parent = node
            node.left = t1._root
            t1._root = self._root
            t1._size = 0
        if not t2.is_empty():
            t2._root.parent = node
            node.right = t2._root
            t2._root = self._root
            t2._size = 0