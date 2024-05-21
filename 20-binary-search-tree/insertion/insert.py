# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    #Function to search a node in BST.
    def insertIntoBST(self, root, val: int):

        parent = None
        temp = root
        while temp is not None:
            parent = temp
            if val>temp.val:
                temp = temp.right
            else:
                temp = temp.left    
        newNode = TreeNode(val)
        if root is None:
            return newNode 
        if val>parent.val:
            parent.right = newNode
        else:
            parent.left = newNode  
        return root  
        
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(40)
root.right.right = TreeNode(41)
root.right.left = TreeNode(38)
root.right.right.right = TreeNode(44)
solution = Solution()
x = solution.insertIntoBST(root,41)
print(x)