from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        q = deque()
        RightView = [] 
        if root == None:
            return []
        q.append(root)
        while len(q) > 0:
            l = len(q)
            for i in range(l):
                curr = q.popleft()
                # Last element in the current level.
                if i == l - 1:
                    RightView.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return RightView

# Construct the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(7)

# Create a solution object
solution = Solution()

# Get the right side view
rightSideView = solution.rightSideView(root)
print("Right Side View of the tree:", rightSideView)  # Output: [1, 3, 6, 7]
