# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flattenHelper(self, root) -> None:
        self.flatten(root)
    
    def flatten(self, root):
        if root is None:
            return None
        
        lt = self.flatten(root.left)
        rt = self.flatten(root.right)
        
        if lt is None and rt is None:
            return root
        elif lt is None and rt is not None:
            return rt
        elif lt is not None and rt is None:
            lc = root.left
            root.right = lc
            root.left = None
            return lt
        else:
            lc = root.left
            rc = root.right
            root.right = lc
            root.left = None
            while lc.right is not None:
                lc = lc.right
            lc.right = rc
            return rt

# Helper function to print the flattened tree
def print_flattened_tree(root: TreeNode) -> None:
    current = root
    while current:
        print(current.val, end=" -> ")
        current = current.right
    print("None")

# Example usage
if __name__ == "__main__":
    # Construct the tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    
    # Flatten the tree
    solution = Solution()
    solution.flattenHelper(root)
    
    # Print the flattened tree
    print_flattened_tree(root)
