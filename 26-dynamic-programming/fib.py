class Solution:
    #Function to find the nth fibonacci number using top-down approach.
    def findNthFibonacci(self,number, dp):
        # Your Code Here
        if number == 1 or number == 0:
            return number
        if dp[number]!=None:
            return dp[number]
        dp[number] = self.findNthFibonacci(number-1,dp) + self.findNthFibonacci(number-2,dp)
        return dp[number]
    
    
n = 6
dp = [None]*92
solution = Solution()
ans = solution.findNthFibonacci(n,dp)
print(ans)