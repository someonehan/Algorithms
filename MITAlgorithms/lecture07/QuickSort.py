import unittest
import random
"""
quick sort:
1. the running time fo quick sort depends on whether the partitions is balanced
or unbalanced, which in turn depends on which elements are used for partitioning
If the partitioning is balanced, the algorithm run as fast as mergesort
If the partitioning is unbalanced, it can run as slow as insertion sort.
"""

class Solution(object):
    """
    """
    def quickSort(self, A, p, r):
        """
        sort A use quick sort
        :param A: the array to be sorted
        :param p: the start index
        :param r: the end index
        :return: None
        """
        if p < r:
            q = self._parition(A, p, r)
            self.quickSort(A, p, q - 1)
            self.quickSort(A, q + 1, r)

    def _parition(self, A, p, r):
        key = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= key:
                i += 1
                A[j],A[i] = A[i],A[j]
        A[i + 1], A[r] = A[r], A[i + 1]
        print(i)
        return i + 1

    def _random_partition(self, A, p, r):
        """

        :param A:
        :param p:
        :param r:
        :return:
        """
        i = random.randint(p, r)
        A[i], A[r] = A[r], A[i]
        return self._parition(A, p, r)


class TestSolution(unittest.TestCase):
    """

    """
    def setUp(self):
        self.solution = Solution()

    def test_quickSort(self):
        li = [2, 2, 4, 3]
        self.solution.quickSort(li, 0, len(li) - 1)
        self.assertEqual(li, [2,2,3,4])

    def test_parition(self):
        li = [2, 2, 4, 3]
        result = self.solution._parition(li, 0, len(li) - 1)
        self.assertEqual(result, 2)



if __name__ == "__main__":
    unittest.main()