# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
        
minValue = float("-inf")
def maxNode(root: Node):
    if root==None:
        return minValue
    else:
        leftSideValue = maxNode(root.left)
        rightSideValue = maxNode(root.right)
        return max(root.data, leftSideValue, rightSideValue) 
     

# Create the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(90)
root.left.right.right = Node(180)

print("maximum node =",maxNode(root))
