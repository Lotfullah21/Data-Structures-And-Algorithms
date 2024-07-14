class Solution:

    def LCSof3(self,A,B,C,n1,n2,n3):
        dp = []
        for i in range(n1+1):
            row = []
            for j in range(n2+1):
                col = []
                for k in range(n3+1):
                    col.append(-1)
                row.append(col)
            dp.append(row)
        return self.helper(A,B,C, n1-1, n2-1, n3-1,dp)
    def helper(self, a, b, c, i, j, k,dp):
        if i<0 or j<0 or k<0:
            return 0
        if dp[i][j][k]!=-1:
            return dp[i][j][k]
        if a[i]==b[j] and b[j]==c[k]:
            x = self.helper(a, b, c, i-1, j-1, k-1,dp)
            dp[i][j][k] = x+1
            return x+1
        else:
            x = self.helper(a, b, c, i-1, j, k,dp)
            y = self.helper(a, b, c, i, j-1, k,dp)
            z = self.helper(a, b, c, i, j, k-1,dp)
            dp[i][j][k] = max(x, y, z)
            return max(x, y, z)
        
        
# Example usage
sol = Solution()
A = "geeks"
B = "geeksfor"
C = "geeksforgeeks"
n1, n2, n3 = len(A), len(B), len(C)
print(sol.LCSof3(A, B, C, n1, n2, n3))  # Output: 5