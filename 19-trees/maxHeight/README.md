## Maximum Height Of Tree

Given a binary tree, find the maximum height of a binary tree.

<h3><a href="https://www.geeksforgeeks.org/batch/dsa-python-self-paced/track/tree-basic-python/problem/height-of-binary-tree">leetcode-144</a></h3>

## Height:

Height of a tree is defined as number of nodes from root to leaf node in the longest path, or number of edges from root to leaf node in longest path.

## Analysis:

`Time Complexity`: Each node is visited at least once, if there is `n` nodes, we are visiting `n` nodes. For each node, a constant amount of work is done: visit the left node, add the root' data, and visit the right node.
So, `Time Complexity` will be `O(N)`.

`Space Complexity`: The only space we are using here is the call stack space where the functions are stored. At once, at maximum we can have `h` number of function from root node to leaf node, hence `Space Complexity`: `O(h)`.
