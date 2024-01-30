# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    
    def levelOrder(self, root: Node):
        bigList = []
        
        if not root:
            return bigList
        
        queue = deque()
        queue.append(root)
        
        while queue:
            size = len(queue)
            localList = []
            
            for _ in range(size):
                node = queue.popleft()
                localList.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            bigList.append(localList)
        
        return bigList
# Create the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.right.right = Node(7)
solution = Solution()
x = solution.levelOrder(root)
print(x)