## InOrder Successor in Binary Search Tree:

```plaintext
      20
     /  \
   10   30
   / \   / \
  5  15 25  35

```

K = 10
Output: 15.
The just greater element than 10 is 15 which is on the left side of target k.

`Time Complexity`: `O(h)`, the number of operations depends on the height of a tree, if a tree's height is more, it means we need to do more operations until we reach the leaf node.
`Space Complexity`: `O(1)`.
