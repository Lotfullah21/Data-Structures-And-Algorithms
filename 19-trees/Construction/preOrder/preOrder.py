from typing import List

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.inOrderMap = {}
        
    def buildTree(self, preOrder: List[int], inOrder: List[int]):
        if not preOrder or not inOrder:
            return None
        n = len(inOrder) - 1
        Is = 0
        ps = 0
        # Add corresponding indices of each inOrder item as key-value pair.
        
        for i in range(n+1):
            self.inOrderMap[inOrder[i]]=i
            
        ans = self.constructTree(preOrder, ps, n, inOrder, Is, n)
        return ans
        
    def constructTree(self, preOrder, ps, pe, inOrder, Is, Ie):
        if ps > pe or Is > Ie:
            return None
        # Get the root node from preOrder's first elements
        root = Node(preOrder[ps])
        # Find the corresponding value's index from preOrder list in inOrderMap which we saved earlier.
        idx = self.inOrderMap[preOrder[ps]]
        # Count how many nodes are there before the root node in inOrder list.
        count = idx - Is
        root.left = self.constructTree(preOrder, ps + 1, ps + count, inOrder, Is, idx - 1)
        root.right = self.constructTree(preOrder, ps + count + 1, pe, inOrder, idx + 1, Ie)
        return root

# Example Usage For checking.
preOrder = [1, 2, 4, 3, 5, 7, 8, 6]
inOrder = [4, 2, 1, 7, 5, 8, 3, 6]

solution = Solution()
root = solution.buildTree(preOrder, inOrder)

# Function to print the tree in order (for verification)
def printInOrder(node):
    if not node:
        return
    printInOrder(node.left)
    print(node.data, end=' ')
    printInOrder(node.right)

# Function to print the tree in preOrder (for verification)
def printpreOrder(node):
    if not node:
        return
    print(node.data, end=' ')
    printpreOrder(node.left)
    printpreOrder(node.right)

print("InOrder Traversal of Constructed Tree:")
printInOrder(root)
print("\npreOrder Traversal of Constructed Tree:")
printpreOrder(root)
