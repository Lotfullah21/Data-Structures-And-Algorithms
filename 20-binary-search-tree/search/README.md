## Search in BST

Complete the function search()which returns true if the node with value x is present in the BST else returns false.

```plaintext


Input:     20
             \
              41
             / \
            40   44
X = 42
Output: False
Explanation: 42 is not present in the given tree.

Input:     20
             \
              41
             / \
            40   44
X = 20

Output: True
Explanation: 20 is present in the root node..
```

## Solution:

The above problem can be solved using two approaches.

#### Recursive approach

```py

    def searchBST(self, root, val):
        if not root:
            return None
        if root.data == val:
            return root
        elif root.data>val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
```

#### Analysis:

`Time Complexity`: `O(logN)`, in every call, the search space is divided into two parts.
`Space Complexity`: `O(h)`, because of recursive call stack.

## Iterative approach

Keep searching until you find the target element.
Every time, change the root to look for the target either on its left or right child.

## Algorithm:

```py
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
        return None
```

#### Analysis:

`Time Complexity`: `O(logN)`, in every call, the search space is divided into two parts.
`Space Complexity`: `O(1)`, no additional space is used.
