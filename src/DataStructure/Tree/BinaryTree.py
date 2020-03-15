from queue import Queue
from abc import abstractmethod
from .tree import Tree
from ..list.LinkedStack import LinkedStack

class BinaryTree(Tree):

    @abstractmethod
    def left(self, p):
        raise NotImplementedError("must be implement in subclass")

    @abstractmethod
    def right(self, p):
        raise NotImplementedError("must be implement in subclass")

    def sibling(self, p):
        """return  a position representing p's sibling(or None if no sibling)"""
        parent = self.parent(p)
        if parent is None:
            # if the position has no parent, no sibling
            return None
        # determined the position is the left child or the right child of its parent
        if p is self.left(parent):
            return self.right(p)
        else:
            return self.left(p)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    #-------------------------iteration methods of tree----------------------------
    def positions(self):
        pass

    def pre_order(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """preorder iter all the elements from the root position"""
        yield p
        for c in self.children(p):
            for o in self._subtree_preorder(c):
                yield o

    def _subtree_preorder_iter(self, p):
        """preorder all the elements from the root position use iter method"""
        q = Queue()
        q.put(p)
        while not q.empty():
            p = q.get()
            yield p
            for c in self.children(p):
                q.put(c)

    def post_order(self):
        """generate a postorder of position in the tree"""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        """generate a postorder iteration of position in subtree rooted at p"""
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def _subtree_postorder_iter(self, p):
        s =LinkedStack()
        self._subtree_generator_left(s, p)
        while not s.is_empty():
            l = s.top()
            s.pop()
            yield l
            self._subtree_generator_left(s, self.sibling(l))

    def _subtree_generator_left(self, s, p):
        while p is not None:
            s.push(p)
            p = self.left(p)

    def breathFirst(self, t, visit):
        q = Queue()
        p = t.root()
        if p is not None:
            q.put(p._node)
            while not q.empty():
                item = q.get()
                visit(item)
                if item._left is not None:
                    q.put(item._left)
                if item._right is not None:
                    q.put(item._right)

    def in_order(self):
        if not self.is_empty():
            for item in self._subtree_inorder(self.root()):
                yield item

    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            yield self._subtree_inorder(self.left(p))
        yield p
        if self.right(p) is not None:
            yield self._subtree_inorder(self.right(p))

if __name__ == "__main__":
    print("hello")