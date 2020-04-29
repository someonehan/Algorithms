#  Given a string s and a string t, check if s is subsequence of t.

# You may assume that there is only lower case English letters in both s and t. 
# t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

# A subsequence of a string is a new string which is formed from the original string by deleting some 
# (can be none) of the characters without disturbing the relative positions of the remaining characters. 
# (ie, "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
# s = "abc", t = "ahbgdc"

# Return true.

# Example 2:
# s = "axc", t = "ahbgdc"

# Return false.

# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, 
# and you want to check one by one to see if T has its subsequence. 
# In this scenario, how would you change your code?

# Credits:
# Special thanks to @pbrother for adding this problem and creating all test cases.

import unittest
from collections import defaultdict


class Solution:
    def isSubquence(self, s : str, t : str) -> bool:
        if len(t) < len(s):
            return False

        index = 0
        for i, c in enumerate(s):
            while t[index] != c:
                index += 1
                if index + len(s) - i - 1 >= len(t) or index >= len(t):
                    return False
        return True

    def isSubquence_followup(self, s : str, t : str) -> bool:
        if len(t) < len(s):
            return False

        s_index = defaultdict(list)
        for i, c in enumerate(t): s_index[c].append(i)

        now_index = 0
        for ch in s:
            if ch in s_index.keys():
                # 这个地方可以进行二分查找优化
                for i in s_index[ch]:
                    if i >= now_index:
                        now_index = i
                        break
                    else:return False
            else:
                return False
        return True

            

class test_Solution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_ex1(self):
        s = "abc"
        t = "ahbgdc"
        ret = self.s.isSubquence(s, t)
        self.assertTrue(ret)

    def test_ex2(self):
        ret = self.s.isSubquence("axc", "ahbgdc")
        self.assertFalse(ret)

    def test_exfollow1(self):
        s = "abc"
        t = "ahbgdc"
        ret = self.s.isSubquence_followup(s, t)
        self.assertTrue(ret)

    def test_exfollow2(self):
        ret = self.s.isSubquence_followup("axc", "ahbgdc")
        self.assertFalse(ret)

if __name__ == "__main__":
    unittest.main(exit=False)