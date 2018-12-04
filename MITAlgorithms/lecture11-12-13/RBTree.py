import sys
from .BST import BSTNode, BST

RED = 'red'
BLACK = 'black'


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
