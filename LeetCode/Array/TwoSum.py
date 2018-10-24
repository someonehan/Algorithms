# _*_ coding:utf-8 _*_
# author:hanxingzhi
# datetime:2018/10/24

import unittest

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
'''

class Solution:
    def twoSum(self, nums, target):
        rst = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if target - nums[i] == nums[j]:
                    rst.append([i, j])
        return rst

    def twoSumTwoDict(self, nums, target):
        """
        in this method, the dict hold the whole nums's value and index.
        loop each item and get another item in the dict, if get return the index if not return
        :param nums: the integer array
        :param target: the sum of two integer
        :return: the index list
        """
        rst = []
        vidict = {nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in vidict.keys() and vidict[val] != i:
                rst.append([i, vidict[val]])
        return rst

    def twoSumDict(self, nums, target):
        """
        in this method, the dict only hold the not matched item
        :param nums: the integer array
        :param target: the sum of two integer
        :return: the index list
        """
        rst = []
        vidict = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in vidict.keys():
                rst.append([min(i, vidict[val]), max(i, vidict[val])])
            else:
                vidict[nums[i]] = i
        return rst


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_twoSum_two_nums(self):
        result = self.solution.twoSum([1,2], 3)
        self.assertTrue(type(result), list)
        self.assertTrue(type(result[0]), list)
        self.assertEqual(result[0][0], 0)
        self.assertEqual(result[0][1], 1)

    def test_twoSum_none_result(self):
        result = self.solution.twoSum([1, 2], 4)
        self.assertEqual(0, len(result))

    def test_twoSum_example_result(self):
        result = self.solution.twoSum([2, 7, 11, 15], 9)
        self.assertTrue(type(result), list)
        self.assertTrue(type(result[0]), list)
        self.assertEqual(result[0][0], 0)
        self.assertEqual(result[0][1], 1)

    def test_twoSum_with_some_result(self):
        result = self.solution.twoSum([2, 7, 11, 2], 9)
        self.assertTrue(type(result), list)
        self.assertTrue(type(result[0]), list)
        self.assertEqual(result[0][0], 0)
        self.assertEqual(result[0][1], 1)

        self.assertEqual(result[1][0], 1)
        self.assertEqual(result[1][1], 3)

    def test_twoSumTwoDict_two_nums(self):
        result = self.solution.twoSumTwoDict([1,2], 3)
        self.assertTrue(type(result), list)
        self.assertTrue(type(result[0]), list)
        self.assertEqual(result[0][0], 0)
        self.assertEqual(result[0][1], 1)

    def test_twoSumTwoDict_none_result(self):
        result = self.solution.twoSumTwoDict([1, 2], 4)
        self.assertEqual(0, len(result))

    def test_twoSumTwoDict_example_result(self):
        result = self.solution.twoSumTwoDict([2, 7, 11, 15], 9)
        self.assertTrue(type(result), list)
        self.assertTrue(type(result[0]), list)
        self.assertEqual(result[0][0], 0)
        self.assertEqual(result[0][1], 1)

    def test_twoSumTwoDict_with_some_result(self):
        result = self.solution.twoSumTwoDict([2, 7, 11, 2], 9)
        self.assertTrue(type(result), list)
        self.assertTrue(type(result[0]), list)
        self.assertEqual(result[0][0], 0)
        self.assertEqual(result[0][1], 1)

        self.assertEqual(result[1][0], 1)
        self.assertEqual(result[1][1], 3)

    def test_twoSumDict_two_nums(self):
        result = self.solution.twoSumDict([1,2], 3)
        self.assertTrue(type(result), list)
        self.assertTrue(type(result[0]), list)
        self.assertEqual(result[0][0], 0)
        self.assertEqual(result[0][1], 1)

    def test_twoSumDict_none_result(self):
        result = self.solution.twoSumDict([1, 2], 4)
        self.assertEqual(0, len(result))

    def test_twoSumDict_example_result(self):
        result = self.solution.twoSumDict([2, 7, 11, 15], 9)
        self.assertTrue(type(result), list)
        self.assertTrue(type(result[0]), list)
        self.assertEqual(result[0][0], 0)
        self.assertEqual(result[0][1], 1)

    def test_twoSumDict_with_some_result(self):
        result = self.solution.twoSumDict([2, 7, 11, 2], 9)
        self.assertTrue(type(result), list)
        self.assertTrue(type(result[0]), list)
        self.assertEqual(result[0][0], 0)
        self.assertEqual(result[0][1], 1)



if __name__ == "__main__":
    unittest.main()