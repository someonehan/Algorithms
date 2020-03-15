import unittest
import sys


class Solution:
    def merge(self, A, p, q, r):
        left, right = A[p:q + 1],A[q+1:r + 1]
        left.append(sys.maxsize)
        right.append(sys.maxsize)
        i = j = 0
        for k in range(p, r):
            if left[i] <= right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1

    def mergeSort(self, A, p, q):
        if p < q:
            mid = (p + q) // 2
            self.mergeSort(A, p, mid)
            self.mergeSort(A, mid + 1, q)
            self.merge(A, p, mid, q)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge(self):
        li = [1,3,5,7,2,4,6,8]
        self.solution.merge(li,0, 3, 7)
        self.assertEqual([1,2,3,4,5,6,7,8], li)

    def test_mergeSort(self):
        li = [1,3,5,7,2,4,6,8]
        self.solution.mergeSort(li,0 ,len(li) -1)
        self.assertEqual([1,2,3,4,5,6,7,8], li)

if __name__ == "__main__":
    unittest.main()
