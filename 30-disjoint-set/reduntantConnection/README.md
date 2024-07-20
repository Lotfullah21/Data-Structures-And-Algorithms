# Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

<h2><a href="https://leetcode.com/problems/redundant-connection/submissions/1327062786/">leetcode</a></h2>

## Kruskal Algorithm

Using this algorithm, we can keep the track of the edges given, because we have to follow the order.
To detect the cycle, whenever, there is two same vertices in the same set, it means there is a cycle.

## Approach

#### Union-Find Data Structure:

##### Initialization: We initialize two arrays, par and rank. par keeps track of the parent of each node, and rank helps in balancing the tree by keeping track of the depth of trees.

Find Operation: This function returns the root of the set containing the element x. It uses path compression to make the tree flat, ensuring that future queries are faster.
Union Operation: This function takes two nodes and unions their sets if they belong to different sets. It uses union by rank to keep the tree balanced.

#### Detecting Redundant Connection:

We iterate through each edge in the input list. For each edge, we perform the union operation on its nodes.
If the union operation returns False, it means that adding this edge creates a cycle, hence this edge is the redundant connection.

## Example

Given the edges [[1, 2], [1, 3], [2, 3]]:

#### Initialization:

par = [0, 1, 2, 3]
rank = [1, 1, 1, 1]

#### Processing Edge [1, 2]:

#### Union(1, 2) is successful:

par = [0, 1, 1, 3]
rank = [1, 2, 1, 1]

#### Processing Edge [1, 3]:

#### Union(1, 3) is successful:

par = [0, 1, 1, 1]
rank = [1, 2, 1, 1]

#### Processing Edge [2, 3]:

Union(2, 3) returns False because 2 and 3 already have the same root, indicating that adding this edge would form a cycle.
Hence, the redundant connection is [2, 3].
