
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

#Function to return a list containing the inorder traversal of the tree. 
class Solution:
    def InOrder(self,root):
        # code here
        inorder = []
        if root is not None:
            inorder+=self.InOrder(root.left)
            inorder.append(root.data)
            # print(root.data)
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