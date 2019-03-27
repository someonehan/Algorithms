import sys
import unittest
import numpy as np
"""
1. 动态规划和分治法的区别
   动态规划应用于子问题重叠的情况
   分治法应用于子问题互不相交
2. 动态规划使用的方式是使用表格法，把子问题只求解一次然后将问题保存到表格中，从而无需每次都要重新计算

1. Characterize the structure of an optimal solution
2. Recursively define the value of an optimal solution
3. Compute the value of an optimal solution, typically in an bottom-up fashion
4. Construct an optimal solution from computed information
"""

class Solution:
    """
    链条切割问题
    给定一段长度为n英寸的钢条和一个价格表，求切割方案，使得收益r最大
    长度  1  2  3  4  5  6  7  8  9  10
    价格  1  5  8  9  10 17 17 20 24 30

    分析过程：
    1. 长度为n英寸的钢条共有 2（n-1）中切割方案。每一个英寸都有两种选择切割或者不切割。
    2. 那么1....n之间一定存在一个值k(1<=k<=n) (1...k之间不切割，k....n之间切割) 使得卖出的价格最高
    3. 解决方案可以是迭代的方式


    """

    def __init__(self):
        self.p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

    def get_max_price1(self, n):
        if n == 0:
            return 0
        max_price = -1
        # i 表示切割的长度
        for i in range(1, n + 1):
            max_p = self.p[i - 1] + self.get_max_price1(n-i)
            max_price = max(max_price, max_p)
        return max_price


    def get_max_price_memoized(self, n):
        c = np.zeros((n, 1))

    def get_max_price_bottom_up(self, n):
        c = [k for k in range(0, n+1)]
        for i in range(1, n + 1):
            q = -1
            for j in range(1, i + 1):
                q = max(q, self.p[j-1] + c[i-j])
            c[i] = q
        print(c)
        return c[n]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_get_max_price1(self):
        ret = self.solution.get_max_price1(1)
        self.assertEqual(1, ret)
    #
    def test_get_max_price1_2(self):
        ret = self.solution.get_max_price1(2)
        self.assertEqual(5, ret)

    def test_get_max_price1_10(self):
        ret = self.solution.get_max_price1(10)
        self.assertEqual(30, ret)

    def test_get_max_bottom_up(self):
        ret = self.solution.get_max_price_bottom_up(10)
        self.assertEqual(30, ret)

if __name__ == "__main__":
    unittest.main()