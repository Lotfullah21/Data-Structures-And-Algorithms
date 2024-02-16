from collections import deque
from typing import List
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        
        visited = [False]*V
        q = deque()
        ans = []
        
        q.append(0)
        visited[0] = True
        
        while q:
            
            removed = q.popleft()
            ans.append(removed)
            for u in adj[removed]:
                if visited[u]==False:
                    visited[u] = True
                    q.append(u)
        return ans
       
# Example usage:
# You can create an instance of Solution and call the bfsOfGraph method with the desired V and adjacency list.
solution = Solution()
V, E = map(int, input().split())  # Input the number of vertices and edges.

adj = [[] for _ in range(V)]
for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)  # Assuming an undirected graph.

result = solution.bfsOfGraph(V, adj)

# Output the BFS traversal.
for node in result:
    print(node, end=" ")
print()
