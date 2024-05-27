### Binary Tree Inorder Traversal

Morris introduced an iterative approach to do Inorder traversal in a binary tree.

<h3><a href="https://leetcode.com/problems/binary-tree-inorder-traversal/">leetcode-144</a></h3>

The nodes are divided into two parts

### Nodes With No Left Child

If a root node does not have a left child, simple process it and move to the left of the root by changing the root to root.right.

### Node With Left Child:

If root node has left child, Find the right most node of its left child and make the connection between that node and current root node.

### Algorithm:

- Initialize with the root and assign to a temp variable for traversing purpose, because we don't want to change the original root node. (`curr = root`)
- As long as the root is not empty
  - Check if left child of current root is empty
  - If empty:
    - Process the current root node (`print(root.val)`)
    - Make the right child the root node (`curr = curr.right`)
  - If left child is not empty:
    - Initialize a node to be one step ahead of the current root to find the right most node of current root's left child (`currPlusOne = curr.left`)
    - Find the right most node of the left child, this node is the node that will be processed just before the root node (`while currp1.right is not None: currp1=currp1.right`)
    - If the right of the right most element is empty:
      - Change the structure of the tree by making right of the right most node to be the root node (`currPlusOne.right = curr`)
      - Move the current root to the left and make the current left to be the root node (`curr = curr.left`)
    - If the right of right most element is not empty:
      - Restore the tree by making its right to point to None (`currPlusOne.right = None`)
      - Process current root (`print(root.val)`)
      - Move to the right side by making its right child to be current root (`curr = crrr.right`)

## Recursive Approach

```py
    def inorderTraversal(self, root):
        res = []
        self._inorderTraversal(root,res)
        return res
    def _inorderTraversal(self, root, res) -> List[int]:
        if root!=None:
            self._inorderTraversal(root.left, res)
            res.append(root.val)
            self._inorderTraversal(root.right, res)
```

## Iterative Approach

```py

    def inorderTraversal(self, root):
        curr = root
        res = []
        while curr is not None:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            else:
                currp1 = curr.left
                while currp1.right is not None and currp1.right is not curr:
                    currp1 = currp1.right

                if currp1.right is None:
                    currp1.right = curr
                    curr = curr.left
                else:
                    currp1.right = None
                    res.append(curr.val)
                    curr = curr.right
        return res
```

## Analysis:

`Time Complexity`: in worse case, we are visiting each node tree times `O(3*N)=O(N)`
`Space Complexity`: except variable, no extra space have been used.
