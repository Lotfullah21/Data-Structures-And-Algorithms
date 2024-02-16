class Solution:
    def dfsOfGraphHelper(self, adj, src, answer, visited):
        neighbors = adj[src]
        for v in neighbors:
            if not visited[v]:
                answer.append(v)
                visited[v] = True
                self.dfsOfGraphHelper(adj, v, answer, visited)
                
    def dfsOfGraph(self, V, adj):
        answer = []
        visited = [False] * V
        answer.append(0)
        visited[0] = True
        self.dfsOfGraphHelper(adj, 0, answer, visited)
        return answer

if __name__ == "__main__":
    solution = Solution()
    V, E = map(int, input().split())
    adj = [[] for _ in range(V)]
    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    result = solution.dfsOfGraph(V, adj)
# print the list of vertices.
    for vertex in result:
        print(vertex, end=" ")
    print()
