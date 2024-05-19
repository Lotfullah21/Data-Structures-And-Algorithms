## Left View

The left view of a binary tree is the set of nodes visible when the tree is viewed from the left side

```plaintext

        1
       / \
      2   3
     / \ / \
    4  5 6  7

```

Output: [1,2,4].

## Solution:

The elements that are visible from left side are the first elements in their respective level.
So, add the first element of each level to the answer.

## Analysis:

`Time Complexity`: `O(N)`. For every node, we are doing two operations, appending to the queue and removing from queue and each of these operations takes constant time `O(1)`. For n nodes, we need to do `n` operations.

`Space Complexity`: `O(N)`. Maximum number of nodes we can have in the queue at a time cannot be more than total number of nodes present in the tree. To be precise, the maximum nodes in the queue will when we are inserting a level where it has maximum number of nodes among all levels, then it becomes `O(W)`, `W` is width of that level.
