"""
find the max totle value of subarray from the array

"""

# method 1
# split the array, the maximun subarray is in the left array right array and cross the left and right array

import sys
import unittest


class Solution:
    def findMaximumSubarray(self, a, start, end):
        if start == end:
            return (a[end], start, end)
        middle = (start + end) // 2
        (left_sum, left_min, left_max) = self.findMaximumSubarray(a, start, middle)
        (right_sum, right_min, right_max) = self.findMaximumSubarray(a, middle + 1, end)
        (middle_sum, middle_min, middle_max) = self.findMaximumSubarrayCorssArray(a, start, middle, end)
        if left_sum > right_sum and left_sum > middle_sum:
            return (left_sum, left_min, left_max)
        elif right_sum > left_sum and right_sum > left_sum:
            return (right_sum, right_min, right_max)
        else:
            return (middle_sum, middle_min, middle_max)

    def findMaximumSubarrayCorssArray(self, a, start, middle, end):
        left_sum = -sys.maxsize
        left_index = middle
        sum = 0
        for i in range(middle, start - 1, -1):
            sum = sum + a[i]
            if sum > left_sum:
                left_sum = sum
                left_index = i
        right_sum = -sys.maxsize
        right_index = middle
        sum = 0
        for j in range(middle, end + 1):
            sum = sum + a[j]
            if sum > right_sum:
                right_sum = sum
                right_index = j
        return (left_sum + right_sum - a[middle], left_index, right_index)

    def findMaximumCommon(self, a):
        max_sum = 0
        s = 0
        left_index, right_index = 0, 0
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                s = sum(a[i:j+1])
                if s > max_sum:
                    max_sum = s
                    left_index, right_index = i, j

        return (max_sum, left_index, right_index)

    # and there is another way find out the max subarray
    def findMaxSubarray(self, a):
        largest = -sys.maxsize
        current_sum = 0
        left_index = 0
        right_index = 0
        for i in range(len(a)):
            current_sum = current_sum + a[i]
            if current_sum > largest:
                largest = current_sum
                right_index = i
            if current_sum < 0:
                current_sum = 0
                left_index = i + 1
        return (largest, left_index, right_index)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findMaximumSubarrayCorssArray(self):
        l = [-1, -2, 3, 24, 2, -3, -3]
        result = self.solution.findMaximumSubarrayCorssArray(l, 0, 3, 6)
        self.assertEqual(29, result[0])
        self.assertEqual(2, result[1])
        self.assertEqual(4, result[2])

    def test_findMaximumSubarray(self):
        l = [-1, -2, 3, 24, 2, -3, -3]
        result = self.solution.findMaximumSubarray(l, 0, 6)
        self.assertEqual(29, result[0])
        self.assertEqual(2, result[1])
        self.assertEqual(4, result[2])


    def test_findMaximumCommon(self):
        l = [-1, -2, 3, 24, 2, -3, -3]
        result = self.solution.findMaximumCommon(l)
        self.assertEqual(29, result[0])
        self.assertEqual(2, result[1])
        self.assertEqual(4, result[2])

    def test_findMaxSubarray(self):
        l = [-1, -2, 3, 24, 2, -3, -3]
        result = self.solution.findMaxSubarray(l)
        self.assertEqual(29, result[0])
        self.assertEqual(2, result[1])
        self.assertEqual(4, result[2])


if __name__ == "__main__":
    unittest.main()