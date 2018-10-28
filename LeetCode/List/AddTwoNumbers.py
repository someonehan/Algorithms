# _*_ coding:utf-8 _*_
# author:hanxingzhi
# datetime:2018/10/26

import unittest
from .Common import ListNode

"""
given two non_empty linked lists representing two non_negative integers, the digits are stored
in reverse order and each of their node contain a single digit, add the two numbers and return it
as a linked list.
"""

class Solution:
    def AddTwoNumbers(self, l1, l2):
        carry = 0
        # the f represent the l1 node the s represent the l2 node
        # when loop f represent the l1 current node
        f, s = l1, l2
        # firstNode represent the head of the result, and the result is not include the firstNode
        # the currentNode represent current cursor
        firstNode = currentNode = ListNode(0)

        while f or s:
            x = f.value if f else 0
            y = s.value if s else 0
            sum = x + y + carry
            carry = sum // 10
            ret = sum % 10
            currentNode.next = ListNode(ret)
            currentNode = currentNode.next
            if f:
                f = f.next
            if s:
                s = s.next
        if carry:
            currentNode.next = ListNode(1)
        return firstNode.next


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_AddTwoNumber_OneNode(self):
        l1 = ListNode(1)
        l2 = ListNode(2)
        ret = self.solution.AddTwoNumbers(l1, l2)
        self.assertEqual(ret.value, 3)

    def test_AddTwoNumber_TwoNodes(self):
        l1 = ListNode(2)
        l1.next = ListNode(2)
        l2 = ListNode(1)
        l2.next = ListNode(1)
        ret = self.solution.AddTwoNumbers(l1, l2)
        self.assertEqual(ret.value, 3)
        self.assertEqual(ret.next.value, 3)

    def test_one_longer(self):
        l1 = ListNode(0)
        l1.next = ListNode(1)

        l2 = ListNode(0)
        next1 = ListNode(1)
        l2.next = next1
        next1.next = ListNode(2)

        ret = self.solution.AddTwoNumbers(l1, l2)
        self.assertEqual(0, ret.value)
        self.assertEqual(2, ret.next.value)


if __name__ == "__main__":
    unittest.main()