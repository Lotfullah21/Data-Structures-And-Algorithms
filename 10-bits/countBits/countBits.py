class Solution:
    def setBits(self,N):
        ans = 0
        for i in range(32):
            if self.checkBit(N, i)==True:
                ans+=1
        return ans            
    def checkBit(self, N, i):
        if N&(1<<i)!=0:
            return True
        else:
            return False        
N = 41
solution = Solution()
ans = solution.setBits(N)
print(ans)