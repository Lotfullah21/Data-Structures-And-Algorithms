class Solution:
    def findMotherVertex(self, V, adj):
        # Initialize visited array and stack
        vis = [False] * V
        st = []
        # Perform DFS from each vertex to find the last finished vertex
        for src in range(V):
            if not vis[src]:
                self.dfs(adj, src, vis, st)
        # Get the last finished vertex
        print(st)
        candidate = st[-1]
        # Reset visited array and perform DFS from candidate
        newVis = [False] * V
        self.dfs(adj, candidate, newVis, [])
        # Check if all vertices are visited in the second DFS
        for vertex in range(V):
            if not newVis[vertex]:
                return -1
        return candidate
    def dfs(self, adj, src, vis, st):
        vis[src] = True
        for ngbr in adj[src]:
            if not vis[ngbr]:
                self.dfs(adj, ngbr, vis, st)
        st.append(src)
        
# Example usage
if __name__ == "__main__":
    solution = Solution()
    # Example graph
    V = 5
    adj = [
        [1, 2],
        [3],
        [3],
        [],
        [2, 3]
    ]
    
    result = solution.findMotherVertex(V, adj)
    print(result)  # Output should be the mother vertex if it exists, else -1