"""
Given a Binary search tree and a value X,  the task is to complete the function which will return the floor of x.

Note: Floor(X) is an element that is either equal to X or immediately smaller to X. If no such element exits return -1.


Input:
       8
     /  \
    5    11
   / \    \
  2   6   12
X = 11
Output: 11
Explanation: Floor of 11 in the given BST
is 11

Input:
       4
     /   \
    3     5
        /  \
       4    8
    

X = 1
Output: -1
Explanation: No smaller element exits


"""

# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right



def floor(root: Node,x: int) -> int:
    # it is our initial answer if all numbers are greater than x.
    answer = -1
    # traverse through the list until you hit the None
    while(root!=None):
        # if root is == x, then the root itself is the floor
        if root.data == x:
            return root.data
        # if root.data>x, then we should move to the left side, because floor of a number cannot be a number greater than itself.
        elif root.data>x:
            root = root.left
        # answer is in the place where the current node becomes < x.
        else:
            # keep an eye on the answer, if you cannot find the closest smaller number, keep the best of them
            answer = root.data
            # move to the side of current root.
            root = root.right
    return answer


root = Node(20)
root.left = Node(10)
root.right = Node(40)
root.right.right = Node(41)
root.right.left = Node(38)
root.right.right.right = Node(44)
x = floor(root,32)
print(x)
