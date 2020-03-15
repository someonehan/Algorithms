from abc import ABCMeta, abstractmethod
from queue import Queue

class Tree(metaclass=ABCMeta):

    class Position(metaclass=ABCMeta):
        """an abstract representing the location of a single element"""

        @abstractmethod
        def element(self):
            """return the element stored at this position"""
            raise NotImplementedError("must be implemented in subclass")

        @abstractmethod
        def __eq__(self, other):
            """return true if other position represents the same location"""
            raise NotImplementedError("must be implemented in subclass")

        @abstractmethod
        def __ne__(self, other):
            """return true if other position does not represents the same location"""
            raise NotImplementedError("must be implemented in subclass")

    @abstractmethod
    def root(self):
        """return the Position representing the tree's root(or None if empty)"""
        raise NotImplementedError("must be implemented in subclass")

    @abstractmethod
    def parent(self, p):
        """return the parent position of position p"""
        raise NotImplementedError("must be implemented in subclass")

    @abstractmethod
    def num_children(self, p):
        """return the num children of the positon p"""
        raise NotImplementedError("must be implemented in subclass")

    @abstractmethod
    def children(self, p):
        """generate an iteration of position representing p's children"""
        raise NotImplementedError("must be implemented by subclass")

    @abstractmethod
    def __len__(self):
        """return the total number of the elements in the tree"""
        raise NotImplementedError("must be implemented by subclass")

    #-------------------------concrete methods implemented in this class-----------
    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0






