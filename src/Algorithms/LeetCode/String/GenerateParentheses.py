import unittest

"""
given n pairs of parentheses, writen a function to generate all combinations of well-formed parentheses
for example n = 3
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
class Solution:
    def generateParentheses(self, n):
        def generate(A=[]):
            if len(A) == n*2:
                if valid(A):
                    ans.append(''.join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            """
            check whether a sequence is valid,the net number of opening brackets minus closing
            brackets. if it falls below zero at any time or doesn't end in zero, the sequence is
            invalid--otherwise it is valid
            """
            balance = 0
            for c in A:
                if c == '(':
                    balance += 1  # matching opening brackets
                else:
                    balance -= 1  # matching closing brackets
                if balance < 0:
                    return False  # every time it falls below zero
            return balance == 0   # end in zero

        ans = []
        generate()
        return ans

    def generateParentheses_Backtracking(self, n):
        """

        :param n:
        :return:
        """
        ans = []
        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S, left, right + 1)

        backtrack()
        return ans

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_three_generateParentheses(self):
        result = self.solution.generateParentheses(3)
        self.assertTrue(5, len(result))

    def test_one_generateParentheses(self):
        result = self.solution.generateParentheses(1)
        self.assertTrue(1, len(result))

if __name__ == "__main__":
    unittest.main()