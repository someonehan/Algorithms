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
    """
    new exception class that for the short length
    """
    def __init__(self, length, atleast):
        """
        init method
        :param length:the error length
        :param atleast:the min length
        """
        super().__init__(self)
        self.length = length
        self.atleast = atleast

    def __repr__(self):
        """
        override the __repr__ method
        :return:
        """
        return self.__str__()

    def __str__(self):
        """
        override the __str__ method for display the exception
        :return:
        """
        return 'array need {0} items but {1} given'.format(self.atleast,self.length)


class Solution:
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            raise ShortInputException(len(nums), target)

        nums = sorted(nums)

        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_threeSumClosest_one_integer(self):
        self.assertRaises(ShortInputException, self.solution.threeSumClosest,[], 2)

    def test_threeSumClosest_three_Interger(self):
        result = self.solution.threeSumClosest([-1, 2, 1], 1)
        self.assertTrue(2, result)

    def test_threeSumClosest_example(self):
        result = self.solution.threeSumClosest([-1, 2, 1, 4], 1)
        self.assertTrue(2, result)




if __name__ == "__main__":
    unittest.main()
