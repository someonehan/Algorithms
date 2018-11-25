import unittest

"""
given an integer, convert it to a roman numeral
input is guaranteed to be within the range from 1 to 3999
"""

values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]


class Solution:
    def IntToRoman(self, num):
        pass

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_IntToRoman(self):
        val = 1
        result = self.solution.IntToRoman(val)
        self.assertEqual('I', result)

if __name__ == "__main__":
    unittest.main()