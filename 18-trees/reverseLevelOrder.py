from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def reverseLevelOrder(self, node: TreeNode) -> list[int]:
        t = []
        if not node:
            return t
        
        stack = []
        queue = deque()
        queue.append(node)
        stack.append(node)
        while queue:
            temp = queue.popleft()
            if temp.right:
                queue.append(temp.right)
                stack.append(temp.right)
            if temp.left:
                queue.append(temp.left)
                stack.append(temp.left)

        while stack:
            temp = stack.pop()
            t.append(temp.val)





class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def reverseLevelOrder(node):
    t = []
    if not node:
        return t
        
    stack = []
    queue = deque()
    queue.append(node)
    stack.append(node)
    while queue:
        temp = queue.popleft()
        if temp.right:
            queue.append(temp.right)
            stack.append(temp.right)
        if temp.left:
            queue.append(temp.left)
            stack.append(temp.left)

    while stack:
        temp = stack.pop()
        t.append(temp.data)