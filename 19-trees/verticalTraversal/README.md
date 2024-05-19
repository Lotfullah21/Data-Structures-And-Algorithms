## Vertical View:

Given a binary tree, return its elements if the nodes are visited from top to bottom instead of left to right or right to left.
The nodes should be visited from left to right, but with vertical traversal.

Input:

```plaintext
   1
  / \
 2   3

```

Output: [[2],[1],[3]]
Input:

```plaintext
       1
      / \
     2   3
      \
       4
        \
         5
          \
           6


```

Output: [[2],[1,4],[3,5],[6]]

Input:

```plaintext
       1
      / \
     2   3
    / \
   4   5


```

Output: [[4],[2],[1,5],[3]]

Input:

```plaintext
        1
       / \
      2   3
     /     \
    4       5
   / \     / \
  6   7   8   9


```

Output: [[6],[4],[2,7],[1,3,8],[5],[9]]

## Idea

Solution is simple, use level order traversal and keep a dictionary. for every level,add all nodes corresponding to that level.
How to determine the level?
Use the distance variable which we used in top view.
