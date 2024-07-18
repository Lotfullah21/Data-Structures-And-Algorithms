class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        par = [0]*n
        for i in range(n):
            par[i] = i
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]==1:
                    self.union(i, j, par)
        ans = 0
        for i in range(len(par)):
            if par[i]==i:
                ans+=1
        return ans

    def union(self, a, b, par):
        pa = self.find(a, par)
        pb = self.find(b, par)
        if pa==pb:
            return 
        par[pa] = pb

    def find(self, x, par):
        if x == par[x]:
            return x
        temp = self.find(par[x], par)
        return temp

        
sol = Solution()
isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
islands =sol.findCircleNum(isConnected)
print("Connected Provinces =", islands)