## Dijkstra's Algorithm:

Given a weighted, undirected and connected graph of V vertices and an adjacency list adj where adj[i] is a list of lists containing two integers where the first integer of each list j denotes there is edge between i and j , second integers corresponds to the weight of that edge . You are given the source vertex S and You to Find the shortest distance of all the vertex's from the source vertex S. You have to return a list of integers denoting shortest distance between each node and Source vertex S.

<h3><a href="https://geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1?utm_source=geeksforgeeks">GFG</a></h3>

## Approach

1. Initialization:

- A priority queue pq is initialized.
- A list ans is initialized with infinity to store the shortest distance to each vertex from the source S.

2. Pushing the Source:

- The source vertex S with a distance of 0 is pushed into the priority queue.

3. Processing the Queue:

- While the priority queue is not empty, the vertex with the smallest weight is popped from the queue.
- If this vertex is already processed (i.e., it has a finite value in ans), it is skipped.
- Otherwise, its shortest distance is recorded in ans.
- For each neighbor of this vertex, if the neighbor is not yet processed, the neighbor and its updated distance are pushed into the queue.

4. Returning the Result:

- Finally, the list ans containing the shortest distances is returned.

## Analysis:

`Time Complexity`: At max, we are processing |E| edges and adding each edge takes logE in heap data structure, hence the time complexity for dijkstra's algorithm is
`O(ElogE) = Elog(V*V-1/2) = ElogV^2 = 2ElogV = O(ElogV)`.

`Space Complexity`: At max, we are saving all possible edges in the priority queue `O(E)`.
