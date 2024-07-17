## Detecting a cycle

1. Follow the Kahn's algorithm.
2. if all nodes are visited or in other words, topological sort is done, then there is no graph as topological sorting is done only in acyclic graph.
3. if Kahn's algorithm is not completed, then we can say there is a cycle.
4. How to check?
   1. Examine if all the nodes are visited.
