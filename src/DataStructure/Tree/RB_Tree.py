
from .TreeMap import TreeMap


class RB_TreeMap(TreeMap):
    """store map implement using the red-black tree
    1. the node is red or black
    """

    RED = 1
    BLACK = 0

    class _Node(TreeMap._Node):
        """Node class for Red-black tree maintaining red and black"""

        __slots__ = 'color'

        def __init__(self, element, **kwargs):
            super().__init__(element, kwargs)
            self.color = RB_TreeMap.RED

    def _rebalance_access(self, p):
        """"""
        pass


    def _rebalance_insert(self, leaf):
        """
        params:
            leaf: the new insert Position

        when insert a new element,
        if the original tree is empty, the inserted element is the root
        of the original tree is not empty, may violation property 4, which
        say that a red node can not have a red child

        after insert a new element in the tree, there will be 3 case
        case 1: the node uncle node is a red, which occurs when both node.p
            and y are red

        case 2: the node uncle node is black and node is a right child
        case 3: the node uncle node is black and node is a left child

        """
        node = leaf.element()
        while node.parent.color == RB_TreeMap.RED:
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y.color == RB_TreeMap.RED:
                    # this is case 1
                    node.parent.color = RB_TreeMap.BLACK
                    y.color = RB_TreeMap.BLACK
                    y.parent.parent.color = RB_TreeMap.RED
                    node = node.parent.parent
                elif node is node.parent.right:
                    # this is case 2
                    node = node.parent
                    self._left_rotate(node)
                node.parent.color = RB_TreeMap.BLACK
                node.parent.parent.color = RB_TreeMap.RED
                self._right_rotate(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y.color == RB_TreeMap.RED:
                    # this is case 1
                    node.parent.color = RB_TreeMap.BLACK
                    y.color = RB_TreeMap.BLACK
                    node.parent.parent.color = RB_TreeMap.RED
                    node = node.parent.parent
                elif node is node.parent.left:
                    node = node.parent
                    self._right_rotate(node)
                node.parent.color = RB_TreeMap.BLACK
                node.parent.parent.color = RB_TreeMap.RED
                self._left_rotate(node.parent.parent)
        self._root.color = RB_TreeMap.BLACK


    def _rebalance_delete(self, p):
        """"""
        pass


