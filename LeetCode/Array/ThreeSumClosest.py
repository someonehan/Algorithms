# _*_ coding:utf-8 _*_
# author:hanxingzhi
# datetime:2018/10/23

import unittest

"""
given an array nums of n integers and target, find 3 interger in nums
such that the sum is closest to target. return the sum of the
3 integers, you may assume that each input would have excetly one solution
"""


class ShortInputException(Exception):
    def __init__(self, length, atleast):
        super().__init__(self)
        self.length = length
        self.atleast = atleast

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'array need {0} items but {1} given'.format(self.atleast,self.length)

class Solution:
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            raise ShortInputException(len(nums), 3)
        pass

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_threeSumClosest_one_integer(self):
        self.solution.threeSumClosest([], 1)
        self.assertRaises(ShortInputException)

    def test_threeSumClosest_three_Interger(self):
        pass

    def test_threeSumClosest_example(self):
        pass




if __name__ == "__main__":
    unittest.main()
