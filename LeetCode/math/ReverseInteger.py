import unittest

"""
given a 320bit signed integer, reverse digits of an integer
"""


class Solution:
    def reverse(self, x):
        mulity = 1 if x >= 0 else -1

        x = abs(x)
        ret = 0
        while x > 0:
            pop = x % 10
            x = x // 10
            ret = ret * 10 + pop

        if ret > 2**32 -1:
            return 0

        return ret * mulity

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reverse(self):
        i = 123
        result = self.solution.reverse(i)
        self.assertEqual(321, result)

    def test_reverse_minus(self):
        i = -123
        result = self.solution.reverse(i)
        self.assertEqual(-321, result)


if __name__ == "__main__":
    unittest.main()

