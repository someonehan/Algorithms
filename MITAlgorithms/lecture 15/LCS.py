import numpy as np
import unittest
import sys


class Solution:
    def __init__(self):
        pass

    def lcs_lenght(self, x, y):
        """
        get the lcs of x and y
        :param x: the source string of x
        :param y: the source string of y
        :return:
        """
        len_x, len_y = len(x), len(y)
        if len_x == 0 or len_y == 0:
            return 0
        if x[len_x - 1] == y[len_y - 1]:
            max_len = self.lcs_lenght(x[0:len_x - 1], y[0:len_y - 1]) + 1
        else:
            max_len = max(self.lcs_lenght(x, y[0:len_y - 1]), self.lcs_lenght(x[0:len_x - 1], y))

        return max_len

    def lcx_memorize(self, x, y):
        len_x, len_y = len(x), len(y)
        c = np.zeros((len_x, len_y), dtype=int)
        return self.lcs_lenght_dp(x, y, c)

    def lcs_lenght_dp(self, x, y, c):
        len_x, len_y = len(x), len(y)
        if len_x == 0 or len_y == 0:
            return 0
        if c[len_x -1][len_y-1] != 0:
            return c[len_x-1][len_y-1]

        len_x, len_y = len(x), len(y)
        if len_x == 0 or len_y == 0:
            return 0
        if x[len_x - 1] == y[len_y - 1]:
            max_len = self.lcs_lenght_dp(x[0:len_x - 1], y[0:len_y - 1], c) + 1
        else:
            max_len = max(self.lcs_lenght_dp(x, y[0:len_y - 1], c), self.lcs_lenght_dp(x[0:len_x - 1], y, c))

        c[len_x - 1][len_y - 1] = max_len
        return max_len

    def lcs_length_buttom_up(self, x, y):
        len_x, len_y = len(x), len(y)

        c = np.zeros((len_x + 1, len_y + 1), dtype=int)

        for i in range(1, len_x + 1):
            for j in range(1, len_y + 1):
                if x[i -1] == y[j -1]:
                    c[i][j] = c[i-1][j-1] + 1
                else:
                    c[i][j] = max(c[i-1][j], c[i][j-1])
        print(c)
        return c[len_x][len_y]




class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lcs_lenght_1(self):
        ret = self.solution.lcs_lenght('a', 'a')
        self.assertEqual(1, ret)

    def test_lcs_lenght_2(self):
        ret = self.solution.lcs_lenght('aa', 'a')
        self.assertEqual(1, ret)

    def test_lcs_lenght_3(self):
        ret = self.solution.lcs_lenght('BD', 'AB')
        self.assertEqual(1, ret)

    def test_lcs_lenght_4(self):
        ret = self.solution.lcs_lenght('BDB', 'ABB')
        self.assertEqual(2, ret)

    def test_lcs_lenght_5(self):
        ret = self.solution.lcx_memorize('ABCBD', 'BDCD')
        self.assertEqual(3, ret)

    def test_lcs_lenght_6(self):
        ret = self.solution.lcs_length_buttom_up('ABCBD', 'BDCDA')
        self.assertEqual(3, ret)


if __name__ == "__main__":
    unittest.main()