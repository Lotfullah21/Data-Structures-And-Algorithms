# MST

A Minimum Spanning Tree (MST) of a connected, undirected graph is a subset of the edges that connects all the vertices together, without forming any cycles, and with the minimum possible total edge weight.

### Key Characteristics of MST:

- Connected: The tree spans all vertices in the graph, meaning every vertex is reachable from every other vertex.
- Acyclic: As a tree, it does not contain any cycles.
- Minimum Weight: The sum of the weights of the edges in the MST is minimized compared to all other possible spanning trees.

### Properties:

- Uniqueness: An MST is not always unique. There can be multiple spanning trees with the same minimum weight if there are multiple edges with equal weights.
- Tree Structure: The result is a tree (i.e., a connected acyclic graph) with V−1 edges, where V is the number of vertices.
-

## Algorithms to Find MST:

Several algorithms can be used to find the MST of a graph, including:

- Kruskal’s Algorithm: Sorts all edges by weight and adds them to the MST, ensuring no cycles are formed using a union-find data structure.
- Prim’s Algorithm: Builds the MST by starting from an initial vertex and adding the smallest edge that connects a vertex in the MST to a vertex outside the MST.

```text
      10
  A--------B
  |\     /|
  | \   / |
  |  \ /  |
  |   X   |
  |  / \  |
  | /   \ |
  |/     \|
  C--------D
      15


```

```text

      10
  A--------B
      |
      6
      |
      C
Sum of Weights: 4 + 5 + 6 = 15
```

## Applications of MST:

- Network Design: Minimizing the cost of connecting nodes in a network (e.g., computer networks, telecommunication networks).
- Clustering: In machine learning, MST can be used for clustering by connecting points in a way that minimizes the total distance.
- Approximation Algorithms: MST is used in approximation algorithms for problems like the Traveling Salesman Problem (TSP).
