# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        minVal = float("-inf")
        maxVal = float("inf")
        res = self.isBST(root, minVal, maxVal)
        return res

        
    def isBST(self, root, minVal, maxVal):
        if root==None:
            return True
        if root.val<minVal or root.val>maxVal:
            return False
        l = self.isBST(root.left, minVal, root.val -1)
        r = self.isBST(root.right, root.val+1, maxVal)
        if l== False or r == False:
            return False
        return True

# Example usage
if __name__ == "__main__":
    # Create a binary tree
    #      2
    #     / \
    #    1   3
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    solution = Solution()
    print(solution.isValidBST(root))  # Output: True

    # Create an invalid BST
    #      5
    #     / \
    #    1   4
    #       / \
    #      3   6
    newRoot = TreeNode(5)
    newRoot.left = TreeNode(1)
    newRoot.right = TreeNode(4)
    newRoot.right.left = TreeNode(3)
    newRoot.right.right = TreeNode(6)

    print(solution.isValidBST(newRoot))  # Output: False
