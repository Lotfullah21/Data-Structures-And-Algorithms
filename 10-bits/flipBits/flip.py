class Solution:
    def flipKthBit(self, N, K):
        answer = N^(1<<K)
        return answer
    
if __name__ =="__main__":
    N,K = list(map(int, input().split()))
    solution = Solution()
    result  = solution.flipKthBit(N,K)
    print(result)