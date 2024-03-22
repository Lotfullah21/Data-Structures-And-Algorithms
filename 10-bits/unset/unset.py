class Solution:
    def unsetKthBit(self, N, K):
        ans = 0
        if self.checkBit(N,K) == True:
            ans = N^(1<<K)
        return ans
    def checkBit(self, N,K):
        if N&(1<<K)!=0:
            return True
        return False
if __name__ =="__main__":
    N,K = list(map(int, input().split()))
    solution = Solution()
    result  = solution.unsetKthBit(N,K)
    print(result)