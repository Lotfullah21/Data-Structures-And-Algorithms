"""
Complete the function search()which returns true if the node with value x is present in the BST else returns false.

Input:      20
             \ 
              41 
             / \ 
            40   44
X = 42
Output: False
Explanation: As 44 is not present in 
the given nodes , so the output will
be False.
Input:      20
             \ 
              41 
             / \ 
            40   44
X = 20
Output: True
Explanation: As 20 is not present in 
the given nodes , so the output will
be True.


"""


# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class BST:
    #Function to search a node in BST.
    def search(self, node, x):
        while node is not None:
            if node.data == x:
                return True
            elif node.data>x:
                node = node.left
            else: 
                node = node.right
        return False
        
root = Node(20)
root.left = Node(10)
root.right = Node(40)
root.right.right = Node(41)
root.right.left = Node(38)
root.right.right.right = Node(44)
solution = BST()
x = solution.search(root,41)
print(x)