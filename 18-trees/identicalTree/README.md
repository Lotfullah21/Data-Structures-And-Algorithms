## Identical tree

Given two binary trees, find if both of them are identical or not

## Solution:

A given tree is said to be identical if.

All elements on one side is equal to all elements on the other side.

They are not identical if:
values are different in two sides.
number of nodes are different.

Use a recursive approach and the base case should be when they are empty, return True.
Along the way check if:
The values for both nodes are equal on the left side.
One of them is empty and other one still got a node.
