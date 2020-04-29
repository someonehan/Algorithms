# You have a total of n coins that you want to form in a staircase shape, 
# where every k-th row must have exactly k coins.

# Given n, find the total number of full staircase rows that can be formed.

# n is a non-negative integer and fits within the range of a 32-bit signed integer.

# Example 1:

# n = 5

# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤

# Because the 3rd row is incomplete, we return 2.

# Example 2:

# n = 8

# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤

# Because the 4th row is incomplete, we return 3.

import unittest

class Solution:
    # def arrangCoins(self, n : int) -> int:
    #     for i in range(1, n):
    #         total = (i + 1) * i / 2
    #         if n - total < i + 1:
    #             return i

    def arrangCoins(self, n : int) -> int:
        left = 1
        right = n
        while left < right:
            mid = int((left + right) / 2)
            total = (mid + 1) * mid / 2
            pre = total - mid
            sub = n - total
            if sub == mid + 1:
                return mid + 1
            elif  sub < mid + 1 and n - pre >= mid:
                return mid
            elif sub > mid + 1:
                left = mid + 1
            else:
                right = mid - 1
        return right


class test_Solution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # def test_input1(self):
    #     ret = self.s.arrangCoins(1)
    #     self.assertEqual(1, ret)
    
    # def test_input0(self):
    #     ret = self.s.arrangCoins(0)
    #     self.assertEqual(0, ret)

    def test_input5(self):
        ret = self.s.arrangCoins(10)
        self.assertEqual(4, ret)

    # def test_input8(self):
    #     ret = self.s.arrangCoins(8)
    #     self.assertEqual(3, ret)

if __name__ == "__main__":
    unittest.main(exit=False)
