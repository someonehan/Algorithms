
class BSTNode(object):
    """A Binary search tree node"""
    def __init__(self, key = None, parent = None):
        """
        create a Binary Search Tree Node
        :param key: the key of the node
        :param parent: the parent of the node
        """
        self.parent = parent
        self.left = None
        self.right = None
        self.key = key

    def search(self,k):
        """
        find the node with key of k from the tree rooted self
        compare from the rooted key, if the k is equal to self.key return self
        if the k is less than self.key find the node from the tree rooted with self.left
        if the k is larger than self.key find the node from the tree rooted with self.right

        the runtime is O(h) h is the height of the tree rooted self
        :param k: the key of the node to be searched
        :return: if exits return the node else None
        """
        if not self or self.key == k:
            return self
        if self.key > k:
            return self.left.search(k)
        else:
            return self.right.search(k)

    def itertive_search(self, k):
        """
        the same action with method search
        but use while loop instead of ...
        :param k: the key of the node to searched
        :return: if exist return the node else None
        """
        current = self
        while current and current.key != k:
            if current.key > k:
                current = self.left
            else:
                current = self.right
        return current

    def find_min(self):
        """
        find the min key node from the tree rooted self

        runtime:O(h) h is the height of the tree
        :return: the node with minimum key
        """
        current = self
        while current.left:
            current = current.left
        return current

    def find_max(self):
        """
        find the max key node from the tree rooted self

        runtime:O(h) h is the height of the tree
        :return: the node with maximum key
        """
        current = self
        while current.right:
            current = current.right
        return current

    def find_successor(self):
        """
        find the next larger of self from the tree rooted self
        if self has right child the next larger node is the min mode of the tree rooted self.right
        if self is the largest node of the tree rooted self meaning that the tree has no right leaf next larger is None
        :return: the next larger of the node
        """
        if self.right:
            return self.right.find_min()
        else:
            current = self
            p = self.parent
            while p and p.right == current:
                current = p
                p = p.parent
            return p

    def insert(self, node):
        """
        insert the node into the tree rooted self

        :param node: the node to be inserted
        :return: None
        """
        current = self
        parent = None
        while current:
            parent = current
            if current.key >= node.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if node.key >= parent.key:
            parent.right = node
        else:
            parent.left = node

    def delete(self, node):
        """
        delete the node from the tree rooted self
        :param node: the node to be deleted
        :return: None
        """
        # the node's left child is None
        # the node's right child is None
        # or the both the node's left and right child are None
        if node.left is None or node.right is None:
            if node is node.parent.left:
                node.parent.left = node.left or node.right
                if node.parent.left:
                    node.parent.left.parent = node.parent
            else:
                node.parent.right = node.right or node.right
                if node.parent.right:
                    node.parent.right.parent = node.parent
        else:
            successor = node.find_successor()
            successor.key, node.key = node.key, successor.key
            self.delete(successor)


class BST(object):
    """
    A Binary Search tree
    """
    def __init__(self):
        self.root = None

    def insert(self, node):
        """
        insert the node into the tree
        :param node: the node to be inserted
        :return: None
        """
        if not self.root:
            self.root = node
        else:
            self.root.insert(node)

    def search(self, k):
        """
        search the node with the key of k
        :param k:the key
        :return: the node with key else None
        """
        if not self.root:
            return None
        return self.root.search(k)

    def find_min(self):
        """
        find the node with minimum key of the tree
        :return: the node with minimum key
        """
        if not self.root:
            return None
        return self.root.find_min()

    def find_max(self):
        """
        find the node with maximum key of the tree
        :return: the node with maximum key
        """
        if not self.root:
            return None
        return self.root.find_max()

    def delete(self):

        if not self.root:
            return None
        return self.root.delete()