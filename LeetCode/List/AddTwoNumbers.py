# _*_ coding:utf-8 _*_
# author:hanxingzhi
# datetime:2018/10/26

import unittest
from .Common import ListNode

"""
given tow non_empty linked lists representing two non_negative integers, the digits are stored
in reverse order and each of their node contain a single digit, add the two numbers and return it
as a linked list.
"""

class Solution:
    def AddTwoNumbers(self, l1, l2):
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_AddTwoNumber_OneNode(self):
        l1 = ListNode(1)
        l2 = ListNode(2)
        ret = self.solution.AddTwoNumbers(l1, l2)
        self.assertEqual(ret.x, 3)

    def test_AddTwoNumber_TwoNodes(self):
        l1 = ListNode(2)
        l1.next = ListNode(2)
        l2 = ListNode(1)
        l2.next = ListNode(1)
        ret = self.solution.AddTwoNumbers(l1, l2)
        self.assertEqual(ret.x, 3)
        self.assertEqual(ret.next.x, 3)