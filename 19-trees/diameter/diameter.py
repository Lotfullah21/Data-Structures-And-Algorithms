class Solution:
    def __init__(self):
        self.ans = 0
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        # Code here
        self.height(root)
        # Adding 1, becuase its defined as the number of nodes and in height we are calculating number of edges. If it was defined based on # edges, no need to add 1.
        return self.ans+1
        
    def height(self, root):
        if root is None:
            return -1
        lh = self.height(root.left)
        rh = self.height(root.right)
        self.ans = max(self.ans, lh+rh+2)
        return max(lh, rh)+1
    
    
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Create nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Compute diameter
solution = Solution()
print(solution.diameter(root))  # Output: 4