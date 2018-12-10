import unittest


'''
将原有的字符串翻转
method1: 使用列表的方式将原来字符串入队，然后pop出来
method2:
'''

class Solution:
    def reverse1(self, s):
        """将原有字符串翻转
        """
        l = list(s)
        result = ''
        while len(l) > 0:
            result += l.pop()
        return result

    def reverse2(self, s):
        return s[::-1]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reverse1(self):
        lstr = 'abcde'
        result = self.solution.reverse1(lstr)
        self.assertEqual('edcba',result)

    def test_reverse2(self):
        lstr = 'abcde'
        result = self.solution.reverse2(lstr)
        self.assertEqual('edcba', result)

if __name__ == "__main__":
    unittest.main()
