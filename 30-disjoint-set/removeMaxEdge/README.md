## Remove Max Number of Edges to Keep Graph Fully Traversable

Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

<h2><a href="https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/">leetcode</a></h2>

##### Solution Approach

Union-Find Data Structure:

Used to keep track of connected components.
Two separate union-find structures are used: one for Alice and one for Bob.
Processing the Edges:

First, process type-3 edges since they are useful for both Alice and Bob.
Then, process type-2 edges for Bob and type-1 edges for Alice.
Edge Removal:

Count and remove redundant edges that do not contribute to the connectivity of the graph for either Alice or Bob.
Connectivity Check:

After processing all edges, ensure that both Alice and Bob can traverse the entire graph.
If either cannot, return -1.

#### Step-by-Step Execution

Input:

n = 4
edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [2, 2, 4], [3, 3, 4]]
Sorting and Initialization:

Sort edges in reverse order by type: [[3, 3, 4], [3, 2, 3], [3, 1, 2], [2, 2, 4], [1, 1, 3]]
Initialize union-find structures for Alice and Bob.
Processing Edges
Edge [3, 3, 4]:

##### Union for Alice and Bob:

Both successful: counta = 2, countb = 2
Edge [3, 2, 3]:

##### Union for Alice and Bob:

Both successful: counta = 3, countb = 3
Edge [3, 1, 2]:

##### Union for Alice and Bob:

Both successful: counta = 4, countb = 4
Edge [2, 2, 4]:

##### Union only for Bob:

Not successful (already connected): ans = 1
Edge [1, 1, 3]:

##### Union only for Alice:

Not successful (already connected): ans = 2
Connectivity Check
Ensure both Alice and Bob can traverse the entire graph:
counta = 4 and countb = 4 (both equal n), so the graph is fully connected for both.
Return Result
Return the number of removable edges: ans = 2

Time Complexity: O(mlogm).
Space Complexity: O(m).
