### Size Of A Tree

The size of a tree is total number of nodes present in a tree.

Input:

```plaintext
      1
     / \
    2   3
   / \
  4   5


```

Output: 5, because there are five nodes present in the tree.

`Time Complexity`: Each node is visited at least once, if there is `n` nodes, we are visiting `n` nodes. For each node, a constant amount of work is done: visit the left node, adding to the count.
So, `Time Complexity` will be `O(N)`.

`Space Complexity`: The only space we are using here is the call stack space where the functions are stored. At once, at maximum we can have `h` number of function from root node to leaf node, hence `Space Complexity`: `O(h)`.
