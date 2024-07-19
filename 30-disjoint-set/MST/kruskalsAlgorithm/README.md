# Minimum Spanning Tree

<h2><a href="https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1?utm_source=geeksforgeeks">GFG-Spanning Tree</a></h2>

Given a weighted, undirected, and connected graph with V vertices and E edges, your task is to find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the graph. The graph is represented by an adjacency list, where each element adj[i] is a vector containing pairs of integers. Each pair represents an edge, with the first integer denoting the endpoint of the edge and the second integer denoting the weight of the edge.

# Approach

## Minimum Spanning Tree

`A Minimum Spanning Tree (MST)` of a connected, undirected graph is a subset of the edges that connects all the vertices together, without forming any cycles, and with the minimum possible total edge weight.

- Convert a graph into a tree, if we have `V` vertices, `E` would be `V-1`.
- No cycle should be formed
- If there are multiple spanning tree, choose the one with min weights.

# Kruskal's Algorithm:

### Steps of Kruskal’s Algorithm:

- Sort All Edges: List all edges in the graph and sort them by their weights in ascending order.

- Initialize: Create an empty set for the MST. Also, initialize a Union-Find data structure to keep track of which vertices are in which components.

- Add Edges: Iterate through the sorted edges and add each edge to the MST if it doesn’t form a cycle (i.e., it connects two different components).

- Check Cycles: Use the Union-Find data structure to check if adding an edge would create a cycle. If it would, skip the edge. Otherwise, add it to the MST and union the two components.

- Repeat: Continue the process until you have V−1 edges in the MST, where V is the number of vertices.

## Example

```text
    1
  A---B
  |   |
  4   2
  |   |
  C---D
    3

```

## Solution:

```text
Edges with Weights:

(A, B) with weight 1
(A, C) with weight 4
(B, D) with weight 2
(C, D) with weight 3


List All Edges Sorted by Weight:

(A, B) - 1
(B, D) - 2
(C, D) - 3
(A, C) - 4

Apply Kruskal’s Algorithm:

Add (A, B) to MST (no cycle).
Add (B, D) to MST (no cycle).
Add (C, D) to MST (no cycle).
Skip (A, C) to avoid a cycle.

```

```text

    1
  A---B
      |
      2
      |
      D
  C---D
    3
Sum of Weights: 1 + 2 + 3 = 6
```

## Adjacency List

An adjacency list represents a graph as an array or list of lists. Each list at index i contains the nodes that are adjacent to node i along with the weight of the edge connecting them.

## Edge List

An edge list represents a graph as a list of edges. Each edge is represented as a tuple or list containing the two nodes it connects and the weight of the edge.

### Adjacency list conversion to edge list

```text

adj = [
    [[1, 10], [2, 6], [3, 5]],  # Edges from vertex 0
    [[0, 10], [3, 15]],         # Edges from vertex 1
    [[0, 6], [3, 4]],           # Edges from vertex 2
    [[0, 5], [1, 15], [2, 4]]   # Edges from vertex 3
]

```

We need to convert this adjacency list to an edge list. During the conversion, we need to ensure that each edge is only added once. The condition if u < v ensures that.

```py

edges = []
for u in range(len(adj)):
    for v, wt in adj[u]:
        if u < v:
            edges.append((u, v, wt))
print(edges)


```

```text

edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]


```

## Analysis:

Expected Time Complexity: O(ElogV).
Expected Auxiliary Space: O(Space Complexity: O(V+E), due to storage for edges and Union-Find data structure.).

## Without converting adj list to edge list

```py
class Solution:
    par = []
    rank = []

    @staticmethod
    def union(x: int, y: int) -> bool:
        px = Solution.find(x)
        py = Solution.find(y)
        if px == py:
            return False
        if Solution.rank[px] > Solution.rank[py]:
            Solution.par[py] = px
        elif Solution.rank[px] < Solution.rank[py]:
            Solution.par[px] = py
        else:
            Solution.par[px] = py
            Solution.rank[py] += 1
        return True

    @staticmethod
    def find(x: int) -> int:
        if Solution.par[x] == x:
            return x
        t = Solution.find(Solution.par[x])
        Solution.par[x] = t
        return t

    @staticmethod
    def spanningTree(V: int, E: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda x: x[2])
        Solution.par = [i for i in range(V)]
        Solution.rank = [1] * V
        ans = 0
        for edge in edges:
            u, v, wt = edge
            flag = Solution.union(u, v)
            if flag:
                ans += wt
        return ans

```
