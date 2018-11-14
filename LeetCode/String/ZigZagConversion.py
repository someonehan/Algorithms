import unittest


"""
the string 'PAYPALISHIRING' is written in a zigzag pattern on a given number of rows like this
P   A   H   H
A P L S I I G
Y   I   R

and then read line by line 'PAHNAPLSIIGYIR'
"""

class Solution:
    def convert(self, s, rows):
        len_ = len(s)
        result = []
        radio = rows + rows - 2
        for i in range(rows):
            for j in range(0, len_, radio):
                if i + j < len_:
                    result.append(s[i + j])
                if i > 0 and i < rows - 1 and j + radio -i < len_:
                    result.append(s[radio + j - i])
        return ''.join(result)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_convert(self):
        s = 'PAYPALISHIRING'
        result = self.solution.convert(s, 3)
        self.assertEqual('PAHNAPLSIIGYIR', result)

    def test_convert2(self):
        s = 'PAYPALISHIRING'
        result = self.solution.convert(s, 4)
        self.assertEqual('PINALSIGYAHRPI', result)

if __name__ == "__main__":
    unittest.main()