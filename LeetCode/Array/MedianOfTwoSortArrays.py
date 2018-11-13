import unittest
import sys
"""
there are two sorted arrays nums1 and nums2 of size m and n respectively
find the median of the two sorted arrays, the overall run time complexity should be O(log(m+n))
assume nums1 and nums2 cannot be both empty
"""

class Solution:

    """
    there are two methods
    1. use the merge method to merge the two arrays and find the median value of the new arrays
    2. split nums1 and nums2 into two part, the left part is less than the right part
    """
    def MedianOfTwoArrays(self, nums1, nums2):
        total = len(nums1) + len(nums2)

        if total % 2 != 0:
            mid_left = mid_right = total // 2
        else:
            mid_left = total // 2 - 1
            mid_right = total // 2

        nums1.append(sys.maxsize)
        nums2.append(sys.maxsize)
        c = []
        i = j = 0
        for k in range(0, total):
            if nums1[i] <= nums2[j]:
                c.append(nums1[i])
                i += 1
            else:
                c.append(nums2[j])
                j += 1
        if mid_left and mid_right:
            return (c[mid_left] + c[mid_right]) / 2
        else:
            return None




class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_MedianOfTwoArrays(self):
        nums1 = [1,3]
        nums2 = [2]
        result = self.solution.MedianOfTwoArrays(nums1, nums2)
        self.assertEqual(result, 2.0)

    def test_MedianOfTwoArrays2(self):
        nums1 = [1,2]
        nums2 = [3,4]
        result = self.solution.MedianOfTwoArrays(nums1, nums2)
        self.assertEqual(2.5, result)

if __name__ == "__main__":
    unittest.main()