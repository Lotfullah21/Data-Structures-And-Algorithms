"""
Given a Binary search tree and a value X,  delete X from this tree.

we will be facing with three scenarios.
Scenario-one: if the node to be deleted is a leaf node, in this case just delete the leaf node.
the above case the easiest one as we do not require any more modification to our tree.


Input:                 
       8
     /  \
    5    11     
   / \    \
  2   6   12
X = 6


Output:
       8
     /  \
    5    11
   /       \
  2        12




Scenario-two: if the node to be deleted has one child, in this case delete the node and replace it with its child.

Input:                 
       8
     /  \
    5    11     
   / \    \
  2   6   12
X = 11
Delete 11 and replace it with its child which is 12.


Output:
       8
     /  \
    5    12
   /       
  2        

Scenario-three: if the node to be deleted have two children(left and right), in this case there is two option: replace the deleted node with the closest smallest node, or replace the deleted node
with closest larger value.
To find the minimum successor, go to right and find the smallest node. 


Output: 12
Explanation: ceil of 23 in the given BST
is 11

Input:
       4
     /   \
    3     5
        /  \
       4    8
    
Input:                 
       8
     /  \
    5    11     
   / \    \
  2   6   12
X = 5
Delete 5 and replace it with closest smaller child which is 2


Output:
       8
     /  \
    2    11     
    \    \
     6   12 

or 


Input:                 
       8
     /  \
    6    11     
   /       \
  2        12
  
Output: -1
Delete 5 and replace it with closest larger child which is 6.
you can find closest larger value of a node in in-order traversal, which is the next node after the current node.


"""



# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right



def getSuccess(root: Node) -> int:
    "go to the left most side of the first node on the right side of the node and return the node's value. that value is the closest value to the root node which is greater than root node.fffff"
    while root.left!=None:
        root = root.left
    return root.data

def deleteNode(root, X):
    # if root is empty or root is None, return without changing anything
    if root == None:
        return 
    # search in the left side
    elif root.data>X:
        root.left = deleteNode(root.left, X)
    # search in the right side
    elif root.data<X:
        root.right = deleteNode(root.right, X)
    # if root.key == X, 
    else:
      # if only one child, replace it with the right child
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        # if two child, replace with closest larger value.
        # that can be find using getSuccess function.
        else:
            successor = getSuccess(root.right)
            root.data = successor
            root.right = deleteNode(root.right, successor)
    return root



root = Node(20)
root.left = Node(10)
root.right = Node(40)
root.right.right = Node(41)
root.right.left = Node(38)
root.right.right.right = Node(44)
x = deleteNode(root,32)
print(x)
