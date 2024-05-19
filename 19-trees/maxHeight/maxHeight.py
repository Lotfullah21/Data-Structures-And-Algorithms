
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
  
def maxHeight(node):
    # base case, if it is the last node, the height is 0
	if node is None:
		return 0
	else:
		# call recursively until you reach the leaf on each side of the tree.
		leftHeight = maxHeight(node.left)
		rightHeight = maxHeight(node.right) 
		if (leftHeight > rightHeight):
			return leftHeight+1
		else:
			return rightHeight+1



root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.left.left = Node(60)
root.left.right.right = Node(70)


print(maxHeight(root))

