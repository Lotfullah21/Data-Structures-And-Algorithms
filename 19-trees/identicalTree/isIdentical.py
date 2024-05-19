class Node:
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = None
        self.right = None



class Solution:
    def areIdentical(self, root1, root2):
        # If both of them are empty 
        if not root1 and not root2:
            return True
        # If one node is left on one side and the other side is empty.
        if not root1 or not root2:
            return False
        # If the values are not equal.
        if root1.data!=root2.data:
            return False
        
        return self.areIdentical(root1.left, root2.left) and self.areIdentical(root2.right, root1.right)
        
        
        
# Tree 1
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.right.right = Node(7)

# Tree 2 (identical to Tree 1)
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)
root2.right.left = Node(6)
root2.right.right = Node(7)

# Tree 3 (different from Tree 1)
root3 = Node(1)
root3.left = Node(2)
root3.right = Node(3)
root3.left.left = Node(4)
root3.left.right = Node(8)  
root3.right.left = Node(6)
root3.right.right = Node(7)



solution = Solution()
# Check if the trees are identical
print(solution.areIdentical(root1, root2)) 
print(solution.areIdentical(root1, root3))  