# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: [TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Initialize the firstIndex, secondIndex and previous node to be None.
        self.firstIdx = None
        self.secondIdx = None
        self.prev = None
        self.helper(root)
        # Swap the indices where the dip happened.
        temp = self.firstIdx.val
        self.firstIdx.val = self.secondIdx.val
        self.secondIdx.val = temp

    def helper(self,curr):
        if curr==None:
            return 
        self.helper(curr.left)
        # If it is the first time list has a dip, update both of the indices.
        if self.prev!=None and self.prev.val>curr.val and self.firstIdx==None:
            self.firstIdx = self.prev
            self.secondIdx = curr
        # If it is the second time the list has a dip
        elif self.prev!=None and self.prev.val>curr.val and self.firstIdx!=None:
            self.secondIdx = curr
        # Update the previous node
        self.prev = curr
        self.helper(curr.right)






        