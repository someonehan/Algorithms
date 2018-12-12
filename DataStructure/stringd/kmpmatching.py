import unittest

class Solution:

    def kmp_matching(self, t, p):
        len_t, len_p = len(t), len(p)
        self.get_next(p)
        i = j = 0
        while i < len_t and j < len_p:
            if t[i] == p[j]:
                i += 1
                j += 1
            else:
                i += 1
                j = self.next[j]

        if j >= len_p:
            return i - j
        else:
            return -1

    def get_next(self,p):
        len_p = len(p)
        self.next = [0 for i in range(len_p)]
		
        k = 0
        for q in range(1,len_p):
            while k > 0 and p[q] != p[k]:
                k = next[k-1]
			
            if(p[q] == p[k]):
                k += 1
            self.next[q] = k
        return self.next


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_kmp_matching(self):
        t = 'aaabbbccc'
        p = 'b'
        result = self.solution.kmp_matching(t,p)
        self.assertEqual(3,result)

    def test_get_next_one(self):
        p = 'a'
        result = self.solution.get_next(p)
        self.assertEqual(0, result[0])

    def test_get_next_two_equal(self):
        p = 'ababab'
        result = self.solution.get_next(p)
        self.assertEqual(0, result[0])
        self.assertEqual(4, result[5])

    def test_get_next_equal(self):
        p = 'aaa'
        result = self.solution.get_next(p)
        self.assertEqual(0,result[0])
        self.assertEqual(1,result[1])
        self.assertEqual(2,result[2])


if __name__ == "__main__":
    unittest.main()
