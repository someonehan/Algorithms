import unittest

class Solution:
    def kmp_matching(self,t,p):
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_kmp_matching(self):
        t = 'aaabbbccc'
        p = 'b'
        result = self.solution.kmp_matching(t,p)
        self.assertEqual(3,result)


if __name__ == "__main__":
    unittest.main()
