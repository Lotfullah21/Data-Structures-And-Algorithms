"""
size of a tree have been defined as the number of nodes in a tree.
use a recursive method to find it.

"""

# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


def size(root: Node) -> int:
    "returns number of nodes by traversing and calling each node."
    # base case
    if root is None:
        return 0
    # recursive calls.
    leftSize = size(root.left)
    rightSize = size(root.right)
    return leftSize + rightSize + 1


# Create the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(90)
root.left.right.right = Node(180)

print("size of tree =",size(root))
