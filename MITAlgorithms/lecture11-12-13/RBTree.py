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


class RBTree:
    null = RBNode(sys.maxsize, None)

    def __init__(self):
        self.node_cls = RBNode
        self.root = None

    def leftRotate(self, x):
        """left rotate the node

        """
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

    def rightRotate(self, x):
        """

        :param y:
        :return:
        """
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
        y.left = x
        x.parent = y

    # https://www.geeksforgeeks.org/red-black-tree-set-2-insert/
    def insert(self, node):
        """red-black tree insert action
        perform standard BST insertion and set the node'color red

        Parameters:
        -----------
        node : RBNode
            the node to be inserted into the red-black tree
        """
        if not isinstance(node, self.node_cls):
            return
        parent = None
        current = self
        while current:
            parent = current
            if current.key >= node.key:
                current = current.left
            else:
                current = current.right
        if parent is None:
            self.root = node
        else:
            if parent.key >= node.key:
                parent.left = node
            else:
                parent.right = node
        node.parent = parent

        node.left = RBTree.null
        node.right = RBTree.null
        node.color = RED

        self.insert_fixup()

    # https://www.geeksforgeeks.org/red-black-tree-set-3-delete-2/
    def delete(self, node):
        pass

    def insert_fixup(self, node):
        """
        2) if x is root, change color os x as BLACK(black height of complete tree increases by 1)
        3) do following if color of x's parent is not black
           a) if x's uncle is red(grand parent must have been black)
              i) change color of parent and uncle as black
              ii) color of grand parent as RED
              iii) change x = x's grand parent, repeat steps 2 and 3 for new x
           b) if x's uncle is black, then there can be four configurations for x, x'parent and x'grandp
              i) left left case(p is left child of g ans x is left child of p)
              ii) left right case(p is left child of g and x is right child of p)
              iii) right right case(Mirror of case i)
              iiii) right left case(Mirror of case ii)
        """
        while node.parent.color == RED:
            if node.parent.parent.left.color == RED and node.parent.parent.right.color == RED:
                node.parent.parent.color = RED
                node.parent.parent.left.color = BLACK
                node.parent.parent.right.color = BLACK
                node = node.parent.parent
            else:
                if node.parent is node.parent.parent.left:
                    if node is node.parent.left:
                        # right rotate g
                        # swap colors of g and p
                        self.rightRotate(node.parent.parent)
                        node.parent.color, node.parent.right.color = node.parent.right.color, node.parent.color
                    else:
                        # left rotate p and it turn to left left case
                        self.leftRotate(node.parent)
                        self.rightRotate(node.parent)
                        node.color, node.right.color = node.right.color, node.color
                else:
                    if node is node.parent.right:
                        self.leftRotate(node.parent.parent)
                        node.parent.left.color, node.parent.color = node.parent.color, node.parent.left.color
                    else:
                        self.rightRotate(node.parent)
                        self.leftRotate(node.parent)
                        node.color, node.left.color = node.left.color, node.color


