class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        
        par = [0]*(V)
        rank = [0]*(V)
        edges = []
        # Convert the adjacency list edge list
        for u in range(V):
            for v, wt in adj[u]:
                if u<v:
                    edges.append((u, v, wt))
                    
        edges.sort(key=lambda x: x[2])
        for i in range(V):
            par[i] = i  
            
        ans = 0
        s = 0
        mstEdges = []
        for u, v, wt in edges:
            flag = self.union(u, v, par, rank)
            if flag:
                ans+=wt
                s+=1
                mstEdges.append((u, v, wt))
            # MAXIMUM number of edges we can have is V-1, once we added V-1 edges, stop.
            if s==V-1:
                break
        print("edges that are in our mst =",mstEdges)
        return ans
    
    def union(self, u, v, par, rank):
        pu = self.find(u, par)
        pv = self.find(v, par)
        # If they have the same parent, merging does not happen
        if pu==pv:
            return False
        if rank[pu]>rank[pv]:
            par[pv]= pu
        elif rank[pv]>rank[pu]:
            par[pu] = pv
        else:
            par[pu] = pv
            rank[pv]+=1
        return True
            
    def find(self, x, par):
        if x==par[x]:
            return x
        par[x] = self.find(par[x], par)
        return par[x] 
    
    
adj = [
    [[1, 10], [2, 6], [3, 5]],  # Edges from vertex 0
    [[0, 10], [3, 15]],         # Edges from vertex 1
    [[0, 6], [3, 4]],           # Edges from vertex 2
    [[0, 5], [1, 15], [2, 4]]   # Edges from vertex 3
]

V = 4
sol = Solution()
print("total weight of spanning tree edges =",sol.spanningTree(V, adj))