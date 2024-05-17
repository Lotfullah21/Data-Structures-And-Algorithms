
from typing import List

# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

#Function to return a list containing the inorder traversal of the tree. 
class Solution:
    def inorderTraversal(self, root) -> List:
        res = []
        self.inOrderHelper(root,res)
        return res
    def inOrderHelper(self, root, res):
        if root!=None:
            self.inOrderHelper(root.left, res)
            res.append(root.data)
            self.inOrderHelper(root.right, res)
    
#        1
#       / \
#      2   3
#     / \
#    4   5


# Create the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Create an instance of Solution class
solution = Solution()

# Get the in-order traversal
inorder_result = solution.inorderTraversal(root)

# Print the result
print("In-order traversal:", inorder_result)