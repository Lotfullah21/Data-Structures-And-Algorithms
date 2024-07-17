class Solution:
    
                    
    def dfsOfGraph(self, V, adj):
        # share the array answer across functions.
        answer = []
        visited = [False] * V
        # If we want to pick 0 as source node, then add the below lines of code.
        answer.append(0)
        visited[0] = True
        # Call it once, be appending 0, we will be  starting from 0.
        self.dfsOfGraphHelper(adj, 0, answer, visited)
        return answer
    
    def dfsOfGraphHelper(self, adj, src, answer, visited):
        # get the neighbors of current source node
        neighbors = adj[src]
        # check for each neighbors
        for v in neighbors:
            # If not visited, add them to the answer.
            if not visited[v]:
                answer.append(v)
                visited[v] = True
                # Call the recursive function current node which is neighbors of source node.
                self.dfsOfGraphHelper(adj, v, answer, visited)
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
