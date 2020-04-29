# Given two arrays, write a function to compute their intersection.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]

# Note:

#     Each element in the result must be unique.
#     The result can be in any order.

import unittest

class Solution:
    def set_intersection(self, set1, set2):
        return [s for s in set1 if s in set2]

    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) > len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)

    def intersection2(self, nums1, nums2):
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        ret = []
        fi = si = 0
        while fi < len(nums1) and si < len(nums2):
            left = nums1[fi]
            right = nums2[si]
            if left == right:
                ret.append(left)
                while left == nums1[fi] and fi < len(nums1) -1 : fi += 1
                while right == nums2[si] and si < len(nums2) -1: si += 1
                continue
            while nums1[fi] < right and fi < len(nums1) -1:
                fi += 1
            while nums1[si] > right and si < len(nums2) - 1:
                si += 1 
        return ret

class test_Solution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
    
    def test_one(self):
        ret = self.s.intersection([1,2,2,1], [2,2])
        self.assertEqual(1, len(ret))
        self.assertIn(2, ret)

    def test_two(self):
        ret = self.s.intersection([4,9,5], [9,4,9,8,4])
        self.assertEqual(2, len(ret))
        self.assertIn(4, ret)
        self.assertIn(9, ret)
        self.assertNotIn(5, ret)

    def test_one2(self):
        ret = self.s.intersection2([1,2,2,1], [2,2])
        self.assertEqual(1, len(ret))

    def test_two2(self):
        ret = self.s.intersection2([4,9,5], [9,4,9,8,4])
        self.assertEqual(2, len(ret))
        self.assertIn(4, ret)
        self.assertIn(9, ret)


if __name__ == "__main__":
    unittest.main()
    