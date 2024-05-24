## Diameter OF A Binary Tree:

he diameter of a binary tree is the length of the longest path between any two nodes in a tree.

Input:

```plaintext

      1
     / \
    2   3
   / \
  4   5

```

Output:4
Explanation: If we observe, the longest from one side to another side takes 4 nodes to finish.

<h3><a href="https://www.geeksforgeeks.org/problems/diameter-of-binary-tree/1?itm_source=geeksforgeeks">GFG</a></h3>

`Time Complexity`: Each node is visited at least once, if there is `n` nodes, we are visiting `n` nodes. For each node, a constant amount of work is done: visit the left node, add the root' data, and visit the right node.
So, `Time Complexity` will be `O(N)`.

`Space Complexity`: The only space we are using here is the call stack space where the functions are stored. At once, at maximum we can have `h` number of function from root node to leaf node, hence `Space Complexity`: `O(h)`.
