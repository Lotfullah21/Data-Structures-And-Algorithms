class Solution:
    def numSquares(self, n: int) -> int:
        dp = [-1] * (n + 1)
        return self.helper(n, dp)
    
    def helper(self, n: int, dp: list[int]) -> int:
        if n == 0 or n == 1:
            return n

        if dp[n] != -1:
            return dp[n]

        smallest = float('inf')

        for i in range(1, int(n**0.5) + 1):
            temp = self.helper(n - i * i, dp)
            smallest = min(smallest, temp)

        dp[n] = smallest + 1
        return smallest + 1

solution = Solution()
n = int(input())
result = solution.numSquares(n)
print(result)
