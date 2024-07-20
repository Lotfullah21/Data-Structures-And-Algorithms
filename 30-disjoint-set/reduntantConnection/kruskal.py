from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [0]*(n+1)
        rank = [1]*(n+1)        
        for i in range(n+1):
            par[i] = i
        for i in range(n+1):
            u = edges[i][0]
            v = edges[i][1]
            flag = self.union(u, v, par, rank)
            if flag==False:
                return edges[i]
    def union(self, u, v, par, rank):
        pu = self.find(u, par)
        pv = self.find(v, par)
        if pu==pv:
            return False
        if rank[pu]>rank[pv]:
            par[pv] = pu
        elif rank[pv]>rank[pu]:
            par[pu] = pv
        else:
            par[pu] = pv
            rank[pv]+=1
    def find(self, x, par):
        if x==par[x]:
            return x
        temp = self.find(par[x], par)
        par[x] = temp
        return temp
    
    
# Example usage
edges = [[1, 2], [1, 3], [2, 3]]
solution = Solution()
print(solution.findRedundantConnection(edges))  # Output: [2, 3]