class Solution:  
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        self.dp = [-1]*n
        return self.helper(a, n-1)
    def helper(self, a, i):
        if i<0:
            return 0
        if i==0:
            return a[0]
        if self.dp[i]!=-1:
            return self.dp[i]
        x = self.helper(a, i-1)
        y = self.helper(a, i-2)+a[i]
        self.dp[i] = max(x, y)
        return self.dp[i]