class Solution:
    def dfsOfGraphHelper(self, adj, src, visited):
        # get the neighbors of current source node
        neighbors = adj[src]
        # check for each neighbors
        for v in neighbors:
            # If not visited, add them to the answer.
            if not visited[v]:
                visited[v] = True
                # Call the recursive function current node which is neighbors of source node.
                self.dfsOfGraphHelper(adj, v, visited)                             
    def dfsOfGraph(self, V, adj):
        visited = [False] * V
        res = 0
        for u in range(len(adj)):
            if visited[u] == False:
                res +=1    
                # Call it once, be appending 0, we will be  starting from 0.
                self.dfsOfGraphHelper(adj, u,visited)
        return res

if __name__ == "__main__":
    solution = Solution()
    V, E = map(int, input().split())
    adj = [[] for _ in range(V)]
    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    result = solution.dfsOfGraph(V, adj)
    print(result)