class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def printKthLevelNodes(root, k):
    # Base Case 
    if root is None:
        return 
    if k==0:
        print(root.data, end=",")
        return
    else:
        printKthLevelNodes(root.left, k-1)
        printKthLevelNodes(root.right, k-1)

# Example Usage:
# Constructing the following binary tree
#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

k = 2
print(f"Nodes at level {k} are:", end=' ')
printKthLevelNodes(root, k)
