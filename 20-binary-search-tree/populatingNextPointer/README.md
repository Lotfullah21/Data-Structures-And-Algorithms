## Populating Next Right Pointers in Each Node

Given a perfect binary tree, where each node has either zero or two children, the task is to populate each node's `next` pointer to point to its next right node. If there is no next right node, the `next` pointer should be set to `None`.

Input:

```plaintext

    8
   / \
  5   14
 / \ / \
4  6 13 16


```

After populating the `next` pointers, the tree should look like this:

```plaintext
    8 -> None
   / \
  5 ->14 -> None
 / \ / \
4->6->13->16 -> None

```

Output after printNext function should look like this

```plaintext
Node 8 -> Next None
Node 5 -> Next 14
Node 14 -> Next None
Node 4 -> Next 6
Node 6 -> Next 13
Node 13 -> Next 16
Node 16 -> Next None

```

## Solution Explanation

The solution uses a two-level nested loop to traverse the tree and set the `next` pointers for each node. Here's how it works:

1. Start with the root node.
2. For each level of the tree:
   - Traverse each node in the level.
   - For each node, set its left child's `next` pointer to its right child.
   - If the node has a right child and a next node, set its right child's `next` pointer to the left child of the next node.
3. Repeat this process for each level until the left child of the current level's nodes is `None`.

`Time Complexity`: `O(h)`, the number of operations depends on the height of a tree, if a tree's height is more, it means we need to do more operations until we reach the leaf node, we are traversing to each level to each node and setting its next pointer to be the right child of its parent.

`Space Complexity`: `O(1)`, No extra space is used.
