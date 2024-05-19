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

### Note:

If there are elements at the same level and their distance is also the same, based on the question we can update our approach.
If the requirement is to return the left most element, then use this approach.
First update the right side, then the left side.

```py
class Solution:
    def bottomView(self, root):
        nodeMap = {}
        q = deque()
        res = []
        if not root:
            return []
        q.append((root, 0))
        while q:
            node,idx = q.popleft()
            # Every time, update the value corresponding to the current idx to get the nodes from bottom of the tree.
            nodeMap[idx] = node.data
            # First, right side
            if node.right:
                q.append((node.right, idx+1))
            # Second, left side
            if node.left:
                q.append((node.left, idx-1))
        # Sort the keys before appending, keys will be added as its origin order.
        for key in sorted(nodeMap.keys()):
            res.append(nodeMap[key])
        return res

```
