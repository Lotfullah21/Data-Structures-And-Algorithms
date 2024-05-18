# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

#Function to return a list containing the preOrder traversal of the tree. 
class Solution:
    def mainPreOrder(self,root):
      result = []
      self.preOrder(root, result)
      return result
      
      
    def preOrder(self, root, result):
      if root==None:
        return
      else:
        result.append(root.data)
        self.preOrder(root.left, result)
        self.preOrder(root.right, result)
        
        
        
    
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
preOrderResult = solution.mainPreOrder(root)

# Print the result
print("Pre-order traversal:", preOrderResult)