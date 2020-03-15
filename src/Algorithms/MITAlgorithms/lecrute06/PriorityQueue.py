import unittest
import itertools
import heapq


class PriorityQueue:

	REMOVEED = '<remove-task>'

	def __init__(self):
		self._queue = []
		self.entry_finder = {}
		self.counter = itertools.count()
		
	def push_task(self, task, priority=0):
		if task in self.entry_finder:
			self.remove_task(task)
		count = next(self.counter)
		entry = [-priority, count, task]
		self.entry_finder[task] = entry
		heapq.heappush(self._queue, entry)
		
	def remove_task(self, task):
		entry = self.entry_finder.pop(task)
		entry[-1] = PriorityQueue.REMOVEED
		
	def pop_task(self):

		while self._queue:
			priority, count, task = heapq.heappop(self._queue)
			if task != PriorityQueue.REMOVEED:
				del self.entry_finder[task]
				return task
		raise KeyError('pop from an empty heap')
		
class TestPriotiryQueue(unittest.TestCase):
	def setUp(self):
		self.priorityQueue = PriorityQueue()
		
	def test_push_task(self):
		self.priorityQueue.push_task('1')
		self.assertEqual('1', self.priorityQueue._queue[0][2])
		
	def test_pop_task(self):
		self.priorityQueue.push_task('2', 2)
		task = self.priorityQueue.pop_task()
		self.assertEqual('2', task)
		
		
if __name__ == "__main__":
	unittest.main()