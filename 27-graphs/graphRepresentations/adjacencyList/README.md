## Adjacency List

Each index represent a vertex and the list inside that index represents the vertices adjacent to that index(vertex).

[[1,2],[0,2],[0,1,3],[2]]

which means for vertex-0, adjacent vertices are vertex-1 and vertex-2.
For vertex-two, adjacent vertices are vertex-0 and vertex-1 and so on.

It is an array of lists where it can be represented:

- Dynamic Sized Array(List)
- Linked List

## Dynamic Sized Array:

They are cache friendly and easy to implement.
It also has the disadvantage of doubling its size while adding some value in some particular times.

### Space used:

One of the main advantages of adjacency list over adjacency matrix is here we do not need to store the information about the nodes that are not connected.

- Undirected Graph: For every edge, there is two connections coming and going and one for the vertex (Theta(V+2E))
- Directed Graph: We need to (V+E) space to store the information about directed graph.

### Operation:

- Edge U to V: To check if there is an edge from u to v, we need to go and find the u, then search through whole u to find if there is adjacency between them (`Theta(V)`).
- Find all adjacent of U: Go to index u, how many vertices (indices) are stored there, in fact it is degree of a vertex which is how many incoming or outgoing edges are there in a vertex(`Theta(degree)`).
- Find degree of U: Go to index U and count how many elements are there in that list, it can be done at constant time(`Theta(1)`).
- Adding an edge: Go to U and append an element to that index, it can be done at `Theta(1)` operation.
- Remove Edge: Go to U and remove an element from that index, at the worst case, it might takes `O(N)` operations.

In most of the real scenarios we are not having (V\*V) connections, in fact the connections are muc lesser and this is one of the main reason behind not using Adjacency matrix.

#### Sparse Graph:

A graph that the connections are less than (V)(V-1) for directed and (V)(V-1)/2 for undirected graph are knows as sparse graph

#### Dense Graph:

If the number of connections between vertices are close to the above numbers, then that graph is called dense graph.
