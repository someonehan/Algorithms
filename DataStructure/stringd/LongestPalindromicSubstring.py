import unittest

"""
give a string s, find the longest palindromic substring in s, you may assume that the maximum length of s is 1000
"""


class Solution:

    def LongestPalindromicSubstring(self, s):
        """
        this is the Brute Force method to find the longest palindromic substring of s
        the cost time is O(n3)
        :param s: the original string
        :return: the longest palindromic substring
        """
        result = ''
        for i in range(0, len(s)):
            for j in range(i + 1, len(s)):
                if self._isPalindromicString(s[i:j + 1]):
                    if len(result) < len(s[i:j+1]):
                        print('change')
                        result = s[i:j+1]
        return result


    def _isPalindromicString(self, s):
        len_ = len(s)
        if len_ % 2 == 0:
            left = len_ // 2 - 1
            right = len_ // 2
            result = True
            while left >= 0 and right < len_:
                if s[left] != s[right]:
                    result = False
                    break
                left -= 1
                right += 1
            return result
        else:
            left = right = len_ // 2
            result = True
            while left >= 0 and right < len_:
                if s[left] != s[right]:
                    result = False
                    break
                left -= 1
                right += 1
            return result

    def LongestPalindromicSubstring2(self,s):
        pass

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_LongestPalindromicSubstring(self):
        s = 'cbbd'
        result = self.solution.LongestPalindromicSubstring(s)
        self.assertTrue('bb', result)

    def test_LongestPalidromicSubstring_all(self):
        s = 'abcba'
        result = self.solution.LongestPalindromicSubstring(s)
        self.assertEqual('abcba', result)

    def test_isPalindromString_true(self):
        s = 'ssss'
        result = self.solution._isPalindromicString(s)
        self.assertTrue(result)

    def test_isPalindromString_false(self):
        s = 'abcd'
        result = self.solution._isPalindromicString(s)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
