"""
Given a binary tree, find the Postorder Traversal of it.
For Example, the postorder traversal of the following tree is:
5 10 39 1

        1
     /     \
   10     39
  /
5


Input:
          11
         /
       15
      /
     7
Output: 7 15 11

"""
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

#Function to return a list containing the inorder traversal of the tree. 
class Solution:
    def postOrder(self,root):
        inorder = []
        if root is not None:
            inorder+=self.postOrder(root.left)
            inorder+=self.postOrder(root.right)
            inorder.append(root.data)
        return inorder
    
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
inorder_result = solution.postOrder(root)

# Print the result
print("Post-order traversal:", inorder_result)