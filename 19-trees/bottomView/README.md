## Bottom View:

Given a binary tree. return the nodes that are visible when viewed from the bottom of the tree.

Input:

```plaintext

          20
        /    \
      8       22
    /   \        \
  5       3       25
        /   \
      10    14

```

Output: [5, 10, 3 ,14, 25]
Explanation: If the tree is viewed from bottom, we can see these nodes in front.

Input:

```plaintext
         10
       /    \
     20      30
    /  \
  40   60

```

OutputL [40, 60, 30]
Explanation: If the tree is viewed from bottom, we can see these nodes in front.

## Solution

All the explanations are the same as <a href="../19-trees/topView/README.md">top view</a> problem With the only difference and that, instead of checking whether the current key is present or not, we keep updating to get and keep the bottom nodes.

in top view:

```py
if idx not in nodeMap:
    nodeMap[idx] = node.data
```

in bottom view:

```py
# Every time, update the value corresponding to the current idx to get the nodes from bottom of the tree.
nodeMap[idx] = node.data
```
