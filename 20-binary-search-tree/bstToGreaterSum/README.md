## Binary Search Tree to Greater Sum Tree

Input:

```plaintext

       4
      / \
     1   6
    / \ / \
   0  2 5  7
        \   \
         3   8

```

Output:

```plaintext
      30
      / \
    36   21
    / \  / \
   36  33 26 15
        \    \
         36   8

```

<h2><a href="https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/">leetcode-1038</a></h2>

## Idea:

Using normal inOrder traversal, if the tree is a binary search tree the values will sorted in increasing order.
Now, if we can the traversal from right to left, then the values will be in sorted decreasing order.
At each iteration:

- Add the previous node's value to current node value.
- Keep that summation in a global variable
- Do these operations for all nodes.

Lets say our input is
input tree: [4,1,6,0,2,5,7,3,8]
inOrder tree: [0,1,2,3,4,5,6,7,8]
reverse inOrder: [8,7,6,5,4,3,2,1,0]

```
For node with value 0:
all numbers are greater than 0.
summation would be 8+7+6+5+4+3+2+1+0 = 36
For node with value 1:
summation would be 8+7+6+5+4+3+2+1= 36
For node with value 2:
summation would be 8+7+6+5+4+3+2= 34
For node with value 3:
summation would be 8+7+6+5+4+3+2= 33
For node with value 7:
summation would be 8+7 = 15
For node with value 8:
summation would be 8+0 = 0
```

```py
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.greater = 0
        def inOrderReverse(root):
            if root==None:
                return
            else:
                inOrderReverse(root.right)
                self.greater = self.greater+root.val
                root.val = self.greater
                inOrderReverse(root.left)
        inOrderReverse(root)
        return root


```

`Time Complexity`: `O(h)`, the number of operations depends on the height of a tree, if a tree's height is more, it means we need to do more operations until we reach the leaf node.
`Space Complexity`: `O(h)`, because of recursion call stack.
