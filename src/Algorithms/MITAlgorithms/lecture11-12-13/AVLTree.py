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
        if self.right is None:
            right_lines, right_pos, right_width = [], 0, 0
        else:
            right_lines, right_pos, right_width = self.right._str()
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        if (middle - len(label)) % 2 == 1 and self.parent is not None and \
                self is self.parent.left and len(label) < middle:
            label += '.'
        label = label.center(middle, '.')
        if label[0] == '.': label = ' ' + label[1:]
        if label[-1] == '.': label = label[:-1] + ' '
        lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                 ' ' * left_pos + '/' + ' ' * (middle - 2) +
                 '\\' + ' ' * (right_width - right_pos)] + \
                [left_line + ' ' * (width - left_width - right_width) + right_line
                 for left_line, right_line in zip(left_lines, right_lines)]
        return lines, pos, width

    def __str__(self):
        return '\n'.join(self._str()[0])

    __repr__ = __str__

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
        parent = None
        current = self
        while current and current.key != node.key:
            parent = current
            if current.key > node.key:
                current = current.left
            else:
                current = current.right
        node.parent = parent
        if node.key >= parent.key:
            parent.right = node
        else:
            parent.left = node

    def delete(self, node):
        """delete and return this node from the tree rooted self

        Parameters:
        -----------
        node : Node
            the node to be deleted

        Returns:
        --------
        node : Node
            return the node removed from the tree
        """
        # 1. the node only has left child
        # 2. the node only has right child
        # 3. the node has none child
        if node.left is None or node.right is None:
            if node is node.parent.left:
                node.parent.left = node.left or node.right
                # this means that the node has one child
                if node.parent.left:
                    node.parent.left.parent = node.parent
            else:
                node.parent.right = node.left or node.right
                # this means that the node has one child
                if node.parnet.right:
                    node.parent.right.parent = node.parent
            return node
        # 4. the node has two subtree
        else:
            succossor = node.next_larger()
            succossor.key, node.key = node.key, succossor.key
            return node


def height(node):
    """ Get the height of the tree rooted with node

    Parameters:
    ----------
    node: Node
    """
    if node is None:
        return -1
    else:
        return getattr(node, 'height')

def update_height(node):
    """Update the tree's height rooted node

    Parameters:
    -----------
    node:Node
    """
    node.height = max(height(node.left), height(node.right)) + 1


class AVL():
    """AVL binary search tree implements"""

    def __init__(self):
        """init an empty tree"""
        self.root = None

    def __str__(self):
        if self.root is None:
            return '<empty tree>'
        else:
            return str(self.root)

    def find(self, key):
        """finds and returns the node with key from the subtree rooted at this node

        Parameters:
        ----------
            key:the key of the node want to find

        Returns:
        --------
            the node with the k or None
        """
        # return self.root.find(key=key) if self.root else None
        return self.root and self.root.find(key)

    def find_min(self):
        """finds and returns the minimum node from the subtree rooted at this node"""

        return self.root and self.root.find_min()

    def next_larger(self, k):
        """find the next_larger (the successor) node of the node with key k

        Parameters:
        ----------
        k : int
            the node with key

        Returns:
        --------
        node : Node
        """
        node = self.find(k)
        return node and node.next_larger()

    # https://www.codingeek.com/data-structure/avl-tree-introduction-to-rotations-and-its-implementation/
    def left_rotate(self, x):
        """left rotate the subtree rooted x"""
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if x is y.parent.left:
                y.parent.left = y
            else:
                y.parent.right = y

        x.right = y.left
        y.left = x
        x.parent = y
        update_height(x)
        update_height(y)

    def right_rotate(self, x):
        """right rotate the subtree rooted x"""
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if x is y.parent.left:
                y.parent.left = y
            else:
                y.parent.right = y
        x.left = y.right
        y.right = x
        x.parent = y
        update_height(x)
        update_height(y)


    def rebalance(self, node):
        while node is not None:
            update_height(node)
            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif height(node.right) >= 2 + height(node.left):
                if height(node.right.right) >= height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent

    def insert(self, k):
        """Inserts a node with key k into the subtree rooted at this node.
        this avl version

        Parameters:
        -----------
        k : key
            the key of the node bo be inserted
        """
        node = Node(None, k)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)
        self.rebalance(node)

    def delete(self, k):
        """deletes and returns a node with key k if it exists from the tree
        this AVL version guarantees the balances property h = O(lg n)

        Parameters:
        ----------
            k : the key of the node we want to delete

        Returns:
        --------
            the deleted node with the key k
        """
        node = self.find(k)
        if node is None:
            return None
        if node is self.root:
            p = Node(None, 0)
            p.left = self.root
            self.root.parent = p
            deleted = self.root.delete(node)
            self.root = p.left

        else:
            deleted = self.root.delete(node)

        self.rebalance()

def main():
    import random, sys

    items = [random.randrange(100) for i in range(100)]

    tree = AVL()
    print(tree)

    for item in items:
        tree.insert(item)
        print("\nadd  " + str(item))
        print(tree)

if __name__ == "__main__":main()




