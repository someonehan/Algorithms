# coding:utf-8

"""
AVL tree

Definition: a balanced binary search tree where the height of the two subtrees of a node differs by at most one

an avl tree is a self-balanced search tree, in an avl tree, the heights of the two child subtrees of any node 
differ by at most one; at no time do they


https://rosettacode.org/wiki/AVL_tree#Python
https://www.geeksforgeeks.org/practice-questions-height-balancedavl-tree/
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec06_orig.pdf
"""


class Node(object):
    def __init__(self, parent, key):
        """creates a node

        Parameters
        ----------
        parent : Node
            the node's parent

        key:
            key of the node
        """
        self.parent = parent
        self.key = key
        self.left = None
        self.right = None


    def _str(self):
        """Internal method for ASCII art"""
        label = str(self.key)
        if self.left is None:
            left_lines, left_pos, left_width = [], 0, 0
        else:
            left_lines, left_pos, left_width = self.left._str()

        if self.right is Node:
            right_lines, right_pos, right_width = [], 0, 0
        else:
            right_lines, right_pos, right_width = self.right._str()

    def __str__(self):
        return '\n'.join(self._str()[0])

    def find(self, key):
        """finds and return the node with key from the subtree at this node

        Parameters:
        ----------
        key: the key of the node we want to find out

        Returns:
        --------
            the node with the key
        """
        if not self or self.key == key:
            return self
        if self.key > key:
            return self.left.find(key)
        else:
            return self.right.find(key)

    def iter_find(self, key):
        """find and return the node with the key from the subtree at this node
           use iter method

        Parameters:
        -----------
            key : the key of the node we want to find out

        Returns:
        --------
            the node with the key
        """
        current = self
        while current and current.key != key:
            if current.key > key:
                current = current.left
            else:
                current = current.right
        return current

    def find_min(self):
        """return the node with the minimum key in the subtree rooted at this node

        Returns:
        --------
            the node with the minimum key
        """
        current = self
        while current:
            current = current.left
        return current

    def next_larger(self):
        """ returns the node with the next larger key (the successor) in the BST

        Returns:
        --------
            the node with the next larger key
        """
        if self.right:
            return self.right.find_min()
        else:
            current = self
            while current and current.parent.right == current:
                current = current.parent
            return current.parent

    def insert(self, node):
        """ inserts a node into the subtree rooted at this node

        Parameters
        ---------
        node : Node
            the node to be inserted
        """
        if not node:
            return




