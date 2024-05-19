### Level Order Traversal:

in this method, the elements are printed level vise.

First print all elements in first level, then 2nd level and so on, what do I mean by here could be explained in the following example.

<h3><a href="https://leetcode.com/problems/binary-tree-level-order-traversal/">leetcode-102</a></h3>

```plaintext
Input:
    1     ----- level 1
  /   \
 3     2  ----- level 2
Output:1 3 2

Example 2:
Input:

        10      ---- level 1
     /     \
    70      60  ---- level 2
  /   \
 80   90        ---- level 3
Output:10 70 60 80 90

```

### Solution:

- step one: Initialize a queue data structure and add root of the tree.
  As long as there is an element in queue, At each iteration do the following:
- Remove an element, removal should be based on queue data structure: first in, first out.
- Print the removed's data
- Add the child of removed element to the queue, if there is any.

`dequeue` is an efficient implementation of queue data structure that allows us to do insertion and deletion in constant time.
It has many methods like removing from front of the queue(`q.popleft()`), removing from end(`q.pop()`).

## Analysis:

`Time Complexity`: `O(N)`. For every node, we are doing two operations, appending to the queue and removing from queue and each of these operations takes constant time `O(1)`. For n nodes, we need to do `n` operations.

`Space Complexity`: `O(N)`. Maximum number of nodes we can have in the queue at a time cannot be more than total number of nodes present in the tree. To be precise, the maximum nodes in the queue will when we are inserting a level where it has maximum number of nodes among all levels, then it becomes `O(W)`, `W` is width of that level.
