
"""
given an integer, generate all structurally unique BST's that store value 1...n

Example:
	input:3
	output:
	[
		[1, null, 2, 3]
		[3,2,null,1],
  		[3,1,null,null,2],
  		[2,1,3],
  		[1,null,2,null,3]
	]
"""


def generateTree( n):
	def generate(start, end):
		if start > end:
			return [None]
		alltrees = []
		for i in range(start, end + 1):
			left_trees = generate(start, i-1)
			right_trees = generate(i+1, end)
			#print(left_trees)
			#print(right_trees)
			for left in left_trees:
				for right in right_trees:
					root = type('Node', (object,), {'key':i})
					root.left = left
					root.right = right
				
					alltrees.append(root)
		return alltrees

	return generate(1, n) if n else []

def t_generateTree():
	result = generateTree(3)
	root_nodes = [item for item in result]


	def inorder(node):
		r = []
		current = node
		r.append(current.key)
		while current:
			if current.left:
				r.append(current.left.key)
			if current.right:
				r.append(current.right.key)
			current = current.left or current.right
		return r


	ans = []
	for root in root_nodes:
		ans.append(inorder(root))

	print(ans)


if __name__ == "__main__":
	t_generateTree()
