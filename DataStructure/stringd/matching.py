import unittest

class Solution:
    def naive_matching(self,t, p):
        m, n = len(p), len(t)
        i = j = 0
        while i < n and j < m:
            if t[i] == p[j]:
                i, j = i + 1, j + 1
            else:
                j, i = 0, i - j + 1
        if j >= m:
            return n - i
        else:
            return -1


    def naive_matching2(self, t, p):
        """
        从匹配字符串中循环截区模式字符串的长度，如果截取的字符串和模式字符串相等即可认为匹配
        """
        len_p = len(p)
        last_index = len(t) - len(p)

        if last_index < 0:
            return -1

        for i in range(last_index):
            if t[i:len_p+i] == p:
                return i

        return -1



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        

    def test_naive_matching(self):
        t = 'ababab'
        p = 'ba'
        result = self.solution.naive_matching(t, p)
        self.assertEqual(3, result)

    def test_naive_matching2(self):
        t = 'aaabbbccc'
        p = 'a'
        result = self.solution.naive_matching2(t, p)
        self.assertEqual(0, result)

if __name__ == "__main__":
    unittest.main()
