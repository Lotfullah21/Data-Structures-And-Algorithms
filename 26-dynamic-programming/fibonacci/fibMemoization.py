class Solution:
    #Function to find the nth fibonacci number using top-down approach.
    def findNthFibonacci(self,number, dp):
        if number == 1 or number == 0:
            return number
        if dp[number]!=None:
            return dp[number]
        dp[number] = self.findNthFibonacci(number-1,dp) + self.findNthFibonacci(number-2,dp)
        return dp[number]
    
solution = Solution()
n = int(input("Enter a number: "))
dp = [None]*(n+1)
ans = solution.findNthFibonacci(n,dp)
print(ans)