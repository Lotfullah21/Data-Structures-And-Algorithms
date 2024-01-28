"""

Given a Binary Tree, find the In-Order Traversal of it.

Example 1:

Input:
       1
     /  \
    3    2
Output: 3 1 2

Input:
        10
     /      \ 
    20       30 
  /    \    /
 40    60  50
Output: 40 20 60 10 50 30

You don't need to read input or print anything.
Your task is to complete the function inOrder() that takes root node of the tree as input and returns a list containing the In-Order Traversal of the given Binary Tree.


"""


# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

#Function to return a list containing the inorder traversal of the tree. 
class Solution:
    def InOrder(self,root):
        inorder = []
        if root is not None:
            # concatenate the lists to the list you are getting from recursive calls.
            inorder+=self.InOrder(root.left)
            inorder.append(root.data)
            inorder+=self.InOrder(root.right)
        return inorder
    
#        1
#       / \
#      2   3
#     / \
#    4   5

#       2
 #     / \

# Create the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Create an instance of Solution class
solution = Solution()

# Get the in-order traversal
inorder_result = solution.InOrder(root)

# Print the result
print("In-order traversal:", inorder_result)