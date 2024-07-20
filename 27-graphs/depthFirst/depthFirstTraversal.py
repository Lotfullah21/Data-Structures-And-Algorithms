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
                # Call the recursive function on current node which is the neighbors of source node.
                self.dfsOfGraphHelper(adj, v, answer, visited)

if __name__ == "__main__":
    solution = Solution()
    # Example input
    V, E = 5, 4  # 5 vertices, 4 edges
    edges = [
        (0, 1),
        (0, 2),
        (0, 3),
        (2, 4)
    ]
    
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    print("adjacency list =",adj)
    result = solution.dfsOfGraph(V, adj)
    
    # Print the list of vertices in the DFS traversal
    for vertex in result:
        print(vertex, end=" ")
    print()
