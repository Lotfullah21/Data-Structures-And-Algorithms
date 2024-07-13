class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        i = len(text1)
        j = len(text2)
        memo = []
        for _ in range(i):
            arr = []
            for _ in range(j):
                arr.append(-1)
            memo.append(arr)
            
        return self.helper(text1, i-1, text2, j-1, memo)
        
        
    def helper(self, s1, i, s2, j, dp):
        if i==-1 or j==-1:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        if s1[i]==s2[j]:
            x = self.helper(s1, i-1, s2, j-1,dp)
            dp[i][j] = x+1
            return x+1
        else:
            x = self.helper(s1, i-1, s2, j,dp)
            y = self.helper(s1, i, s2, j-1,dp)
            dp[i][j] = max(x, y)
            return max(x, y)
        
        
        
if __name__ == "__main__":
    # Example usage:
    sol = Solution()
    print(sol.longestCommonSubsequence("abcde", "ace"))  # Output: 3
    print(sol.longestCommonSubsequence("abc", "abc"))    # Output: 3
    print(sol.longestCommonSubsequence("abc", "def"))    # Output: 0