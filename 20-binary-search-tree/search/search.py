

# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class BST:
    #Function to search a node in BST.
    def searchBST(self, node, val):
        while node is not None:
            if node.data == val:
                return True
            elif node.data>val:
                node = node.left
            else: 
                node = node.right
        return False
    
    def searchBST(self, root, val):
        if not root:
            return None
        if root.data == val:
            return root
        elif root.data>val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
        
            
       
    
# Example Usage 
root = Node(20)
root.left = Node(10)
root.right = Node(40)
root.right.right = Node(41)
root.right.left = Node(38)
root.right.right.right = Node(44)
solution = BST()
val = solution.search(root,41)
print(val)