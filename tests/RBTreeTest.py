import unittest

from MITAlgorithms.RBTree import RBTree, RBNode


class TestRBTree(unittest.TestCase):
    def setUp(self):
        self.tree = RBTree()
        self.nodes = [RBNode(2),RBNode(1),RBNode(4),RBNode(3),RBNode(5),RBNode(6)]
        for node in self.nodes:
            self.tree.insert(node)


    def test_leftRotate(self):
        x = self.nodes[2]
        self.tree.leftRotate(x)
        self.assertEqual(x.key, self.nodes[4].left.key)


    def test_rightRotate(self):
        pass

if __name__ == "__main__":
    unittest.main()