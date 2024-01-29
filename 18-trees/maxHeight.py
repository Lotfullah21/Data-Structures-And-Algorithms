"""
Given a binary tree, find its height.

Example 1:

Input:
     1
    /  \
   2    3
Output: 2
Example 2:

Input:
  2
   \
    1
   /
 3
Output: 3   

You don't need to read input or print anything. Your task is to complete the function height() which takes root node of the tree as input parameter and returns an integer denoting the height of the tree. If the tree is empty, return 0. 


"""
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

def inOrder(root):
    inorder = []
    if root is None:
        return []
    else:
        # concatenate the result of inOrder recursive call to the inorder list.
        inorder = inorder + inOrder(root.left)
        # add fthe current root.data to the inorder list
        inorder.append(root.data)
        # concatenate the result of inOrder calls to the inoder list.
        inorder = inorder + inOrder(root.right)
    # print(inorder)
    return inorder

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.left.left = Node(60)
root.left.right.right = Node(70)


print(maxHeight(root))
print(inOrder(root))
