class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m = len(s)
        s1 = s[::-1]
        memo = [[-1]*(m) for _ in range(m+1)]
        return self.helper(s, m-1, s1, m-1,memo) 
    def helper(self, s, i, s1, j,memo):
         # Base case: when either index is out of bounds
        if i==-1 or j==-1:
            return 0
        # If already computed
        if memo[i][j]!=-1:
            return memo[i][j]
        if s[i]==s1[j]:
            x = self.helper(s, i-1, s1, j-1, memo)
            memo[i][j] = x+1
            return x+1
        else:
            x = self.helper(s, i-1, s1, j,memo)
            y = self.helper(s, i, s1, j-1, memo)
            memo[i][j] = max(x, y)
            return max(x, y)

if __name__ == "__main__":
    # Example usage:
    sol = Solution()
    print(sol.longestPalindromeSubseq("bbbab"))  # Output: 4
    print(sol.longestPalindromeSubseq("cbbd"))   # Output: 2
            