from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        res = []
        if not root:
            return res
        q = deque()
        q.append(root)
        while q:
            ans = []
            sizeOfQueue = len(q)
            for _ in range(sizeOfQueue):
                node = q.popleft()
                ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(ans)
        return res
       

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