
from .TreeMap import TreeMap


class RB_TreeMap(TreeMap):
    """store map implement using the red-black tree
    1. the node is red or black
    """

    RED = 1
    BLACK = 0

    class _Node(TreeMap._Node):
        """Node class for Red-black tree maintaining red and black"""

        __slots__ = 'red'

        def __init__(self, element, **kwargs):
            super(_Node, self).__init__(element, kwargs)
            self.red = RB_TreeMap.RED





    def _rebalance_access(self, p):
        pass

    def _rebalance_insert(self, leaf):
        pass

    def _rebalance_delete(self, p):
        pass


