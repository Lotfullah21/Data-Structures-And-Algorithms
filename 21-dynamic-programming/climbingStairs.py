"""
There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. 
Count the number of ways, the person can reach the top (order does matter).
"""
class Solution:
    def __init__(self):
        self.dp = []

    def countWays(self, n: int) -> int:
        self.dp = [-1] * (n + 1)
        return self.climbStairsHelper(n)

    def climbStairsHelper(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        if self.dp[n] != -1:
            return self.dp[n]
        step1 = self.climbStairsHelper(n - 1)
        step2 = self.climbStairsHelper(n - 2)

        self.dp[n] = (step1 + step2)%1000000007
# added a new line
        return self.dp[n]