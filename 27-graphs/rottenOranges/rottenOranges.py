from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count1=0;count2=0
        q = deque()
        # All directions, (1, 0) means one step above, (0,-1) means one step to the right
        directions = [(1, 0),(-1, 0),(0,1),(0,-1)]
        # Looking and adding all the initial rotten oranges.
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j,0))
                    count2+=1
                elif grid[i][j]==1:
                    count1+=1
        if count1==0:
            return 0
        elif count2==0:
            return -1
        ans = -1
        while q:
            row, col, time = q.popleft()
            ans = time
            for rdir, cdir in directions:
                rowNum = row+rdir
                colNum = col + cdir
                # print(rowNum,colNum)
                if 0<=rowNum<m and 0<=colNum<n and grid[rowNum][colNum]==1:
                    q.append((rowNum, colNum, time+1))
                    grid[rowNum][colNum]=2
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        return ans
        
        
solution = Solution()

grid = [[2,1,1],[1,1,0],[0,1,1]]
print("Time",solution.orangesRotting(grid))
