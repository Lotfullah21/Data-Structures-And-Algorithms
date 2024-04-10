class Solution:    
    def nCrModp(self, n, r):
        MOD = 10**9 + 7
        dp = [[0 for _ in range(r+1)] for _ in range(n+1)]
        
        for i in range(n+1):
            for j in range(min(i, r)+1):
                # Base cases
                if j == 0 or j == i:
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD
                    
        return dp[n][r]

# Test the function
sol = Solution()
print(sol.nCrModp(3, 2))  
print(sol.nCrModp(4, 2)) 
