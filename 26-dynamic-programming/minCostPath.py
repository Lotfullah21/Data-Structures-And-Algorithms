"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

"""

class Solution:
    def minPathSum(self,grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for _ in range(n)] for col in range(m)]   
        return self.minCostPathHelper(grid, m-1, n-1,dp)
        
    def minCostPathHelper(self,grid, row, col,dp):
        if row<0 or col<0:
            return float("inf")
        if row==0 and col==0:
            return grid[row][col]
        if dp[row][col]!=-1:
            return dp[row][col]
        x = self.minCostPathHelper(grid, row-1, col,dp)
        y = self.minCostPathHelper(grid, row, col-1,dp)
        ans = min(x,y) + grid[row][col]
        dp[row][col] = ans
        return ans
    
grid = [[1,3,1],[1,5,1],[4,2,1]]
solution = Solution()
print(solution.minPathSum(grid))