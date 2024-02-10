"""You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through,
1 means the cell contains a cherry that you can pick up and pass through, or
-1 means the cell contains a thorn that blocks your way.
Return the maximum number of cherries you can collect by following the rules below:

Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).
After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.
"""

class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[None] * m for _ in range(n)] for _ in range(m)]
        
        ans = self.cherryPickupHelper(grid, 0, 0, 0, dp)

        if ans == float('-inf'):
            return 0
        else:
            return ans

    def cherryPickupHelper(self, grid: List[List[int]], row1: int, col1: int, row2: int, dp: List[List[List[int]]]) -> int:
        col2 = row1 + col1 - row2
        
        if row1 >= len(grid) or row2 >= len(grid) or col1 >= len(grid[0]) or col2 >= len(grid[0]) or grid[row1][col1] == -1 or grid[row2][col2] == -1:
            return float('-inf')

        if dp[row1][col1][row2] is not None:
            return dp[row1][col1][row2]

        if row1 == len(grid) - 1 and col1 == len(grid[0]) - 1 and row2 == len(grid) - 1 and col2 == len(grid[0]) - 1:
            return grid[row1][col1]

        temp1 = self.cherryPickupHelper(grid, row1, col1 + 1, row2, dp)
        temp2 = self.cherryPickupHelper(grid, row1 + 1, col1, row2 + 1, dp)
        temp3 = self.cherryPickupHelper(grid, row1, col1 + 1, row2 + 1, dp)
        temp4 = self.cherryPickupHelper(grid, row1 + 1, col1, row2, dp)

        maxTemp = max(temp1, temp2, temp3, temp4)
        
        contribution = grid[row1][col1] if row1 == row2 and col1 == col2 else grid[row1][col1] + grid[row2][col2]

        if maxTemp == float('-inf'):
            dp[row1][col1][row2] = float('-inf')
        else:
            dp[row1][col1][row2] = maxTemp + contribution

        return dp[row1][col1][row2]
