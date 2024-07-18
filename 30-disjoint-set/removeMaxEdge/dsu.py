from typing import List
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:   
        edges.sort(reverse=True)
        parU = [0]*(n+1)
        parV = [0]*(n+1)
        ranka = rankb = [1]*(n+1)
        ans = 0
        for i in range(n+1):
            parU[i]=parV[i]=i
            ranka[i]=rankb[i] = 1
        counta = 1
        countb = 1
        # Lets go through each edge and based on their category and the unions, either we have to keep them or remove them.
        for edge in edges:
            ca, x, y = edge
            if ca==3:
                mergea = self.union(x, y, parU, ranka)
                mergeb = self.union(x, y, parV, rankb)
                # If the edges did not merge, it means there parents are the same and they are already merged.
                if not mergea and not mergeb:
                # We do not need them, increment the count of avoiding edges.
                    ans+=1
                # Which caegories did we merge, if merge a returns True, it means x and y got connected
                if mergea:
                    counta+=1
                if mergeb:
                    countb+=1
            elif ca==2:
                mergeb = self.union(x, y, parV, rankb)
                if not mergeb:
                    ans+=1
                else:
                    countb+=1
            else:
                mergea = self.union(x, y, parU, ranka)
                if not mergea:
                    ans+=1
                else:
                    counta+=1
        # After trying to merge all the edges, mergin is not possible.
        if counta!=n or countb!=n:
            return -1
        return ans
                    
    
    def union(self, u, v, par, rank):
        pu = self.find(u, par)
        pv = self.find(v, par)
        # If there parents are the same, it means they are already connected.
        if pu==pv:
            return False
        if rank[pu]>rank[pv]:
            par[pv] = pu
        elif rank[pv]>rank[pu]:
            par[pu] = pv
        else:
            par[pu] = pv
            rank[pv]+=1
        return True
    
    def find(self,u, par):
        if u==par[u]:
            return u
        temp = self.find(par[u], par)
        par[u] = temp
        return temp
        


# Create an instance of Solution
sol = Solution()

# Define the number of nodes and edges
n = 4
edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [2, 2, 4], [3, 3, 4]]

# Call the maxNumEdgesToRemove method and print the result
result = sol.maxNumEdgesToRemove(n, edges)
print(result)  # Output should be 2