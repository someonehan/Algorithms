from abc import ABCMeta, abstractmethod

class Tree(metaclass=ABCMeta):
    """
    abstract base class representing a tree structure
    """

    class Position(metaclass=ABCMeta):
        """An abstraction representing the location of a single element"""
        @abstractmethod
        def element(self):
            """return the element stored in the position"""
            raise NotImplemented("must be implemented in the subclass")

        @abstractmethod
        def __eq__(self, other):
            """return true if other position represents the same location"""
            raise NotImplemented("must be implemented in the subclass")

        def __ne__(self, other):
            return not self == other

    @abstractmethod
    def root(self):
        """return the position representing the tree's root
        (or None if empty)
        """
        raise NotImplemented("must be implemented in the subclass")

    @abstractmethod
    def parent(self, p):
        """return the position representing p's parent
        (or None if p is root)
        """
        raise NotImplemented("must be implemented in the subclass")

    @abstractmethod
    def num_children(self, p):
        """return the number of children that position p has"""
        raise NotImplemented("must be implemented in the subclass")

    @abstractmethod
    def children(self, p):
        """create a iteration of position representing p's children"""
        raise NotImplemented("must be implemented in the subclass")

    @abstractmethod
    def __len__(self):
        """return the total number of elements in the tree"""
        raise NotImplemented("must be implemented in the subclass")


    def is_root(self, p):
        """return true if position represents the root of the tree"""
        return self.root() == p

    def is_leaf(self, p):
        """return true if position p does not has any child"""
        return self.num_children(p) == 0

    def is_empty(self):
        """return true if the tree is empty"""
        return len(self) == 0

    def depth(self, p):
        """return the number of level separating position p from the root"""
        if self.is_root(p):
            return 0
        return self.depth(self.parent(p)) + 1

    def height(self, p = None):
        """return the height of the subtree rooted at positon p
        the height of tree if p is None
        """
        if p is None:
            p = self.root()
        return self._height(p)

    def _height(self, p):
        if self.is_leaf(p): return 0
        else: return 1 + max([self._height(c) for c in self.children(p)])

