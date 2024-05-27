# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def inorderTraversal(self, root):
        curr = root
        res = []
        while curr is not None:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            # If root node has a left child.
            else:
                currp1 = curr.left
                # Cannot use or here, both of the conditions should be True to move to the right side.
                while currp1.right is not None and currp1.right is not curr:
                    currp1 = currp1.right
                # Make the connect between the right most node of left child and the current root.
                if currp1.right is None:
                    currp1.right = curr
                    # Move to left of current node.
                    curr = curr.left
                # IF currp1==curr
                
                else:
                    # Restore the order
                    currp1.right = None
                    # Process current node
                    res.append(curr.val)
                    # Move to the right of current node.
                    curr = curr.right
        return res
                    
        
        
def create_example_tree() -> TreeNode:
    # Creating the tree:
    #       1
    #        \
    #         2
    #        /
    #       3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    return root

# Create the example tree
example_tree = create_example_tree()

# Create a Solution object
solution = Solution()

# Perform Morris In-order Traversal
result = solution.inorderTraversal(example_tree)

# Print the result
print("In-order Traversal of the tree:", result)