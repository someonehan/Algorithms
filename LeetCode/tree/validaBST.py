"""
given a binary tree, determine if it is a valid binary search tree

Assume a bst is defined as follow:
	the left subtree of a node contain only nodes with keys less than the node'skey
	the right subtree of a node contain only nodes with keys greater that the node's key
	both the left and right subtrees must also be binary search tree

"""

def isvalidbsttree(node):
	def helper(node, lower = float('-inf'), upper = float('inf')):
		if not node:
			return True
		val = node.key
		if lower > val or upper < val:
			return False

		if not helper(node.left,lower, val):
			return False
		if not helper(node.right, val, upper):
			return False
		return True

	return helper(node)


def isvalidbsttree1(node):
	if not node:
		return True

	father_nodes = []
	current = node
	inorder = float('-inf')
	while current or len(father_nodes) > 0:
		while current:
			father_nodes.append(current)
			current = current.left

		current = father_nodes.pop()	
		if inorder > current.key:
			return False
		inorder = current.key
		current = current.right
	return True		

def create_tree():
	root = type("tree_node", (object, ), {'key':6, 'parent':None, 'left':None, 'right':None})
	left_sub = type("tree_node", (object,), {'key':4, 'parent':root, 'left':None, 'right':None})
	root.left = left_sub

	right_sub = type("tree_node", (object,), {'key':7, 'parent':root, 'left':None, 'right':None}) 

	root.right = right_sub

	left_left_l = type("tree_node", (object,), {'key':2, 'parent':root, 'left':None, 'right':None}) 

	left_sub.left = left_left_l

	left_left_r = type("tree_node", (object,), {'key':5, 'parent':root, 'left':None, 'right':None}) 

	left_sub.right = left_left_r

	return root

root = create_tree()
print(isvalidbsttree(root))

print(isvalidbsttree1(root))

