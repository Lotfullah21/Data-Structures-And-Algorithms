## Topological sorting

linear ordering of a graph such that for every directed edge (u,v), vertex u comes before v in the ordering.
it is only possible for direct and acyclic graph, because we want to preserve the ordering, if it is not directed or it has circle, then there is no ordering.

### Kahn's Algorithm

1. Create an inDegree array:
   1. create an empty array of size V.
   2. count the number of in-degree for each node and add the count of it to the newly created array.
2. Create a queue
3. Add the elements with zero in-degree to the queue and remove it.
4. Go to the removed vertex's neighbors and decrement their in-degree by 1.
   1. if in-degree becomes zero, add to the queue.
5. Repeat step 3-4 until the queue becomes empty.

### Detecting a cycle

1. Follow the Kahn's algorithm.
2. if all nodes are visited or in other words, topological sort is done, then there is no graph as topological sorting is done only in acyclic graph.
3. if Kahn's algorithm is not completed, then we can say there is a cycle.
4. How to check?
   1. Examine if all the nodes are visited.
