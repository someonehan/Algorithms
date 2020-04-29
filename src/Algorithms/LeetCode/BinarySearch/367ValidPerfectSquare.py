# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: 16
# Output: true

# Example 2:

# Input: 14
# Output: false

import unittest
import sys

class Solution:
    def isPerfectSquare(self, num : int) -> bool:
        """
        判断一个数值是否是完全平方数
        """
        left = 0
        right = num / 2
        while left <= right:
            mid = (left + right) / 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
            else: left = mid + 1
        return False
        

class test_Solution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_16(self):
        ret = self.s.isPerfectSquare(16)
        self.assertTrue(ret)

    def test_14(self):
        ret = self.s.isPerfectSquare(14)
        self.assertFalse(ret)

    def test_49(self):
        ret = self.s.isPerfectSquare(49)
        self.assertTrue(ret)


if __name__ == "__main__":
    unittest.main(exit=False)

