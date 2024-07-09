class Solution:
    def numberOfPaths(self, row: int, column: int) -> int:
        dp = [[-1] * column for _ in range(row)]
        
        # for i in range(row):
        #     for j in range(column):
        #         dp[i][j] = -1
        
        return self.pathsHelper(row - 1, column - 1, dp)
    
    def pathsHelper(self, sourceRow: int, sourceColumn: int, dp: list[list[int]]) -> int:
        # we are reaching out of index.
        if sourceRow < 0 or sourceColumn < 0:
            return 0
        # base case.
        if sourceRow == 0 and sourceColumn == 0:
            return 1
        if dp[sourceRow][sourceColumn] != -1:
            return dp[sourceRow][sourceColumn]
        # move one step down, or travel one row.
        path1 = self.pathsHelper(sourceRow - 1, sourceColumn, dp)
        # move one step right or travel one column.
        path2 = self.pathsHelper(sourceRow, sourceColumn - 1, dp)
        
        dp[sourceRow][sourceColumn] = path1 + path2
        return dp[sourceRow][sourceColumn]
    
    
solution = Solution()
solution.numberOfPaths(7,4)
