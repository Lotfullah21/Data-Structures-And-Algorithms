# Definition for a binary tree node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        if root is None:
            return None
        ans = root

        while root.left is not None:
            temp = root
            while temp is not None:
                temp.left.next = temp.right
                if temp.next is not None:
                    temp.right.next = temp.next.left
                temp = temp.next
            root = root.left
        return ans
