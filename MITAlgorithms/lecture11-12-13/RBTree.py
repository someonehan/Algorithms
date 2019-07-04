import sys
from .BST import BSTNode, BST

RED = 'red'
BLACK = 'black'

"""
a red-black tree is a binary search tree with the extra bit of storage per node: it's color,
which can be either red or black. By constraining the node colors on any simple path from the 
root to leaf, red-black tree ensure that no such path is more than twice as long as any other,
so that the tree is approximately balanced.

each node of the tree now contains color, key, left, right, and p. if a child or the parent of 
node does not exists, the corresponding pointer attribute of the node contains the value NIL
we shall regard these NILs as being pointers to leaves(external nodes) of the binary search tree 
and normal, key-bearing nodes as being internal node of the tree

红黑树是一棵二叉树， 有五大特征：
a red-black tree is a binary tree that satisfies the following red-black properties

特征一： 节点要么是红色，要么是黑色（红黑树名字由来）。
      every node is either red or black
特征二： 根节点是黑色的
      the root is black
特征三： 每个叶节点(nil或空节点)是黑色的。
      every leaf (NIL) is black
特征四： 每个红色节点的两个子节点都是黑色的（相连的两个节点不能都是红色的）。
      if a node is red, then both its children are black
特征五： 从任一个节点到其每个叶子节点的所有路径都是包含相同数量的黑色节点。
      for each node, all simple path from the node to descendant leaves the same number of black nodes
"""


class RBNode(BSTNode):
    """
    init red-black tree node
    the different with bst node is that this node's has color property
    """
    def __init__(self, key, parent=None):
        super(RBNode, self).__init__(key, parent)
        self.color = BLACK

    @property
    def color(self):
        return self.color

    @color.setter
    def color(self, value):
        if value in (RED, BLACK):
            self.color = value
        else:
            raise ValueError


class RBTree(BST):

    null = RBNode(sys.maxsize, None)

    def __init__(self):
        super(RBTree, self).__init__()
        self.node_cls = RBNode

    def leftRotate(self, x):
        """
        left rotate the node
        :param x:
        :return:
        """
        # set the right node's left to the x node's right
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        # change the node's parent
        y.parent = x.parent
        if not y.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def rightRotate(self, y):
        """

        :param y:
        :return:
        """
        x = y.left
        y.left = x.right
        if x.right:
            x.right.parent = y

        x.parent = y.parent
        if not x.parent:
            self.root = x
        elif y.parent.left == y:
            y.parent.left = x
        else:
            y.parent.right = x

        x.right = y
        y.parent = x

    def insert(self, node):
        if not isinstance(node, self.node_cls):
            return

        super().insert(node)

        node.left = RBTree.null
        node.right = RBTree.null
        node.color = RED

        self.insert_fixup()

    def insert_fixup(self, node):
        """
        after insert a node, the tree maybe
        :param node:
        :return:
        """

        pass
