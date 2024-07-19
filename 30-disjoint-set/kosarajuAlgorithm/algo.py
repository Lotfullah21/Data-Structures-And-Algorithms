class Solution:
    def dfs(self, graph, vis, st, src):
        vis[src] = True
        for nbr in graph[src]:
            if not vis[nbr]:
                self.dfs(graph, vis, st, nbr)
        st.append(src)

    def kosaraju(self, V, adj):
        vis = [False] * V
        st = []
        for i in range(V):
            if not vis[i]:
                self.dfs(adj, vis, st, i)

        transpose = [[] for _ in range(V)]
        for i in range(V):
            for nbr in adj[i]:
                transpose[nbr].append(i)

        ans = 0
        vis = [False] * V
        while st:
            rem = st.pop()
            if not vis[rem]:
                st2 = []
                self.dfs(transpose, vis, st2, rem)
                ans += 1
        return ans

# Example usage:
V = 5
adj = [
    [1],
    [2, 3],
    [0],
    [4],
    []
]

sol = Solution()
print(sol.kosaraju(V, adj))  # Output: 3
