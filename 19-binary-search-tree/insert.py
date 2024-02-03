
"""

Add an element to a BST
If tree is empty create a new one with the given key
If key is already present, do not change anything; just return from the tree.
Insertion will be made at the leaf node.

Input:      20
             \ 
              41 
             / \ 
            40   44
X = 42 
Output:    20
             \ 
              41 
             / \ 
            40   44
                /
               42           


"""


# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class BST:
    #Function to search a node in BST.
   def insert(self,root, Key):
        if root == None:
            return Node(Key)
        elif root.data == Key:
            return root
        elif root.data>Key:
            root.left = self.insert(root.left, Key)
        else:
            root.right = self.insert(root.right, Key)
        return root
        
root = Node(20)
root.left = Node(10)
root.right = Node(40)
root.right.right = Node(41)
root.right.left = Node(38)
root.right.right.right = Node(44)
solution = BST()
x = solution.insert(root,41)
print(x)