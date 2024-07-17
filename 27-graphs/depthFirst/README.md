## Depth First Traversal

Here, the order does not matter.

## Approach

- Initialize an answer list, a visited list and also initialize the src vertex does no matter which one.
- Find the neighbors of the source vertex.
- Check if any of them is not visited:
  - If not visited, add them to the answer
  - Make its visited index to be True
  - and call a recursive function which do the above operation until nothing left.

## Analysis

`Time Complexity:` `O(V+E) = O(V+2E) = O(V+(V(V-1))/2)= O(V^2)`.
`Space Complexity:` `O(V)`.

```py


class Solution:

    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        ans = []
        ans.append(0)
        visited = [False]*V
        visited[0] = True
        self.helper(0, visited, adj,ans)
        return ans

    def helper(self, src, visited, adj,ans):
        neighbors = adj[src]
        for v in neighbors:
            if visited[v]==False:
                ans.append(v)
                visited[v] = True
                self.helper(v, visited, adj ,ans)

```
