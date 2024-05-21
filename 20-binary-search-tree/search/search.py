

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class BST:
    #Function to search a node in BST.
    def searchBST(self, node: TreeNode, val: int) ->TreeNode:
        while node is not None:
            if node.data == val:
                return True
            elif val<node.data:
                node = node.left
            else: 
                node = node.right
        # If node is not found, return None.
        return None
    

        
            
       
    
# Example Usage 
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(40)
root.right.right = TreeNode(41)
root.right.left = TreeNode(38)
root.right.right.right = TreeNode(44)
solution = BST()
val = solution.searchBST(root,41)
print(val)