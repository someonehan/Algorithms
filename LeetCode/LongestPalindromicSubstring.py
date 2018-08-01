import unittest
"""
giving a string s, find the longest palindromic substring of s
"""

class Solution:
    def findLongestPalidromic(self, s):
        current = ''

        for index in range(0, len(s) - 1):
            s[index]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findLongestPalidromic_common(self):
        s = 'aba'
        r_len, r_str = self.solution.findLongestPalidromic(s)
        self.assertEqual(len(s), r_len)
        self.assertEqual(s, r_str)

    def test_findLongestPalidromic_in(self):
        s = 'caba'
        r_len, r_str = self.solution.findLongestPalidromic(s)
        self.assertEqual(3, r_len)
        self.assertEqual('aba', r_str)

if __name__ == "__main__":
    unittest.main()
