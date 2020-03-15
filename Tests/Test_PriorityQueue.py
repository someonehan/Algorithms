import unittest
from src.DataStructure.priorityqueue import PriorityQueue, SortedPriorityQueue, HeapPriorityQueue


class Test_PriorityQueue(unittest.TestCase):
    def setUp(self):
        self.q = self._create_priorityQueue()

    def test_add_one(self):
        self.q.add(1, "hanxingzhi")
        self.assertEqual(1, len(self.q))

    def test_add_two(self):
        self.q.add(1, "hanxingzhi")
        self.q.add(2, "someone")
        self.assertEqual(2, len(self.q))

    def test_find_min(self):
        self.q.add(1, "hanxingzhi")
        self.q.add(2, "someone")
        (i, v) = self.q.min()
        self.assertEqual(1, i)
        self.assertEqual("hanxingzhi", v)

    def test_remove_min(self):
        self.q.add(1, "hanxingzhi")
        self.q.add(2, "someone")
        self.q.remove_min()
        self.assertEqual(1, len(self.q))

    def _create_priorityQueue(self):
        return PriorityQueue()


class Test_SortPriorityQueue(Test_PriorityQueue):
    def _create_priorityQueue(self):
        return SortedPriorityQueue()


class Test_HeapPriorityQueue(Test_PriorityQueue):
    def _create_priorityQueue(self):
        return HeapPriorityQueue()

if __name__ == "__main__":
    unittest.main()