import unittest
from DataStructure.stackuse.stack import Stack



class Solution:
    def checkParens(self, text):
        parens = '{}()[]'
        open_parens = '{(['
        opposite = {'}':'{',')':'(',']':'['}

        def parentheses(text):
            start, len_ = 0, len(text)

            while True:
                while start < len_ and text[start] not in text:
                    start += 1
                if start >= len_:
                    break
                yield text[start]
                start += 1

        st = Stack(100)
        result = True;
        for x in parentheses(text):
            if x in open_parens:
                st.push(x)
            else:
                val = st.pop()
                if val != opposite[x]:
                    result = False
                    break
        if not st.stackEmpty():
            result = False
        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_checkParens_true(self):
        s = '[]'
        result = self.solution.checkParens(s)
        self.assertTrue(result)

    def test_checkParens_False(self):
        s = '[['
        result = self.solution.checkParens(s)
        self.assertFalse(result)

    def test_checkParens_False2(self):
        s = '[[]][[]](('
        result = self.solution.checkParens(s)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()