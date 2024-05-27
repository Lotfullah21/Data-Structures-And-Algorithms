## Morris Traversal

It is an efficient algorithm for in-order and pre-order traversal that does not use stack space unlike recursive approach.
It temporarily changes the structure of the tree to traverse back to the roots of subtrees.

It can be applied only to in-order and pre-order traversal, but for post order, there has to be double connection between each node and its left and right child which is an efficient approach.

`Time Complexity` is same as recursive approach (`O(N)`) and space complexity is reduced to `O(1)`.
