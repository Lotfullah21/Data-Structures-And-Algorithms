## Find Lowest Common Ancestor of Two Nodes in a Binary Tree

Given a Binary STree (with all values unique) and two node values n1 and n2 (n1!=n2). Find the Lowest Common Ancestors of the two nodes in the binary tree.

<h3><a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/1266735113/">leetcode-236</a></h3>

Input:

```plaintext
   2
 /   \
1     3
Start at root (2): 1 is less than 2 and 3 is greater than 2. So, 2 is the LCA.
Output: 2.
```

Here's the algorithm to find the LCA:

`Time Complexity`: `O(n)`, the number of operations depends on the number of nodes in the tree and we have to look for every node until we found the target node.
`Space Complexity`: `O(h)`, a recursive call stack is created because of recursion and number of
