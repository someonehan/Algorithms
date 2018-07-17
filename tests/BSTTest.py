import unittest

from MITAlgorithms.BST import BSTNode, BST


class TestBSTNode(unittest.TestCase):

    def setUp(self):
        self.current_node = BSTNode(4, parent=None)
        self.smaller = BSTNode(3)
        self.bigger = BSTNode(5)

    def test_init_(self):
        self.assertIsNotNone(self.current_node)
        self.assertEqual(self.current_node.key, 4)

    def test_insert(self):
        self.current_node.insert(self.smaller)
        self.assertEqual(self.current_node.left.key, self.smaller.key)
        self.assertEqual(self.smaller.parent.key, self.current_node.key)
        self.current_node.insert(self.bigger)
        self.assertEqual(self.current_node.right.key, self.bigger.key)
        self.assertEqual(self.bigger.parent.key, self.current_node.key)

    def test_delete_without_child(self):
        self.current_node.insert(self.smaller)
        self.current_node.insert(self.bigger)

        self.current_node.delete(self.smaller)
        self.assertIsNone(self.current_node.left)

        self.current_node.delete(self.bigger)
        self.assertIsNone(self.current_node.right)

    def test_delete_with_one_child(self):
        self.current_node.insert(self.smaller)
        self.current_node.left.insert(self.bigger)
        self.current_node.delete(self.smaller)
        # self.assertEqual(self.current_node.)

    def test_find_min(self):
        minimum = self.current_node.find_min()
        self.assertEqual(minimum.key, self.current_node.key)
        self.current_node.insert(self.smaller)
        minimum = self.current_node.find_min()
        self.assertEqual(minimum.key, self.smaller.key)
        self.current_node.insert(self.bigger)
        minimum = self.current_node.find_min()
        self.assertEqual(minimum.key, self.smaller.key)

    def test_findmax(self):
        maximum = self.current_node.find_max()
        self.assertEqual(maximum, self.current_node)


class TestBST(unittest.TestCase):
    def setUp(self):
        self.tree = BST()
        self.root = BSTNode(key=3)
        self.smaller = BSTNode(key=2)
        self.bigger = BSTNode(key=4)

    def test_init(self):
        self.assertIsNone(self.tree.root)

    def test_insert_root(self):
        self.tree.insert(self.root)
        self.assertIsNotNone(self.root)
        self.assertEqual(self.root,self.tree.root)

    def test_insert_left_node(self):
        self.tree.insert(self.root)
        self.tree.insert(self.smaller)
        self.assertIsNotNone(self.root.left)
        self.assertEqual(self.root.left, self.smaller)
        self.assertEqual(self.smaller.parent, self.root)

    def test_insert_right_node(self):
        self.tree.insert(self.root)
        self.root.insert(self.bigger)
        self.assertIsNotNone(self.root.right)
        self.assertEqual(self.root.right, self.bigger)
        self.assertEqual(self.bigger.parent, self.root)

    def test_find_min(self):
        self.tree.insert(self.root)

        self.tree.insert(self.bigger)
        self.assertIsNotNone(self.tree.find_min())
        self.assertEqual(self.root, self.tree.find_min())

        self.tree.insert(self.smaller)
        self.assertEqual(self.smaller, self.tree.find_min())


if __name__ == "__main__":
    unittest.main()