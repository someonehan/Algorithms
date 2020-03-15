"""
given two binary tree, write a function to check if they are the same or not
two binary trees are considersed the same if they are strucually and the nodes are the same value

"""

def issametree(a, b):
	if not a and not b:
		return True
	if not a or not b:
		return False
	if a.key != b.key:
		return False
	return issametree(a.left, b.left) and issametree(a.right, b.right)

from queue import Queue
def issametree2(a, b):
	def check(a, b):
		if not a and not b:
			return True

		if not a or not b:
			return False
		if a.key != b.key:
			return False
		return True
	deq = Queue([(a,b)])
	while deq:
		a, b = deq.get()
		if not check(a, b):
			return False
		if a:
			deq.put((a.left, b.left))
			deq.put((a.right, b.right))



