#! _*_ coding:utf-8 _*_


def inorder_tree_walk(node, result):
    """inorder traversal a tree rooted as node

    Parameters:
    -----------
    Node : the tree node as root node
    """
    if node:
       # print(node.left.key)
       # print(node.right.key)
        inorder_tree_walk(node.left, result)
        result.append(node.key)
        inorder_tree_walk(node.right, result)

def inorder_tree_walk_iter(node):
	"""inorder traversal a tree rooted as node
	   iteration method

	Parameters:
	----------
	node : the tree node as root node
	"""	
	father_nodes = []
	current = node
	result = []
	while current or len(father_nodes) > 0:
		while current:
			father_nodes.append(current)
			current = current.left

		current=father_nodes.pop()
		result.append(current.key)
		current = current.right

	return result

class tree_node:
	def __init__(self,key, parent=None):
		self.parent = parent
		self.key = key
		self.right = None
		self.left = None

def create_tree():
	root = tree_node(3)
	left_sub = tree_node(4,root)
	root.left = left_sub

	right_sub = tree_node(5, root)
	root.right = right_sub

	left_left_l = tree_node(6, left_sub)
	left_sub.left = left_left_l

	left_left_r = tree_node(7, left_sub)
	left_sub.right = left_left_r

	return root

def test_inorder_tree_walk():

	result  = []
	root = create_tree()
	inorder_tree_walk(root, result)
	print(result)
	
def test_inorder_tree_walk_iter():
	root = create_tree()
	result = inorder_tree_walk_iter(root)
	print(result)

if __name__ == "__main__":
	test_inorder_tree_walk()
	test_inorder_tree_walk_iter()
