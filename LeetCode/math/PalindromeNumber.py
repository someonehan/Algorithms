import unittest

"""
Determine whether an integer is a palindrome,
an integer is a palindrome when it reads the same backward as forward
"""

"""
if reverse the integer and the value is equal the integer will be palindrome?
"""

class Solution:
    def PalindromNumber(self, val):
        if val < 0:
            return False

        def reverse(val):
            result = 0
            while val:
                pop = val % 10
                val = val // 10
                result = result * 10 + pop
            return result
        return val == reverse(val)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_PalindromNumber_true(self):
        val = 121
        result = self.solution.PalindromNumber(val)
        self.assertTrue(result)

    def test_PalindromNumber_False(self):
        val = -121
        result = self.solution.PalindromNumber(val)
        self.assertFalse(result)

    def test_PalindromNumber_False2(self):
        val = 2221
        result = self.solution.PalindromNumber(val)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()