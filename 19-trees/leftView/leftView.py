
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def LeftView(root):
    q = deque()
    LeftView = []
    if root == None:
        return []
    q.append(root)
    while len(q) > 0:
        l = len(q)
        for i in range(l):
            curr = q.popleft()
            # The elements visible from left side are the first elements at each level.
            if i == 0:
                LeftView.append(curr.data)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return LeftView



# Helper function to construct the tree
def constructTree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root

# Construct the tree
root = constructTree()
# Get the left view
leftView = LeftView(root)
print("Left View of the tree:", leftView)  # Output: [1, 2, 4]
