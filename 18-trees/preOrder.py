"""
Given a binary tree, find its preorder traversal.

Example 1:

Input:
        1      
      /          
    4    
  /    \   
4       2
Output: 1 4 4 2 


Input:
       6
     /   \
    3     2
     \   / 
      1 2
Output: 6 3 1 2 2 


You just have to complete the function preOrder() which takes the root node of the tree as input and returns an array containing the preOrder traversal of the tree.

"""


# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

#Function to return a list containing the preOrder traversal of the tree. 
class Solution:
    def PreOrder(self,root):
        preorder = []
        if root is not None:
            preorder.append(root.data)
            preorder.extend(self.PreOrder(root.left))
            preorder.extend(self.PreOrder(root.right))
        # print(preorder)
        return preorder
    
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
pre_result = solution.PreOrder(root)

# Print the result
print("Pre-order traversal:", pre_result)