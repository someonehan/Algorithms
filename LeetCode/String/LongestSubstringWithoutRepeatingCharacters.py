import unittest

"""
Given a string, find the longest substring without repeating characters
"""


class Solution:
    def longSubstring(self, s):
        ans = 1
        for i in range(0, len(s) - 1):
            for j in range(i + 1, len(s) - 1):
                if self._allunique(s[i:j + 1]):
                    ans = max(ans, j - i + 1)

        return ans

    def longestSubstring2(self, str):
        s = set()
        ans = 0
        i = j = 0
        while i < len(str) and j < len(str):
            if str[j] in s:
                s.remove(str[i])
                i += 1
            else:
                s.add(str[j])
                j += 1
                ans = max(ans, j - i)
        return ans

    def _allunique(self, s):
        sset = set(s)
        return len(s) == len(sset)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_long_substring(self):
        str = 'abcabcbb'
        result = self.solution.longSubstring(str)
        self.assertEqual(3, result)

    def test_longestSubstring2(self):
        str = 'bbbbb'
        result = self.solution.longSubstring(str)
        self.assertEqual(1, result)

    def test_longestSubstring3(self):
        str = 'pwwkew'
        result = self.solution.longSubstring(str)
        self.assertEqual(3, result)

    def test_longestSubstring2(self):
        str = 'bbbbb'
        result = self.solution.longestSubstring2(str)
        self.assertEqual(1, result)

    def test_longestSubstring2_2(self):
        str = 'abcabcbb'
        result = self.solution.longestSubstring2(str)
        self.assertEqual(3, result)

    def test_longestSubstring2_3(self):
        str = 'pwwkew'
        result = self.solution.longestSubstring2(str)
        self.assertEqual(3, result)

if __name__ == "__main__":
    unittest.main()