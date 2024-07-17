class Solution:
    @staticmethod
    def dfsOfGraphHelper(adj, src, vis):
        nbrs = adj[src]
        for v in nbrs:
            if not vis[v]:
                vis[v] = True
                Solution.dfsOfGraphHelper(adj, v, vis)

    @staticmethod
    def numProvinces(adj, V):
        # Convert adjacency matrix to adjacency list
        graph = [[] for _ in range(V)]
        for i in range(V):
            for j in range(len(adj[i])):
                if adj[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        vis = [False] * V
        count = 0
        for i in range(V):
            if not vis[i]:
                Solution.dfsOfGraphHelper(graph, i, vis)
                count += 1
        return count

if __name__ == "__main__":
    V = int(input())
    adj = []
    for _ in range(V):
        row = list(map(int, input().split()))
        adj.append(row)
    provinces = Solution.numProvinces(adj, V)
    print(provinces)
