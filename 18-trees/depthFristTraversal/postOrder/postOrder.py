
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

#Function to return a list containing the inorder traversal of the tree. 
class Solution:
    def MainPostOrder(self,root):
        result = []
        self.postOrder(root, result)
        return result
      
      
      
      
    def postOrder(self, root, result):
        if root==None:
          return 
        self.postOrder(root.left, result)
        self.postOrder(root.right, result)
        result.append(root.data)
      
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
inOrderList = solution.MainPostOrder(root)

# Print the result
print("Post-order traversal:", inOrderList)