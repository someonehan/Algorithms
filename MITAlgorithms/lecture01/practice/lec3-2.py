from ..mergeSort import Solution
import unittest


class Solution(Solution):
    def merge(self, A, p, q, r):
        left = A[p : q + 1]
        right = A[q + 1 : r + 1]
        k = p
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            A[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            A[k] = right[j]
            k += 1
            j += 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge(self):
        li = [1,3,5,7,2,4,6,8]
        self.solution.merge(li,0, 3, 7)
        self.assertEqual([1,2,3,4,5,6,7,8], li)

if __name__ == "__main__":
    unittest.main()