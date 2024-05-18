### Pre Order

Given a binary tree, returns an array that consist of preOrder traversal of a tree.

"""

```plaintext


Input:
        1
      /
    4
  /    \
4       2
Output: 1 4 4 2


Input:
       6
     /   \
    3     2
     \   /
      1 2
Output: 6 3 1 2 2


```

<h3><a href="https://leetcode.com/problems/binary-tree-preorder-traversal/">leetcode-144</a></h3>

## Analysis:

`Time Complexity`: Each node is visited at least once, if there is `n` nodes, we are visiting `n` nodes. For each node, a constant amount of work is done: visit the left node, add the root' data, and visit the right node.
So, `Time Complexity` will be `O(N)`.

`Space Complexity`: The only space we are using here is the call stack space where the functions are stored. At once, at maximum we can have `h` number of function from root node to leaf node, hence `Space Complexity`: `O(h)`.
