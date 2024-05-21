

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
        # if x<root.data, then we should move to the left side,we are looking for numbers just greater than x.
        elif x<root.data:
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
