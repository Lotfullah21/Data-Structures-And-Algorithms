## Top View:

Given a binary tree. return the nodes that are visible when viewed from the top.

Input:

```plaintext
      1
     / \
    2   3


```

Output: [2,1,3], all these nodes are visible when viewed from the top.

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

Output: [2,1,3,6], all these nodes are visible when viewed from the top.

```plaintext
          1
         / \
        2   3
       / \ / \
      4  5 6  7




```

Output: [4,2,1,3,7], all these nodes are visible when viewed from the top.

## Idea:

Two crucial point to note here.

Consider the root node as node that has zero distance from the root(itself).
Right child of a root node is one horizontal distance away from the root node, the distance is positive (+1).
Left child of a root node is one horizontal distance away from the root node, the distance is negative (-1).

Now, there are many nodes that will be having same distance from root node, which one to add?
We will be using dictionary to add only the roots that are visited for the first time and those are the ones visible from top.

Remember that the major difference with the other views here is that we are adding one extra value along the node to keep the distance from root node

## Steps:

1. Initialize a dictionary and a deque.
2. Add the root node with horizontal distance zero to the deque. (deque.append((root, 0)))
3. As long as there is element inside the deque.
   1. Pop from the left side of the deque and save the node and horizontal distance in two separate variables.
   2. Check if with the current distance, elements are there in dictionary.
      1. If not there:
         1. Add the node.data with the key being the horizontal distance.
      2. Check if any node is there to the left side of poped node, If there:
         1. Add it to the deque with horizontal distance -1 from the poped index. deque.append((node.left, -1))
      3. Check if any node is there to the right side of the poped node, If there:
         1. Add it to the deque with the horizontal distance of +1 from the poped index. deque.append((node.left, +1))
4. return the mapped node's data in sorted order.

```py
class Solution:
    def topView(self, root):
        nodeMap = {}
        q = deque()
        res = []
        if not root:
            return []
        q.append((root, 0))
        while q:
            node,idx = q.popleft()
            if idx not in nodeMap:
                nodeMap[idx] = node.data
            if node.left:
                q.append((node.left, idx-1))
            if node.right:
                q.append((node.right, idx+1))

        for key in sorted(nodeMap.keys()):
            res.append(nodeMap[key])

        return res

```

##

## Analysis:

`Time Complexity`: `O(NlogN + N)~O(NlogN)`. For every node, we are doing two operations, appending to the queue and removing from queue and each of these operations takes constant time `O(1)`.
For n nodes, we need to do `n` operations. But to get the node's data from left most to the right most, we have sort them. This will `O(KlogK)` for `K` elements in the dictionary, in worst case
for `n` elements, we will be doing `NlogN`

`Space Complexity`: `O(N)`. Maximum number of nodes we can have in the queue at a time cannot be more than total number of nodes present in the tree.
To be precise, the maximum nodes in the queue will when we are inserting a level where it has maximum number of nodes among all levels, then it becomes `O(W)`, `W` is width of that level.

## Idea-2:

We keep and `min-value and max-value` to get the min and max range. This allows to just use a range function and return the elements instead of sorting them separately.

```py

    def topView(self, root):
        nodeMap = {}
        q = deque()
        res = []
        if not root:
            return []
        q.append((root, 0))
        minValue = float("inf")
        maxValue = float("-inf")
        while q:
            node,idx = q.popleft()
            minValue = min(minValue, idx)
            maxValue = max(maxValue, idx)
            if idx not in nodeMap:
                nodeMap[idx] = node.data
            if node.left:
                q.append((node.left, idx-1))
            if node.right:
                q.append((node.right, idx+1))
        for i in range(minValue, maxValue+1):
            res.append(nodeMap[i])

        return res
```

## Analysis:

`Time Complexity`: `O(N)`. For every node, we are doing two operations, appending to the queue and removing from queue and each of these operations takes constant time `O(1)`.
For n nodes, we need to do `n` operations.

`Space Complexity`: `O(N)`. Maximum number of nodes we can have in the queue at a time cannot be more than total number of nodes present in the tree.
To be precise, the maximum nodes in the queue will when we are inserting a level where it has maximum number of nodes among all levels, then it becomes `O(W)`, `W` is width of that level.
