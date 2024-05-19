# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


def sizeOfTree(root: Node):
    if root==None:
        return 0
    else:
        leftSideSize = sizeOfTree(root.left)
        rightSideSize = sizeOfTree(root.right)
        return leftSideSize+rightSideSize+1
     

# Create the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(90)
root.left.right.right = Node(180)

print("size of tree =",sizeOfTree(root))
