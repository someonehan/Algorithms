import unittest


class Solution:
    def insertSort(self, A):
        for i in range(1, len(A)):
            j = i
            key = A[j]
            while j > 0 and A[j - 1] > key:
                A[j] = A[j - 1]
                j -= 1
            A[j] = key

    def selectSort(self, A):
        for i in range(0, len(A)):
            key = A[i]
            for j in range(i, len(A)):
                if key > A[j]:
                    key, A[j] = A[j], key
            A[i] = key


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_insertSort(self):
        li = [2, 1, 4, 3]
        self.solution.insertSort(li)
        self.assertEqual(li, [1,2,3,4])

    def test_insertSort_equal(self):
        li = [2, 2, 4, 3]
        self.solution.insertSort(li)
        self.assertEqual(li, [2,2,3,4])

    def test_selectSort(self):
        li = [2, 1, 4, 3]
        self.solution.selectSort(li)
        self.assertEqual(li, [1, 2, 3, 4])

    def test_selectSort_equal(self):
        li = [2, 2, 4, 3]
        self.solution.selectSort(li)
        self.assertEqual(li, [2,2,3,4])


if __name__ == "__main__":
    unittest.main()
