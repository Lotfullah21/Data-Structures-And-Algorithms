from collections import deque
class Solution:
    def Bfs(self, visited ,adj, srcNode):
        dq = deque()
        dq.append(srcNode)
        visited[srcNode] = True
        while dq:
            removed = dq.popleft()
            for u in adj[removed]:
                if visited[u]==False:
                    visited[u] = True
                    dq.append(u)
                        
    def reachable(self, V ,adj, destNode):
        srcNode = 0
        visited = [False]*V
        self.Bfs(visited, adj, srcNode)
        if visited[destNode]!=True:
            print("All nodes are not reachable")
        else:
            print("All nodes are reachable")
        
solution = Solution()
adj = [[1, 2, 3],  # Node 0 is connected to nodes 1, 2, and 3
            [],         # Node 1 has no outgoing connections
            [],         # Node 2 has no outgoing connections
            [],         # Node 3 has no outgoing connections
            []]         # Node 4 has no outgoing connections
V = 10        
solution.reachable(V,adj,4)
