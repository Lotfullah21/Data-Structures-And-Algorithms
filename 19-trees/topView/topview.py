from collections import deque
class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None
        self.hd = 0
                
class Solution:     
    def topView(self, root):
        nodeMap = {}
        q = deque()
        res = []
        if not root:
            return []
        q.append((root, 0))
        while q:
            node,idx = q.popleft()
            # If the element with current distance is not in dictionary.
            if idx not in nodeMap:
                nodeMap[idx] = node.data
            if node.left:
                q.append((node.left, idx-1))
            if node.right:
                q.append((node.right, idx+1))
        # Sort the keys before appending, keys will be added as its origin order.
        for key in sorted(nodeMap.keys()):
            res.append(nodeMap[key])
        return res
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)
solution = Solution()
# Output: [2, 1, 3, 6]
print(solution.topView(root))  
        
        
        
        