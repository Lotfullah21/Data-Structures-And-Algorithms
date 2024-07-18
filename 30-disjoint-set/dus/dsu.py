class Solution:
    def __init__(self, V):
        self.par = [0]*V
        for i in range(V):
            self.par[i] = i
        # self.par = list(range(V)). [0, 1, 2, ..., V-1]
    def connectedComponents(self, edges, V):
        # Find the u and v edges, make sure to iterate over edges.
        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            self.union(u,v)
        # for u,v in edges:
        #     self.union(u, v)
            
        c = 0
        for i in range(len(self.par)):
            if self.par[i]==i:
                c+=1
        return c
    # Merge the two vertex with common edges.
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        # if parents are the same, do nothing.
        if pu==pv:
            return 
        # Make parent of pu to be pv
        self.par[pu] = pv
    # Find the parent of the vertex v
    def find(self,u):
        if u==self.par[u]:
            return u
        temp = self.find(self.par[u])
        return temp
    
    
# Example usage:
edges = [(0, 1), (1, 2), (3, 4)]
V = 5
solution = Solution(V)
print(solution.connectedComponents(edges, V))  # Output: 3