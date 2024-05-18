from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def reverseLevelOrder(self, node: TreeNode) -> list[int]:
        result = []
        if not node:
            return result
        
        queue = deque([node])
        stack = deque()  # Using deque for efficient pop from the end
        
        while queue:
            current = queue.popleft()
            stack.append(current)
            
            # Enqueue right child first so left child is processed first during popping from stack
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
        
        while stack:
            result.append(stack.pop().val)
        
        return result

# Example Usage:
# Constructing the following binary tree
#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

tree = Tree()
print("Reverse Level Order Traversal:", tree.reverseLevelOrder(root))
