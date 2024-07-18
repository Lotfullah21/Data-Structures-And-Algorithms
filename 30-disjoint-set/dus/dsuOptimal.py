from typing import List
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        edges.sort(reverse=True, key=lambda x: x[0])
        parU = [0]*(n+1)
        parV = [0]*(n+1)
        ranka = rankb = [1]*(n+1)
        ans = 0
        for i in range(n+1):
            parU[i]=parV[i]=i
            ranka[i]=rankb[i] = 1
        counta = 0
        countb = 0
        # Lets go through each edge and based on their category and the unions, either we have to keep them or remove them.
        for edge in edges:
            ca, x, y = edge
            if ca==3:
                mergea = self.union(x, y, parU, ranka)
                mergeb = self.union(x, y, parV, rankb)
                # If the edges did not merge, it means there parents are the same and they are already merged.
                if mergea == False and mergeb==False:
                # We do not need them, increment the count of avoiding edges.
                    ans+=1
                # Which caegories did we merge, if merge a returns True, it means x and y got connected
                if mergea:
                    counta+=1
                if mergeb:
                    countb+=1
            elif ca==2:
                mergea = self.union(x, y, parU, ranka)
                if mergea==False:
                    ans+=1
                else:
                    counta+=1
            else:
                mergeb = self.union(x, y, parV, rankb)
                if mergeb==False:
                    ans+=1
                else:
                    countb+=1
        # After trying to merge all the edges, mergin is not possible.
        if counta!=n-1 or countb!=n-1:
            return -1
        return ans
                    
    
    def union(self, u, v, par, rank):
        pu = self.find(u, par)
        pv = self.find(v, par)
        # If there parents are the same, it means they are already connected.
        if pu==pv:
            return False
        if rank[pu]>rank[pv]:
            par[v] = pu
        elif rank[pv]>rank[pu]:
            par[u] = pv
        else:
            par[u] = pv
            rank[pv]+=1
        return True
    
    def find(self,u, par):
        if u==par[u]:
            return u
        temp = self.find(par[u], par)
        par[u] = temp
        return temp
        
