# _*_coding:utf-8_*_
# author = 'hanxingzhi'
# datetime = 2018/10/23

import unittest


class Solution:
    def maxArea(self, height):
        maxArea = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                maxArea = max(maxArea, min(height[i], height[j]) * (j - i))
        return maxArea

    def maxArea2(self, height):
        maxArea = 0
        start, end = 0, len(height) - 1
        while end > start:
            maxArea = max(maxArea, min(height[start], height[end]) * (end - start))
            # to get the max area
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return maxArea


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.min_array = [2, 2]
        self.example_array = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    def test_maxArea_min(self):
        result = self.solution.maxArea(self.min_array)
        self.assertEqual(2, result)

    def test_maxArea_example(self):
        result = self.solution.maxArea(self.example_array)
        self.assertEqual(49, result)

    def test_maxArea2_min(self):
        result = self.solution.maxArea2(self.min_array)
        self.assertTrue(2, result)

    def test_maxArea2_example(self):
        result = self.solution.maxArea2(self.example_array)
        self.assertEqual(49, result)


if __name__ == "__main__":
    unittest.main()