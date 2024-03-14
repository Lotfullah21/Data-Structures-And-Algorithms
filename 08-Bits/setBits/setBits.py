class Solution:
    def setKthBit(self, N, K):
        answer = N | (1<<K)
        return answer
    

N = 10 
K = 2
solution = Solution()
result  = solution.setKthBit(N,K)
print(result)