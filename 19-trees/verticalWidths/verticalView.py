class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def verticalWidthUtil(root, pos, left, right):
    if root is None:
        return left, right
    
    left, right = verticalWidthUtil(root.left, pos - 1, min(left, pos - 1), right)
    left, right = verticalWidthUtil(root.right, pos + 1, left, max(right, pos + 1))
    
    return left, right

def verticalWidth(root):
    left, right = verticalWidthUtil(root, 0, 0, 0)
    return abs(left) + abs(right) + 1

# Example 1
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.right.right = Node(7)
root1.right.left.right = Node(8)
root1.right.right.right = Node(9)

print("Vertical Width of Example 1:", verticalWidth(root1))

# Example 2
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)

print("Vertical Width of Example 2:", verticalWidth(root2))
