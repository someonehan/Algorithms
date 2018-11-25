from DataStructure.LList import LNode
import unittest

"""
given a linked list, remove the n-th node from the end of list and return its head
"""

class Solution:
    def removeNthNodeFromEnd(self, head, index):
        l_len = 0
        n = head
        while n:
            n = n.next_
            l_len += 1

        current = n = head
        current_len = 0
        while n:
            current = n
            n = n.next_
            current_len += 1
            print((l_len - current_len + 1) == index)
            if (l_len - current_len + 1) == index:
                break
        return current


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_removeNthNodeFromEnd(self):
        head = LNode(1)
        node = head
        for i in range(2, 6):
            n = LNode(i)
            node.next_ = n
            node = n
        result = self.solution.removeNthNodeFromEnd(head, 2)
        self.assertEqual(4, result.elem)

if __name__ == "__main__":
    unittest.main()

