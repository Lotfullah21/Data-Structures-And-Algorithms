## Print Kth nodes from a given node

Given a binary tree, print the kth distance node from a the root node. This distance can be considered as the level of the node. For instance if the k==0, it means the 0th level which will be the root itself, if k=1, it means the nodes that are one level below root node, and if k=2, it means the nodes that are 2 level below root node.

## Solution:

We start from K and every time, we reduce the `K` by one to reach to the kth level, once the distance becomes zero, all the elements at that distance are our answer.
