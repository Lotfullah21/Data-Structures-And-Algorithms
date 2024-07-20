## Mother Vertex

Given a Directed Graph, find a Mother Vertex in the Graph (if present).

<h2><a href="https://www.geeksforgeeks.org/problems/mother-vertex/1">GFG</a></h2>

`A Mother Vertex is a vertex through which we can reach all the other vertices of the Graph`

The process involves performing DFS, recording the finishing order, and then verifying if the last finished node can reach all other nodes.

## Approach

If we do dfs on the problem and it is mentioned that the graph has a mother vertex, using kosaraju's first step, the element on the top is our mother vertex.
If it is not mentioned that 100%, there is a mother vertex, we need to verify it after doing dfs? HOW?

take the top of the stack ans save it in var, lets say `answer`, do the dfs again using the ans as the source node, if all other nodes could be visited using the answer, then the answer is our mother vertex, else not.

```p

0 -> 1
0 -> 2
1 -> 3
2 -> 3
4 -> 2
4 -> 3

```

```py

adj = [
    [1, 2],  # Neighbors of vertex 0
    [3],     # Neighbors of vertex 1
    [3],     # Neighbors of vertex 2
    [],      # Neighbors of vertex 3
    [2, 3]   # Neighbors of vertex 4
]

```

### DFS Traversal and Stack Order

Let's perform DFS starting from vertex 0 and see how nodes are added to the stack.

Start DFS from Vertex 0:

Visit 0: Mark it as visited.

- Explore Neighbors of 0:
- Visit Neighbor 1: Mark 1 as visited.
  Explore Neighbors of 1:
- Visit Neighbor 3: Mark 3 as visited.
- No further neighbors of 3, so add 3 to stack.
  Add 1 to stack after finishing its neighbors (3).
  Return to 0.
  Visit Neighbor 2: Mark 2 as visited.
  Explore Neighbors of 2:
- Neighbor 3 is already visited.
- No further neighbors of 2, so add 2 to stack.
- Add 0 to stack after finishing its neighbors (1, 2)

### Visualization with Example

- Here’s a step-by-step visualization:

  - Start DFS from vertex 0:

        - Mark 0, visit 1, mark 1, visit 3, mark 3, add 3 to stack.
        - Finish 1, add 1 to stack.
        - Return to 0, visit 2, mark 2, add 2 to stack.
        - Finish 0, add 0 to stack.

    Resulting stack (in order of addition): 3, 1, 2, 0

The vertex at the top of the stack (0) is then used to verify if it's a mother vertex by performing another DFS.

### DFS Traversal

During DFS, nodes are added to the stack when all their descendants (neighbors) are fully processed. This ensures that nodes that finish their processing later are added to the stack before those that finish earlier.

### Stack Order

Nodes are added in the order they complete their processing in DFS. The node that finishes processing last will be at the top of the stack.

# Analysis:

Expected Time Complexity: `O(V + E)`.
Expected Space Complexity: `O(V)`.
