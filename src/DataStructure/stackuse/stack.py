import unittest
from queue import PriorityQueue

"""
使用python来实现栈
"""

class Stack(object):
    def __init__(self, size, items = None):
        self.size = size
        self.top = 0
        self._items = []

    def pop(self):
        if self.stackEmpty():
            raise IndexError("empty stack")
        self.top -= 1
        return self._items.pop()

    def push(self, x):
        if self.stackFull():
            raise IndexError("stack full")
        self.top += 1
        self._items.append(x)

    def stackEmpty(self):
        return self.top == 0

    def stackFull(self):
        return self.top == self.size


class TestStack(unittest.TestCase):
    def test_push(self):
        s = Stack(2)
        s.push(1)
        s.push(2)
        self.assertFalse(s.stackEmpty())
        self.assertEqual(s._items[0], 1)
        self.assertEqual(s._items[1], 2)

    def test_pop(self):
        s = Stack(2)
        s.push(1)
        s.push(2)
        r1 = s.pop()
        self.assertEqual(2, r1)
        r2 = s.pop()
        self.assertEqual(1, r2)
        self.assertTrue(s.stackEmpty())

    def test_push_overflow(self):
        s = Stack(1)
        with self.assertRaises(IndexError):
            s.push(1)
            s.push(2)


if __name__ == "__main__":
    unittest.main()

