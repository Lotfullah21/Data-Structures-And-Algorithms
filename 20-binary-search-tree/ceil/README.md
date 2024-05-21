## Ceil of a node

Given a Binary search tree and a value X, the task is to complete the function which will return the ceil of x.

Note: Ceil(X) is an element that is either equal to X or immediately greater to X. If no such element exits return -1.

```
Input:
       8
     /  \
    5    11
   / \    \
  2   6   12

X = 11
Output: 11
Explanation: ceil of 11 in the given BST
is 11.

Input:
       4
     /   \
    3     5
        /  \
       4    8


X = 12
Output: -1
Explanation: No greater than 12 exits.
```

<h3><a href="https://www.geeksforgeeks.org/batch/dsa-python-self-paced/track/bst-basic-python/problem/implementing-ceil-in-bst">GFG</a></h3>

`Time Complexity`: `O(h)`, the number of operations depends on the height of a tree, if a tree's height is more, it means we need to do more operations until we reach the leaf node.
`Space Complexity`: `O(1)`.
