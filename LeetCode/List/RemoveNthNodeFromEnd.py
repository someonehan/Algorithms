from DataStructure.LList import LNode
import unittest

"""
given a linked list, remove the n-th node from the end of list and return its head
"""

class Solution:
    def removeNthNodeFromEnd(self, head, n):
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_removeNthNodeFromEnd(self):
        head = LNode(1)
        node = head.next_
        for i in range(2, 6):
            node = LNode(i)
            node.next_ = node.next_.next_
        result = self.solution.removeNthNodeFromEnd(head, 2)
        self.assertEqual(4, result.elem)

if __name__ == "__main__":
    unittest.main()

