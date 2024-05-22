# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.greater = 0
        self.inOrderReverse(root)
        return root
    
    def inOrderReverse(self, root):
        if root==None:
            return 
        else:
            self.inOrderReverse(root.right)
            # Adding the current node to previous summations.
            self.greater = self.greater+root.val
            # Changing the value of the node.
            root.val = self.greater
            self.inOrderReverse(root.left)
            
            
# Example usage:
# Constructing the BST:
root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

# Converting BST to GST
solution = Solution()
gstRoot = solution.bstToGst(root)

# Print inOrder traversal after applying greater sum tree function.
def printInOrder(root):
    if root is not None:
        printInOrder(root.left)
        print(root.val, end=' ')
        printInOrder(root.right)

printInOrder(gstRoot)

