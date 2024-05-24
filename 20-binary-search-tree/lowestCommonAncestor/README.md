## Find Lowest Common Ancestor of Two Nodes:

Given a Binary Search Tree (with all values unique) and two node values n1 and n2 (n1!=n2). Find the Lowest Common Ancestors of the two nodes in the BST.

<h3><a href="https://www.geeksforgeeks.org/batch/dsa-python-self-paced/track/bst-advanced-python/problem/lowest-common-ancestor-in-a-bst">GFG</a></h3>
<h3><a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/">leetcode-235</a></h3>
Input:

```plaintext
   2
 /   \
1     3
Start at root (2): 1 is less than 2 and 3 is greater than 2. So, 2 is the LCA.
Output: 2.
```

Here's the algorithm to find the LCA:

### Algorithm:

Start from the root of the BST.

- If both n1 and n2 are smaller than the root's value, then the LCA lies in the left subtree.
- If both n1 and n2 are greater than the root's value, then the LCA lies in the right subtree.
- If one of n1 or n2 is equal to the root's value, or n1 and n2 lie on opposite sides of the root, then the current root is the LCA.

`Time Complexity`: `O(h)`, the number of operations depends on the height of a tree, if a tree's height is more, it means we need to do more operations until we reach the leaf node, we are traversing the linked list, but each time, cutting the search space to half.
`Space Complexity`: `O(1)`, No extra space is used.
