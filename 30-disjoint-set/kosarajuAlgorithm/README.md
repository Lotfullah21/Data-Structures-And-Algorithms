## Strongly Connected Components (Kosaraju's Algo)

Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, Find the number of strongly connected components in the graph.

<h2><a href="https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1?utm_source=geeksforgeeks">GFG</a></h2>

## Important steps in KosaRaju algorithm

### First DFS for Finishing Times:

The first DFS ensures that we process nodes in the order of their completion, capturing the essence of their connectivity.

### Graph Transposition:

Reversing the graph's edges is crucial because it helps in identifying SCCs during the second DFS.

### Second DFS for SCCs:

Processing nodes in the order defined by the first DFS's finishing times ensures that we start new DFS calls for new SCCs, counting each one accurately.
