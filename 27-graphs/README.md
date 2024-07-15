## Graph

Connection of nodes and edges are known as a graph.

It is a non-linear data structure unlike a tree which is a linear data structure.
We cannot use trees when there is random connections among the nodes.

### Properties

- Unlike a tree, here is no hierarchy, in trees we had parent node then the child nodes, here those child nodes are neighbors.
- And also, a node here can have any number of connections.
- In graph we can have cycles unlike trees, which means we can comeback to the same node in a tree.
- We can move in both directions unlike a tree.

### Applications

- Computer networks
- Social networks
- Circuits
- Molecular Structure

### Example

Lets consider a directed graph with three vertices, 0, 1, 2.

## Classifications

### 1. Based on edges:

1. Directed graph: the edges are directional, we can move only from source to destination, not form destination from source.
   Examples: Social media apps like instagram, when we follow someone there is an edge created.

```text
1 --> 2
      |
      v
      3

```

2. Undirected graph: The edges are two directional, from source to destination and from destination to source.
   It means the movement is possible in and from both directions.

```text.
1 -- 2
 \
  \
   3

```

### 2. Based on weighted edges:

Unlike trees where we could assign weights only to nodes, in graph we can assign weights to edges as well.

1. in a directional graph or undirectional graph, each edge can carry a weight, These kinds of graphs are called weighted graph.

```text
    2
1 ------ 2
 \      /
  \ 3  /
   \  /
    3
Edge (1-2) has a weight of 2
Edge (2-3) has a weight of 2
Edge (1-3) has a weight of 3.

    2
1 -----> 2
       /
      / 2
     v
     3
     ^
     | 3
     |
     1


Edge 1 --> 2 has a weight of 2
Edge 2 --> 3 has a weight of 2
Edge 1 --> 3 has a weight of 3

```

###### Real life examples:

1. Road networks(Weighted)
   Description: Cities or intersections as nodes and roads as edges.
   Weights: The weight of an edge can represent the distance, travel time, or cost of traveling from one node to another.
   Example: Google Maps uses weighted graphs where the weight can represent travel time considering traffic conditions.

2. Social Networks(Unweighted)

Description: People as nodes and friendships or connections as edges.
Unweighted: Edges simply represent the existence of a connection, not the strength or type of relationship.
Example: Facebook's friendship graph where an edge represents a friendship without considering how close the friendship is.

## Graph Representation Using Different Data Structures

- Edge list
- Adjacency list
- Adjacency matrix
