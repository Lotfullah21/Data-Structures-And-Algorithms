

# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


def sumOfTree(root: Node) -> int:
    "returns sum of node values by traversing and calling each node."
    # base case
    if root is None:
        return 0
    # recursive calls.
    leftSum = sumOfTree(root.left)
    rightSum = sumOfTree(root.right)
    return leftSum + rightSum + root.data


# Create the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.right.right = Node(7)

print("size of tree =",sumOfTree(root))
