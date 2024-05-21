## Identical tree

Given two binary trees, find if both of them are identical or not

```plaintext


Tree-1:
    1
   / \
  2   3

Tree-2:
    1
   / \
  2   3



```

The above trees are identical.

<h3><a href="https://leetcode.com/problems/same-tree/">leetcode-100</a></h3>

## Solution:

A given tree is said to be identical if.

All elements on one side is equal to all elements on the other side, both data wise and in number of nodes.

They are not identical if:

- values are different in two sides.
- number of nodes are different.

Use a recursive approach and the base case should be when they are empty, return True.
Along the way check if:

- Base-Case-one: If both of them are empty, it is an identical tree
- Base-Case-two: If one is empty and the other still has some nodes, not an identical tree.
- Value-Check: If values of current nodes are different, not an identical tree.
