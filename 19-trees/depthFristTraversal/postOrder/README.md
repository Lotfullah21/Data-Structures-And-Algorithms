## Post Order Traversal

Given a binary tree, return the nodes of the tree using post order traversal method.
For Example, the postOrder traversal of the following tree is:

```plaintext
5 10 39 1

        1
     /     \
   10     39
  /
5


Input:
          11
         /
       15
      /
     7
Output: 7 15 11


```

<h3><a href="https://leetcode.com/problems/binary-tree-postorder-traversal/description/">leetcode-145</a></h3>

## Analysis:

`Time Complexity`: Each node is visited at least once, if there is `n` nodes, we are visiting `n` nodes. For each node, a constant amount of work is done: visit the left node, add the root' data, and visit the right node.
So, `Time Complexity` will be `O(N)`.

`Space Complexity`: The only space we are using here is the call stack space where the functions are stored. At once, at maximum we can have `h` number of function from root node to leaf node, hence `Space Complexity`: `O(h)`.
