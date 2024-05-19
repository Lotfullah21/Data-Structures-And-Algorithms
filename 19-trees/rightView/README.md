## Left Side View

Given a binary tree, return the nodes that are visible from right side of the tree.

<h3><a href="https://leetcode.com/problems/binary-tree-right-side-view/submissions/1261824640/">leetcode-199</a></h3>

Input:

```plaintext

        1
       / \
      2   3
     / \ / \
    4  5 6  7

```

Output: [1, 3, 7]

Input:

```plaintext
         1
       /   \
      2     3
     / \   / \
    4   5 6   7
   / \   \   / \
  8   9   10 11 12
     /
    90
```

Output: [1, 3, 12,90]

Input:

```plaintext
         1
          \
           2
            \
             3
```

Output: [1,2,3]

## Solution:

The elements that are visible from right side are the the last elements at each level.

So, add the last element of each level to the answer.

##### How to add the last element.

Inside each level, when `i` is `len(q)-1`, it means we are at last iteration of that level.

## Analysis:

`Time Complexity`: `O(N)`. For every node, we are doing two operations, appending to the queue and removing from queue and each of these operations takes constant time `O(1)`. For n nodes, we need to do `n` operations.

`Space Complexity`: `O(N)`. Maximum number of nodes we can have in the queue at a time cannot be more than total number of nodes present in the tree. To be precise, the maximum nodes in the queue will when we are inserting a level where it has maximum number of nodes among all levels, then it becomes `O(W)`, `W` is width of that level.
