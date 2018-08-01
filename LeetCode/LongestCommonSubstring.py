import unittest
# https://en.wikipedia.org/wiki/Longest_common_substring_problem
# https://blog.csdn.net/wateryouyo/article/details/50917812

"""
Suffix Tree:
the longest common substrings of a set of string can be found by building a generalized suffix
tree, and then finding the deepest internal node which have leaf nodes from all the string in 
the subtree below it,

"""
class Solution:
    def findLongestCommonSubstring(self, s, t):
        """
        find the longest common substring between two strings
        :param s: first string
        :param t: 2th string
        :return: the longest common string
        """

        if len(s) == 0 or len(t) == 0:
            return ''
        m = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]
        max_len = 0
        p = 0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    m[i + 1][j + 1] = m[i][j] + 1
                    if m[i + 1][j + 1] > max_len:
                        max_len = m[i + 1][j + 1]
                        p = i + 1
        return s[p - max_len: p]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findLongestCommonSubstring(self):
        s = 'abcd'
        t = 'dabc'

        result = self.solution.findLongestCommonSubstring(s,t)
        self.assertEqual('abc', result)

    def test_findLongestCommonSubstring_empty(self):
        s = 'adfd'
        t = ''
        result = self.solution.findLongestCommonSubstring(s,t)
        self.assertEqual('', result)

    def test_findLongestCommonSubstring_Nomatch(self):
        s = 'asdf'
        t = 'hjkl'
        result = self.solution.findLongestCommonSubstring(s, t)
        self.assertEqual('', result)

if __name__ == "__main__":
    unittest.main()