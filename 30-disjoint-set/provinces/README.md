# Number of Provinces

<h2><a href="https://leetcode.com/problems/number-of-provinces/description/">leetcode</a></h2>

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

```py

isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

```

## Approach

### Union-Find Operations:

For i = 0:

j = 1: isConnected[0][1] = 1 (nodes 0 and 1 are connected).

### Call self.union(0, 1, par, rank):

Find roots:
find(0, par) → 0
find(1, par) → 1
Union nodes 0 and 1:
par becomes [0, 0, 2] (Node 1’s parent becomes 0).
rank becomes [1, 0, 0] (rank of node 0 is incremented).
j = 2: isConnected[0][2] = 0 (nodes 0 and 2 are not connected).

No union operation needed.
For i = 1:

j = 2: isConnected[1][2] = 0 (nodes 1 and 2 are not connected).
No union operation needed.
For i = 2: The inner loop does not run since j starts from 3 (out of bounds).

### Finding Unique Roots:

After processing all edges, the par array is [0, 0, 2].

### Finding unique roots:

find(0, par) → 0 (root of 0 is 0)
find(1, par) → 0 (path compression makes root of 1 become 0)
find(2, par) → 2 (root of 2 is 2)
Unique roots: {0, 2}

Therefore, there are 2 connected components.

### Analysis:

Time Complexity: O(n^2) due to the nested loops.
Space Complexity: O(n) for the parent and rank arrays
