class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        
    def maxHeight(self, root):
        "Returns maximum height of a tree based on number of edges."
        if root is None:
            return -1
        lh = self.maxHeight(root.left)
        rh = self.maxHeight(root.right)
        return max(lh, rh) + 1
        
    def longestPathCrossingRoot(self, root):
        "Returns the longest path in a tree where crossing point is the root node."
        leftMaxPath = self.maxHeight(root.left)
        rightMaxPath = self.maxHeight(root.right)
        # if height of right subtree is None, add only one edge to the max path
        if leftMaxPath is not None and rightMaxPath is  None:
            return leftMaxPath + 1
        elif rightMaxPath is not None and leftMaxPath is None:
            return rightMaxPath + 1
        else:
            # If left and right nodes are present, add two edges in addition to the left and right sub tree max height.
            return rightMaxPath+leftMaxPath+2
        
        
        
# Example usage:
# Construct the example binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Create TreeNode instance and compute the longest path crossing the root
tree = TreeNode(0) 
print(tree.longestPathCrossingRoot(root)) 