# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def deleteNode(self, root: TreeNode, key: int) ->TreeNode:
        if root is None:
            return None
        elif root.val<key:
            root.right = self.deleteNode(root.right, key)
        elif root.val>key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left==None and root.right==None:
                return None
            elif root.left is None and root.right is None:
                return root.left
            elif root.right is not None and root.left is None:
                return root.right
            else:
                # Traverse to the left subtree and find the max.
                maxNodeValue = self.findMax(root.left)
                # Swap the value of the node to be deleted with the node with max value.
                root.val = maxNodeValue
                # The node with max value is on the left subtree, go and delete it.
                root.left = self.deleteNode(root.left, maxNodeValue)
                # Return the root to the parent caller.
                return root
        return root
    # Find the node with maximum value on the right side of a node.
    def findMax(self, root):
        while root.right is not None:
            root = root.right
        return root.val
    
    
    
# Helper function for inorder traversal to print the tree
def inOrderTraversal(root):
    if root is None:
        return None
    if root:
        inOrderTraversal(root.left)
        print(root.val, end=' ')
        inOrderTraversal(root.right)

# Test the implementation
root = TreeNode(6)
root.left = TreeNode(5)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.left.right = TreeNode(3)

# Delete node with value 2
sol = Solution()
root = sol.deleteNode(root, 2)

# Print the tree inorder after deletion
inOrderTraversal(root)