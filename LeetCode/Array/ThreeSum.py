# _*_ coding:utf-8 _*_
# author:hanxingzhi
# datetime:2018/10/24

import unittest
from ThreeSumClosest import ShortInputException

"""
Given an array nums of n integers, are there elements a, b, c in nums, such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero
"""
"""
if I want get a + b + c = 0
1. should sort the array
2. 
"""

class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            raise ShortInputException(len(nums), 3)

        nums.sort()
        start, end = 0, len(nums) - 1
        target_sum = 0
        for i in range(len(nums)):
            target_sum = nums[i] * -1;
            start = i + 1

            nums[start] + end

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_threeSum_exception(self):
        self.assertRaises(ShortInputException, self.solution.threeSum,[])

    def test_threeSum_example(self):
        pass


if __name__ == "__main__":
    unittest.main()