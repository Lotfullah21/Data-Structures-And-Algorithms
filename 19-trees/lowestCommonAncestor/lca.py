class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def LCA(self, root, n1, n2):
        # If the root is None, there is no tree to search, so return None
        if root is None:
            return None
        # If the current node is one of the nodes we are looking for, return it
        if root.val == n1 or root.val == n2:
            return root
        
        # Recursively search for n1 and n2 in the left and right subtrees
        left = self.LCA(root.left, n1, n2)
        right = self.LCA(root.right, n1, n2)
        
        # If both left and right are not None, n1 and n2 are found in different branches
        if left is not None and right is not None:
            return root
        
        # If only the left subtree contains either n1 or n2
        if left is not None:
            return left
        
        # If only the right subtree contains either n1 or n2
        if right is not None:
            return right
        
        # If neither subtree contains n1 or n2
        return None

# Example Usage
# Construct the binary tree
#       3
#      / \
#     5   1
#    / \ / \
#   6  2 0  8
#     / \
#    7   4

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

solution = Solution()

# Find the LCA of nodes 5 and 1
lca = solution.LCA(root, 5, 1)
print(f"The LCA of nodes 5 and 1 is: {lca.val}")  # Output: 3

# Find the LCA of nodes 1 and 8
lca = solution.LCA(root, 1, 8)
print(f"The LCA of nodes 1 and 8 is: {lca.val}")  # Output: 1

# Find the LCA of nodes 7 and 4
lca = solution.LCA(root, 7, 4)
print(f"The LCA of nodes 7 and 4 is: {lca.val}")  # Output 2
