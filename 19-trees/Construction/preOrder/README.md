## Construct Binary Tree from preOrder and inOrder Traversal

Given two integer arrays preOrder and inOrder where preOrder is the preOrder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

<h3><a href="https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/">leetcode-105</a></h3>

Input:

preOrder (Root-Left-Right): [1, 2, 4, 3, 5, 7, 8, 6]
inOrder (Left-Root-Right): [4, 2, 1, 7, 5, 8, 3, 6]

```plaintext
     1
    / \
   2   3
  /   / \
 4   5   6
    / \
   7   8


```

## Idea-1:

- From preOrder list, get the root node.
- Assign the that node value to variable (named root).
- Find the index of that root node in inOrder list.
- Make that index in inOrder as point of separation to the left and right node.
- Count how many elements are there in left side inOrder list, because we will be having the same amount for preOrder list.
- Counting can be the root's index in inOrder list minus 0th index in inOrder list (root's index in inOrder - starting index of inOrder list.)
- Elements up to that index in inOrder traversal goes to the left side's inOrder list.
- From 0th till the counts index, elements will go to preOrder of left side.

```py

class Solution:
    def buildTree(self, preOrder: List[int], inOrder: List[int]):
        if not preOrder or not inOrder:
            return None
        n = len(inOrder) - 1
        Is = 0
        ps = 0
        ans = self.constructTree(preOrder, ps, n, inOrder, Is, n)
        return ans

    def constructTree(self, preOrder, ps, pe, inOrder, Is, Ie):
        if ps > pe or Is > Ie:
            return None
        # Get the root node from preOrder's first elements
        root = Node(preOrder[ps])
        # Find the root node in inOrder list traversal to divide the lists for left and right nodes of the root node.
        idx = 0
        for i in range(Is, Ie + 1):
            # Do not if inOrder[i] == preOrder[ps], it creates an non-ending recursive calls.
            if inOrder[i] == root.data:
                idx = i
                break
        # Count how many nodes are there before the root node in inOrder list.
        count = idx - Is
        root.left = self.constructTree(preOrder, ps + 1, ps + count, inOrder, Is, idx - 1)
        root.right = self.constructTree(preOrder, ps + count + 1, pe, inOrder, idx + 1, Ie)
        return root

```

## Analysis:

Basically, we are doing two tasks.

### Finding the root in inOrder array:

For each subtree, we need to search for its root in inOrder array, This operation takes `O(N)` time in the worst case.

### Splitting the tree into left and right subtree.

Each node in tree is visited once and one recurse call is made for each node and for `n` nodes, This operation takes `O(N)` time.

`Time Complexity:` `O(N)*O(N)=O(N^2)`
`Space Complexity:` `O(N)`, to save the recursive calls in a stack.

## Idea-2:

Use a map to save the index and values of each element in inOrder tree, later we use this hashmap directly inside our recursive function to find the root's index in inOrder list.

```py

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        # Initialize a dictionary to save the index of inOrder items.
        self.inOrderMap = {}

    def buildTree(self, preOrder: List[int], inOrder: List[int]):
        if not preOrder or not inOrder:
            return None
        n = len(inOrder) - 1
        Is = 0
        ps = 0
        # Add corresponding indices of each inOrder item as key-value pair.
        # The indices are saved as value to the values of inOrder elements.
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

        count = idx - Is
        root.left = self.constructTree(preOrder, ps + 1, ps + count, inOrder, Is, idx - 1)
        root.right = self.constructTree(preOrder, ps + count + 1, pe, inOrder, idx + 1, Ie)
        return root

```

`Time Complexity:` `O(N)`, looking for an element in a dictionary takes `O(1)` time.
`Space Complexity:` `O(N)`, to save the recursive calls in a stack.
