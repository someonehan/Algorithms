import unittest
import random

"""
Quicksort with equal element values
"""
"""
1. suppose that all element values are equal
2. the partition procedure returns an index q such that each element of A[p...q-1] is less than
    or equal to A[q] and each element of A[q+1...r] is greater than A[q]
"""

class Solution:
    def quickSort(self, A, p, r):
        if p < r:
            q = self._partition(A, p, r)
            self.quickSort(A, p, q[0] - 1)
            self.quickSort(A, q[1] + 1, r)

    def _partition(self, A, p, r):
        """

        :param A: the original array to be sorted
        :param q: the start index
        :param r: the end index
        :return:  index of split element
        """

        key = A[r]
        i = p - 1
        j = p - 1
        for z in range(p, r):
            if A[z] < key:
                i += 1
                j += 1
                A[i], A[z] = A[z], A[i]
            if A[z] == key:
                j += 1
                A[j], A[z] = A[z], A[j]
        print(j + 1)
        A[r], A[j + 1] = A[j+1],A[r]
        return i + 1, j + 1

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_partition(self):
        A =  [2, 2, 4, 3]
        result = self.solution._partition(A, 0, len(A) - 1)
        self.assertEqual(result[0], 2)
        self.assertEqual(result[1], 2)

    def test_quickSort(self):
        # pass
        li = [2, 2, 4, 3]
        self.solution.quickSort(li, 0, len(li) - 1)
        self.assertEqual(li, [2,2,3,4])

if __name__ == "__main__":
    unittest.main()


