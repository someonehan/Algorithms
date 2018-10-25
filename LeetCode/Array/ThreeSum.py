# _*_ coding:utf-8 _*_
# author:hanxingzhi
# datetime:2018/10/24

import unittest

from LeetCode.Array.ThreeSumClosest import ShortInputException



"""
Given an array nums of n integers, are there elements a, b, c in nums, such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero
"""
"""
if I want get a + b + c = 0
1. should sort the array
2. if we Duplicate removal before solving the problem whether can match(find all unique triplets)
"""

class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            raise ShortInputException(len(nums), 3)
        result = []
        nums.sort()
        nums = list(set(nums))
        target_sum = 0
        for i in range(len(nums)):
            target_sum = nums[i] * -1;
            start, end = i + 1, len(nums) - 1
            while end > start:
                if nums[start] + nums[end] == target_sum:
                    result.append([i, start, end])
                    break
                elif nums[start] + nums[end] > target_sum:
                    end -= 1
                else:
                    start += 1
        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_threeSum_exception(self):
        self.assertRaises(ShortInputException, self.solution.threeSum,[])

    def test_threeSum_example(self):
        result = self.solution.threeSum([-1, 0, 1])
        self.assertEqual([0, 1, 2], result[0])

    def test_threeSum_no_answer(self):
        result = self.solution.threeSum([1,2,3])
        self.assertEqual(0, len(result))

    def test_threeSum_unique(self):
        result = self.solution.threeSum([-1, 0, 1, -1])
        # should only get one result [0, 1, 2]
        self.assertEqual(1, len(result))
        self.assertEqual([0, 1, 2], result[0])


if __name__ == "__main__":
    unittest.main()